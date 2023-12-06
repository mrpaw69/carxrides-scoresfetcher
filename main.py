import praw
from praw.models import MoreComments
import pandas as pd
import datetime
import re

from reddit_utils import *
from date_utils import *
from rating_utils import *
from private_constants import *

print("Date/Time format is 'dd/mm/yy hh:mm:ss'. Make sure to enter start and end datetime in this format")
print("Example of December 1, 2023 at 12 AM (00:00): '01/12/23 00:00:00'")
print("Keep in mind that timezone CarXRides-ScoresFetcher counts from is UTC")
print() # space
start_date = to_timestamp(input("Enter start datetime, where CarXRides-ScoresFetcher will start searching from (without single(') or double(\") quotes): "))
end_date = to_timestamp(input("Enter end datetime, where CarXRides-ScoresFetcher will end searching (without single(') or double(\") quotes): "))

how_many_winners = 10

print("Creating and authenticating Reddit instance")
reddit = create_reddit()
print("Authenticating and retrieving data")
# checking is user is a mod
is_valid_user = False
for mod in get_moderators(get_subreddit(reddit)):
	if mod.name == redd_username:
		is_valid_user = True

if not is_valid_user:
	print(f"u/{redd_username} doesn't appear to be a r/{subreddit_name} moderator")
	print("The script access is limited only to moderators. Because reasons")
	print("Aborting")
	exit()

posts_dict, comments_dict = fetch_posts_and_comments_from_date_range(start_date, end_date, reddit)
posts_dict = pd.DataFrame(posts_dict)
comments_dict = pd.DataFrame(comments_dict)

indexes = []
for i in range(0, len(posts_dict)):
	indexes.append(i)
# sort and calculate winners

ratings_indexes = []
for i in indexes:
	ratings_indexes.append((posts_dict["rating"][i], i))
ratings_indexes.sort(key=lambda x: x[0])
ratings_indexes.reverse()

sorted_posts_dict = { "title": [], "id": [], "author": [], "is_mod": [], "rating": [], "datetime": [], "top_comment_text": [], "top_comment_author": [] }
for i in ratings_indexes:
	(rating, idx) = i
	# only rated ones are accepted
	if rating == -1:
		continue
	all_authors = posts_dict["author"]
	author = all_authors[idx]
	# no duplicate OPs
	if author in sorted_posts_dict["author"]:
		continue

	sorted_posts_dict["title"].append(posts_dict["title"][idx])
	sorted_posts_dict["id"].append(posts_dict["id"][idx])
	sorted_posts_dict["author"].append(posts_dict["author"][idx])
	sorted_posts_dict["is_mod"].append(posts_dict["is_mod"][idx])
	sorted_posts_dict["rating"].append(posts_dict["rating"][idx])
	sorted_posts_dict["datetime"].append(posts_dict["datetime"][idx])
	sorted_posts_dict["top_comment_text"].append(posts_dict["top_comment"][idx]["text"])
	sorted_posts_dict["top_comment_author"].append(posts_dict["top_comment"][idx]["author"])
sorted_posts_dict  = pd.DataFrame(sorted_posts_dict)

sub = get_subreddit(reddit)
place_templates = [
	sub.wiki["scores-retriever-first-place-template"].content_md,
	sub.wiki["scores-retriever-second-place-template"].content_md,
	sub.wiki["scores-retriever-third-place-template"].content_md
]
header_template = sub.wiki["scores-retriever-header-template"].content_md
footer_template = sub.wiki["scores-retriever-footer-template"].content_md
count_winners = min(min(len(place_templates), how_many_winners), len(sorted_posts_dict))
posts_count = len(posts_dict["title"])
text = header_template.replace("<posts-count>", f"{posts_count}") + "\n\n\n\n"
for i in range(0, count_winners):
	template = place_templates[i]
	user = sorted_posts_dict["author"][i].name
	date = sorted_posts_dict["datetime"][i]
	rating = sorted_posts_dict["rating"][i]
	rating_str = f"{rating}/10"
	modbadge = "**MOD**"
	if not sorted_posts_dict["is_mod"][i]:
		modbadge = ""
	post_title = sorted_posts_dict["title"][i]
	post_id = sorted_posts_dict["id"][i]
	post_url = f"https://reddit.com/r/{subreddit_name}/comments/{post_id}"
	top_comment_text = sorted_posts_dict["top_comment_text"][i]
	top_comment_author = sorted_posts_dict["top_comment_author"][i].name
	text += template.replace("<user>", user).replace("<date>", date).replace("<rating>", rating_str).replace("<modbadge>", modbadge).replace("<post-title>", post_title).replace("<post-url>", post_url).replace("<top-comment-text>", top_comment_text).replace("<top-comment-author>", top_comment_author) + "\n\n\n"

text += footer_template

print("Writing data")
text_file = open("post-text.md", "w", encoding="utf-8")
text_file.write(text)
text_file.close()
posts_dict.to_csv("posts.csv")
comments_dict.to_csv("comments.csv")
sorted_posts_dict.to_csv("winners.csv")
