import praw
from praw.models import MoreComments
from getpass import getpass

from constants import *
from private_constants import *
from rating_utils import *
from date_utils import *

def create_reddit():
	passwd = redd_password
	if len(passwd) == 0:
		print(f"u/{redd_username}, Please enter your Reddit password")
		passwd = getpass("Password: ")
	else:
		print(f"UNSAFE PASSWORD ENTRY WARNING: u/{redd_username}, your password is currently stored in `private_constants.py` file, which is UNSAFE!")
		print("You don't have to enter your password now, but KEEP IN MIND that a malicious program, or other person that gets access to your PC might read that file and steal your Reddit password!")
		print("So please consider navigating to that file and erasing `redd_password` to \"\"(it should be like this: `redd_password = \"\"`). After that, CarXRides-ScoresFetcher will be asking for password each run, which is more secure than having password stored in a file")
		print("If you have suspicion that the password got stolen, navigate to your Reddit account and change the password. I recommend using a trusted password generator(for example, Safari browser automatically detects and generates a password when needed)")
	return praw.Reddit(client_id=api_client_id, client_secret=api_secret, user_agent=api_user_agent, username=redd_username, password=passwd)

def get_subreddit(reddit):
	return reddit.subreddit(subreddit_name)

def get_moderators(subreddit):
	return subreddit.moderator()

def get_muted(subreddit, is_mod):
	users = []
	if is_mod:
		for user in subreddit.muted():
			users.append(user)
	else:
		print(f"Unable to get muted users in the r/{subreddit_name}: Reddit only allows that information to moderators")
	return users

def fetch_posts_from_date_range(start_date, end_date, reddit, muted):
	subreddit = get_subreddit(reddit)
	posts = subreddit.new(limit = None)
	filtered_posts = []
	for post in posts:
		date = post.created_utc
		if (date > start_date) and (date < end_date) and (post.link_flair_text == "Pic/Clip") and (post.author not in muted):
			filtered_posts.append(post)
	return filtered_posts

def retrieve_comments(submission, start_date, end_date, mods, muted):
	comments_dict = { "post_id": [], "author": [], "is_mod": [], "rating": [], "body": [], "datetime": [] }
	top_comment = { "text": "<none>", "author": "", "score": -999 }
	for comment in submission.comments:
		date = comment.created_utc
		if (date < start_date) or (date > end_date):
			continue

		if type(comment) == MoreComments:
			continue

		# OP cant rate himself so... filter him out. and some bots too
		if comment.author == submission.author:
			continue

		if comment.author in bots_usernames:
			continue

		if comment.body in forbidden_comments:
			continue

		if comment.author in muted:
			continue

		if top_comment["score"] < comment.score:
			top_comment["text"] = comment.body
			top_comment["author"] = comment.author
			top_comment["score"] = comment.score
		rating = extract_rating(comment.body)
		is_mod = False
		if comment.author in mods:
			is_mod = True
		comments_dict["author"].append(comment.author)
		comments_dict["post_id"].append(submission.id)
		comments_dict["body"].append(comment.body)
		comments_dict["rating"].append(rating)
		comments_dict["is_mod"].append(is_mod)
		comments_dict["datetime"].append(time_to_string(time_from_utc(date)))
	return (comments_dict, top_comment)

# Retrieves all posts & comments from a specified date range, calculates ratings
# and returns two disctionaries: posts and comments
def fetch_posts_and_comments_from_date_range(start_date, end_date, reddit, is_mod):
	posts_dict = { "title": [], "id": [], "author": [], "is_mod": [], "rating": [], "datetime": [], "top_comment": [] }
	comments_dict = { "post_id": [], "author": [], "is_mod": [], "rating": [], "body": [], "datetime": [] }
	subreddit = get_subreddit(reddit)
	mods = get_moderators(subreddit)
	muted = get_muted(subreddit, is_mod)
	posts = fetch_posts_from_date_range(start_date, end_date, reddit, muted)
	for post in posts:
		(comments_data, top_comment) = retrieve_comments(post, start_date, end_date, mods, muted)
		comments_dict["author"].extend(comments_data["author"])
		comments_dict["post_id"].extend(comments_data["post_id"])
		comments_dict["body"].extend(comments_data["body"])
		comments_dict["rating"].extend(comments_data["rating"])
		comments_dict["is_mod"].extend(comments_data["is_mod"])
		comments_dict["datetime"].extend(comments_data["datetime"])
		is_mod = False
		if post.author in mods:
			is_mod = True
		posts_dict["title"].append(post.title)
		posts_dict["id"].append(post.id)
		posts_dict["author"].append(post.author)
		posts_dict["rating"].append(calculate_rating(comments_data["rating"]))
		posts_dict["is_mod"].append(is_mod)
		posts_dict["datetime"].append(time_to_string(time_from_utc(post.created_utc)))
		posts_dict["top_comment"].append(top_comment)
	return posts_dict, comments_dict
