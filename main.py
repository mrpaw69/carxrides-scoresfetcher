 # Copyright 2023 mrpaw69
 #
 #  Licensed under the Apache License, Version 2.0 (the "License");
 #  you may not use this file except in compliance with the License.
 #  You may obtain a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 #  Unless required by applicable law or agreed to in writing, software
 #  distributed under the License is distributed on an "AS IS" BASIS,
 #  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 #  See the License for the specific language governing permissions and
 #  limitations under the License.
 #
 
import pandas as pd
import datetime

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
print()
how_many_winners = input("How many winners do you want to save?: ")
if how_many_winners.isdigit():
	how_many_winners = int(how_many_winners)
else:
	print("The value you entered was not valid. Aborting")
	exit()

print("Creating and authenticating Reddit instance")
reddit = create_reddit()
print("Authenticating and retrieving data\n")
# checking is user is a mod
is_mod = False
for mod in get_moderators(get_subreddit(reddit)):
	if mod.name == redd_username:
		is_mod = True

if not is_mod:
	print(f"u/{redd_username} doesn't appear to be a r/{subreddit_name} moderator")
	print("Some things like muted users list is available only for moderators")
	print("Results may contain results that should not be included, like posts and comments from muted users")

posts_dict, comments_dict = fetch_posts_and_comments_from_date_range(start_date, end_date, reddit, is_mod)
posts_dict = pd.DataFrame(posts_dict)
comments_dict = pd.DataFrame(comments_dict)

print()
print("Calculating scores...")

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

print("Generating text...")

sub = get_subreddit(reddit)
place_templates = [
	sub.wiki["scores-retriever-first-place-template"].content_md,
	sub.wiki["scores-retriever-second-place-template"].content_md,
	sub.wiki["scores-retriever-third-place-template"].content_md
]
count_winners = min(how_many_winners, len(sorted_posts_dict))
if count_winners > 3:
	for i in range(3, count_winners):
		place_templates.append(sub.wiki["scores-retriever-anyplace-template"].content_md)

header_template = sub.wiki["scores-retriever-header-template"].content_md
footer_template = sub.wiki["scores-retriever-footer-template"].content_md
posts_count = len(posts_dict["title"])
text = header_template.replace("<posts-count>", f"{posts_count}") + "\n\n\n\n"
for i in range(0, count_winners):
	template = place_templates[i]
	place_num = str(i + 1)
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
	text += template.replace("<user>", user).replace("<date>", date).replace("<rating>", rating_str).replace("<modbadge>", modbadge).replace("<post-title>", post_title).replace("<post-url>", post_url).replace("<top-comment-text>", top_comment_text).replace("<top-comment-author>", top_comment_author).replace("<place>", place_num) + "\n\n\n"

text += footer_template

print("Writing data")

meta = { "totalPostsCount": posts_count, "validPostsCount": len(sorted_posts_dict), "inputWinnersCount": how_many_winners, "outputWinnersCount": count_winners, "highestRating": sorted_posts_dict["rating"][0] }
meta = pd.DataFrame(meta, index=[0])
text_file = open("post-text.md", "w", encoding="utf-8")
text_file.write(text)
text_file.close()
posts_dict.to_csv("posts.csv")
comments_dict.to_csv("comments.csv")
sorted_posts_dict.to_csv("winners.csv")
meta.to_csv("meta.csv")

print("Finished")
print("Generated text is written to `post-text.md`\nWinners CSV data written to `winners.csv`\nPosts CSV data written to `posts.csv`\nComments CSV data is written to `comments.csv`\nOther results data written to `meta.csv`")
