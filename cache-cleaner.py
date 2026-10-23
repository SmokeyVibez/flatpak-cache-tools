#!/usr/bin/env python3
# Version 2.0.1 - shows a Deleted popup after it deletes
# Version 2.0.0 - measures Brave + Stremio caches, asks first, deletes only on Yes
# Version 1.2.0 - loop measures Brave + Stremio caches, pops up the total
# Started as a copy of Fix Stremio Version 1.1.0 - became its own program at 2.0.0


import os
import shutil
import subprocess

apps = ["~/.var/app/com.brave.Browser/cache", "~/.var/app/com.stremio.Stremio/cache", "~/.var/app/com.stremio.Stremio/.stremio-server/stremio-cache"]


total = 0
for app in apps:
    path = os.path.expanduser(app)
    if os.path.exists(path):
      result = subprocess.run(["du", "-sb", path], capture_output=True, text=True)
      total = total + int(result.stdout.split()[0])
      print(result.stdout)
print("Total GB:", round(total / 1000000000, 2))
answer = subprocess.run(["kdialog", "--yesno", "Total cache: " + str(round(total / 1000000000, 2)) + " GB. Delete it?"])
if answer.returncode == 0:
    for app in apps:
        shutil.rmtree(os.path.expanduser(app), ignore_errors=True)
    subprocess.run(["kdialog", "--msgbox", "Deleted! :)"])
else:
    print("Nothing deleted.")
