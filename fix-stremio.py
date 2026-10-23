#!/usr/bin/env python3
# Version 1.1.0
import os
import shutil
import subprocess

cache = os.path.expanduser("~/.var/app/com.stremio.Stremio/.stremio-server/stremio-cache")


if os.path.exists(cache):
   shutil.rmtree(cache)
   message = "Cache deleted. All clear OG."
else:
  message = "Cache folder not there."

subprocess.run(["kdialog", "--msgbox", message])
# nukes stremio cache when it starts acting up
