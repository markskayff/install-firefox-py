import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from tqdm import tqdm
import re
import tarfile
import os
from lib.funcs import killp_by_name
from lib import menu

############################################################
# The default extract location
############################################################
extract_location = "/usr/lib/"

############################################################
# Prompt for a Firefox version to install
############################################################
selected_version = menu.deal_menu()

print("Selected firefox version is: ", selected_version)

############################################################
# The firefox latest version download url
############################################################
url = (
  f"https://download.mozilla.org/"
  f"?product={selected_version}&os=linux64&lang=en-US"
)
print("Connecting with Mozilla ...")

try:
  # Download the file
  r = requests.get(url, stream=True)
  # ---------------------------------------------------
  # Raise an exception is status is not OK
  # ---------------------------------------------------
  r.raise_for_status()
except HTTPError: 
  print("Connection request responded with an error status. Try again later.")
  exit()
except Timeout:
  print("Connection has timed out.")
  exit()
except ConnectionError:
  print("An error ocurred while connecting with Mozilla's server")
  exit()
  
# Get the content disposition
cd = r.headers.get('Content-Disposition')
# Set a filename for the downloaded file
if cd != None :
  # Capture the filename in the Content Disposition
  m = re.findall('filename=(.+)', cd)
  filename = m[0]
else:
  filename = "firefox-latest.tar.bz2"

############################################################
# Prepare for tqdm progress bar
############################################################
# Calculate the download size
download_size = int(r.headers.get('content-length',0)) 
# Set a block size
block_size    = 102400 # 100 Kibibyte
# Create the tqdm "progress bar" object
pbar = tqdm(total=download_size, desc="Downloading",unit='iB', unit_scale=True)

# Download the stream and show progress
with open(filename, 'wb') as df:
  for c in r.iter_content(block_size):
    pbar.update(len(c))
    df.write(c)
# Close the progress bar
pbar.close()

# Force a filename. Maybe for dev or manual setup processing.
#filename="firefox-latest.tar.bz2"

############################################################
# Check file could was downloaded and available
############################################################
if os.path.exists(filename):
  print("Firefox downloaded ok!")
else:
  print("Firefox coud not be downloaded. Exiting")
  exit()

# Shutdown firefox
print("Shutting down firefox...")
############################################################
# Force shutdown Firefox if open.
# Some files might not be deleted/overwritten if a Firefox
# process is still open
############################################################
killp_by_name("firefox")

print("Installing Firefox ...")
print("From: " + filename)

try:
  ############################################################
  # Extract the files in the "path" location
  ############################################################
  with tarfile.open(filename, 'r:bz2') as tar:
    tar.extractall(path=extract_location, filter="tar")
except FileNotFoundError:
  print("Error. Seems could not find a file with name: " + filename)
except ReadError:
  print("There seems to be a problem with the tarball file")
except AbsolutePathError:
  print("Someone is doing something nasty. An absolute path seems to be defined for a member")
except PermissionError:
  print("You need to use 'sudo' for program execution or some permission block is ocurring.")
else:
  print("Cleaning downloaded file")
  ############################################################
  # Remove the downloaded file
  ############################################################
  os.remove(filename)
  print("Done")
