# Firefox Installer for Linux distros

Python script for installing/updating to the latest available Firefox version.

Firefox in Linux does not come with an **auto update** so it's hard to stay at the edge with a latest firefox version.

Just run this python script, select the Firefox flavor you want and you are good to go.

### Dependencies

Dependencies are defined in the `requirements.txt` file.

### Default install location

The script will attempt to install by default at: `/usr/lib/`

### Install

Clone this repo into your desired location

Install dependencies using:

`$ pip install -r requirements.txt`

### Usage

You will require **administrative** privileges to run this script, as it's installing under `/usr/lib`
by default.

`$ sudo python install.py`

You will be prompted for a Firefox flavor to install. Choose one and you are good to go.

Note: This version still does not create or prompt you to create a **desktop** entry. It does not either
prompt you for choosing a desired location for your setup.

