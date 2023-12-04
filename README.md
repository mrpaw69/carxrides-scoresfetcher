# CarX Rides Scoresfetcher for r/CarXStreetRides

This is a script written by u/mrpaw69 in Python, with some help from u/4Nota2Robot0 and u/jaylins420.

# Purpose

This thing's purpose is to collect, calculate and summarize all the scores and ratings for Weekly Contest

# Ok... but who asked?
Previously all this was done entirely by hand, and was taking up to several hours, and was really exhausting. Now, with this script, time we spend reduced to less that 10 minutes, which is AMAZING! Wake up, quickly launched the script, copy-pasted generated text, and done!

# How does this thing work?

When I wrote the code, God and I knew how it worked. Now only God knows... (of course it's a joke, or is it?)

# Ok, but... how to install and use it?

1. You gotta create a reddit `script` application. How to create it: read [here](https://redditclient.readthedocs.io/en/latest/oauth/)(ignore the c++(or whatever that language is) code at the bottom). Make sure to type a long, unique user agent, or else it might not work

2. You gotta install Python 3
>Don't know if Python is installed on your machine? Open Terminal/cmd.exe, type `python3` and hit Enter. If it says something like "command not found", "command not recognized", etc., Python 3 is not installed. Otherwise, skip this step

## Mac

There are 3 ways:

### Using Homebrew

Open the Terminal, type `brew install python` and hit Return(or Enter, whatever you call it)
>Command `brew` not found? Go to https://brew.sh and follow the instructions! Or use another less preferred ways to install Python

### Going to python.org and downloading an installer (least preferred way)

Go to https://python.org, download an installed for Mac. When it downloads, open it to install
> MAKE SURE you downloaded version with correct architecture. For Apple Silicon architecture is arm64, for Intel architecture is x64/x86_64. If you don't know which Mac do you have, go to  -> About This Mac and look at Processor. If you see Intel, you have an Intel Mac, if you see M1, M3 Pro, etc. you're on Apple Silicon

### Xcode

If you are a software developer and have it installed(you probably have, it's impossible to write whole apps for Apple devices without Xcode), python 3 should be already available, as it comes pre-installed with Xcode. **Don't** go and install it right away just for Python, use one of the methods above

## Windows

This script hasn't been tested on Windows yet. Go to https://python.org and download an installer for Windows and your processor architecture(I hope yk how to get correct architecture on Windows because I don't)

## Linux

This script hasn't been tested on Linux yet. Go to https://python.org and download an installed for your Linux distro and processor architecture

After you're finished installing

3. Download the source code. Click on Code -> Download ZIP on this GitHub page. After it downloaded, extract the downloaded ZIP

4. Install required packages.

To do that, execute `bootstrap` script

Windows: double-click `bootstrap.bat` and it should work(hasn't been tested yet)

Linux/Unix/macOS: Open Terminal, `cd` into extracted folder, and execute `./bootstrap.sh`(`./` plays important role here). If it says something like `Permission denied` or `Operation not permitted`, run `chmod +x bootstrap.sh` and try again

If bootstrap fails with something like `pip3 not available`, `pip3: command not found`, try manually running `pip3 install pandas praw` or `pip install pandas praw`. If this fails, it might mean you didn't install Python 3 correctly or not installed it at all

5. Open `private_constants.py`(will be available soon) and fill out your created Reddit app data. Make sure to put each data in quotes, or else code won't execute. Like this:

client_id="your-reddit-app-client-id"

6. Now it should be ready

# Usage

1. Open Terminal/cmd.exe

2. `cd` into directory with script's source code

3. Run `python3 main.py`

4. (TO BE IMPLEMENTED) It should ask for start date and end date. Start date is date script starts searching posts with, end date is where script stops searching. Start date should always be earlier than end date

5. It will ask for your Reddit credentials. It won't work without them. DW, they're only passed to PRAW lib for authentication, which is open-source and available [here](https://github.com/praw-dev/praw)

6. When the script finishes, you should see 4 new files appearing in sources directory: `post-text.md`, `comments.csv`, `posts.csv`, and `winners.csv`. If you want a generated text, you need to view `post-text.md`. If your OS does not recognize `md` extension, simply change it to `txt` and open it. Other files contain raw data of comments, posts, and winners

# License

CarXRides-ScoresFetcher is licenced under MIT license.

# Contributions

If you know how to code and want to help me with this code(which I don't plan to maintain in the future, I'm doing another great project, can't tell what it is tho, it's too early), feel free to contribute by making a pull request