# CarX Rides Scoresfetcher for r/CarXStreetRides

This is a script written by u/mrpaw69 in Python, with some help from u/4Nota2Robot0 and u/jaylins420.

# Purpose

This thing's purpose is to collect, calculate and summarize all the scores and ratings for Weekly Contest

# Ok... but who asked?
Previously all this was done entirely by hand, and was taking up to several hours, and was really exhausting. That, and results weren't always fair. Now, with this script, time we spend reduced to less than 10 minutes, which is AMAZING! Wake up, quickly launch the script, copy-paste generated text, and done!

# How does this thing work?

When I wrote the code, God and I knew how it worked. Now only God knows... (of course it's a joke, right?)

# Ok, but... how to install and use it?

1. Download the source code. Go to [releases](https://github.com/mrpaw69/carxrides-scoresfetcher/releases) and download the version you need. We recommend downloading the latest version

2. Install Python3. Read how to install it on [macOS](./PYMACINSTALL.md), [Windows](./PYWININSTALL.md) and [Linux](./PYLINUXINSTALL.md)

# Preparing to use

1. Create a reddit `script` application. How to create it: read [here](https://redditclient.readthedocs.io/en/latest/oauth/)(ignore the c++(or whatever that language is) code at the bottom). Make sure to type a long, unique user agent, otherwise it might not work

2. Open `private_constants.py`, fill out your created Reddit app data and your username. Make sure to put each data in quotes, or else code won't execute. Like this:

client_id="your-reddit-app-client-id"
>STRICT RECOMMENDATION: Please don't put your Reddit password in `redd_password` field! Preferred way is to enter the password each time script executes. While it's a bit incoveniient, it's more secure, since password is NOT stored on disk. It's intended to run just once a week, so it shouldn't be frustrating.

>Unless you're debugging the script on a throwaway account. When debugging/developing, usually you have to launch it many times in a short period of time because you're constantly modifying and testing the code, it can get really frustrating to enter password every f##king time

6. Now it should be ready to [use](#usage)

# Usage

1. Open Terminal/cmd.exe

2. `cd` into directory with script's source code

3. Run `python3 main.py`(or `python main.py` on Windows)

4. It should ask for start date and end date. Start date is date script starts searching posts with, end date is where script stops searching. Start date should always be earlier than end date

5. It will ask for your Reddit credentials, unless you typed in your password in `private_constants.py`(which is **unsafe**). Credentials are only passed to PRAW lib for authentication, which is open-source and available [here](https://github.com/praw-dev/praw)

6. When the script finishes, you should see 4 new files appearing in sources directory: `post-text.md`, `comments.csv`, `posts.csv`, and `winners.csv`. If you want a generated text, you need to view `post-text.md`. If your OS does not recognize `md` extension, simply change it to `txt` and open it(or type in `notepad post-text.md` on Windows while being in the same directory). Other files contain raw data of comments, posts, and winners

# Bug reports

Feel free to open an issue on [Issues page](https://github.com/mrpaw69/carxrides-scoresfetcher/issues)

# License

CarXRides-ScoresFetcher is licenced under Apache License 2.0.\
Unless required by applicable law or agreed to in writing, software
distributed under the [License](./LICENSE.md) is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the [License](./LICENSE.md) for the specific language governing permissions and
limitations under the [License](./LICENSE.md).\
Copyright 2023 mrpaw69

# Contributions

If you're also a coder and want to help me with this project, feel free to open a pull request