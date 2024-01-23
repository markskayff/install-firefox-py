menu = {
  1: { "title": "Firefox Latest", "name": "firefox-latest-ssl"},
  2: { "title": "Firefox Beta", "name": "firefox-beta-latest-ssl"},
  3: { "title": "Firefox Developer Edition", "name": "firefox-devedition-latest-ssl"},
  4: { "title": "Firefox Nightly", "name": "firefox-nightly-latest-ssl"},
  5: { "title": "Firefox Extended Support Release", "name": "firefox-esr-latest-ssl"},
  6: { "title": "Exit"}
}
def deal_menu():
  print("Select a Firefox version to download and install: \n")
  for key in menu.keys():
    print(key, ' - ', menu[key]["title"])

  option = int(input("Enter your Firefox: "))
  # Just exit on option 6
  if(option == 6):
    exit()
  # Wrong option passed
  if(option not in range(1,7)):
    exit("Wrong option, exiting")

  return menu[option]["name"]

