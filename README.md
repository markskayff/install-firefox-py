# Firefox Installer for Linux distros

![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmarkskayff%2Finstall-firefox-py%2Fmain%2Finstall-firefox.toml&query=%24.min_python_version&suffix=%2B&style=flat&label=Min%20Python)


Python script for installing/updating to the latest available Firefox version.

In some Linux distros Firefox is not **auto updating** or package managers do have an old and not even close to the latest version/package available.
It's hard to stay at the edge with the latest firefox available out there then.

Just run this python script, select the Firefox flavor you want and you are good to go.

### Dependencies

Dependencies are defined in the `requirements.txt` file.

### Warning

It would be a good idea to identify and even backup your **"main/active"** Firefox profile or allthe  profiles you are actively using in Firefox.

To locate your profile path you can type `about:profiles` in your Firefox tab. You will find your **profiles path locations**
where you can create a backup.

You can always run Firefox with the profile manager prompt using:

`$ firefox --ProfileManager`

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

