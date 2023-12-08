# Installing Python and required packages on macOS

## Keep in mind that script need `praw` and `pandas` Python packages to operate

1. Check if it's installed. Open Terminal.app, type in `python3` and hit Return(Enter). If it says "python3: command not found", move on to the next step. Otherwise skip straight to step 3

2. Preferred way to install Python 3 is using Homebrew package manager. It's like `apt` on Ubuntu/Debian, `pac` on Arch Linux, and `yum` on CentOS. Open Terminal.app(if it's not opened already), type in `brew install python3` and hit Return(Enter). If it says that `brew command is not found`, [install it](https://brew.sh) then repeat the step

3. After Python installation has finished, it's time to install required packages. Run `pip3 install praw pandas` in Terminal

Now that everything's installed, move on to [Preparing to Use](./README.md#preparing-to-use)