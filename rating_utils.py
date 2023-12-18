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

import re

def extract_rating(input_string):
    # Use regular expressions to find the rating pattern
    match = re.search(r'(\d+(?:[.,]\d+)?)\s*(?:out\s*of|outta|\/)\s*(\d+)', input_string)
    
    if match:
        rating = float(match.group(1))
        max_num = float(match.group(2))
        if max_num <= 1:
            # invalid rating
            return -1

        # Convert to "1 to 10 system"
        multiplier = 10 / max_num
        rating = rating * multiplier
        max_num = 10
        
        # Trim the rating to be between 1 and 10
        if rating < 1:
            rating = 1
        elif rating > max_num:
            rating = 10
        
        return rating
    else:
        # Return -1 if no valid rating is found
        return -1


# it should extract all valid ratings(those that arent -1, which means there's no rating) from given data
# then it calculates the average
# if average is 10.0, it looks at valid ratings count, if there's more than one, it returns e.g. 12 if there's 2
# otherwise just return the average
# if no valid ratings, return -1
def calculate_rating(ratings):
    valid_ratings = []
    for rating in ratings:
        if rating != -1:
            valid_ratings.append(rating)
    if len(valid_ratings) == 0:
        return -1
    else:
        ratings_avg = float(sum(valid_ratings)) / float(len(valid_ratings))
        total_rating = ratings_avg
        if total_rating == 10 and len(valid_ratings) > 1:
            total_rating = 10 + len(valid_ratings)
        return total_rating
