# Flatpak Cache Tools (KDE)

Two small Python tools I built while learning to code. Both were made for a real problem on my own machine: Flatpak app caches piling up, and one corrupted cache that kept breaking Stremio.

**Who did what — honestly:**

- **The programs: mine.** I typed every line by hand and made every decision, with an AI tutor — Io, on Meta's Muse platform — guiding me step by step while I learned.
- **This README: drafted by Io** at my request, so the explanation would be written clearly. I read it and approved it.

## The tools

### Fix Stremio — `fix-stremio.py` (v1.1.0)

One click clears Stremio's special streaming cache folder and pops up a confirmation.

- Deletes exactly this folder, nothing else: `~/.var/app/com.stremio.Stremio/.stremio-server/stremio-cache`
- Why: a corrupted cache made my Stremio black-screen and freeze my whole PC. Clearing this folder fixed it.
- **Close Stremio before running it.**

### Cache Cleaner — `cache-cleaner.py` (v2.0.1)

The bigger sibling. It measures the caches, tells you the total, asks first, and only deletes if you say Yes.

- Measures: Brave cache, Stremio cache, and Stremio's special cache (listed above)
- Shows the total size in a popup and asks before deleting anything
- Deletes **only** those cache folders — never settings, never your data
- If you only have one of the apps, the missing ones are skipped silently
- After deleting, it confirms with a popup
- Coming in 2.1.0: a checklist box showing each app's size, so you can pick which caches to delete

## Requirements

- Linux with KDE (the popups use `kdialog`)
- Python 3
- Brave and/or Stremio installed as Flatpaks

## How to use

Right now these install by hand (steps below). A ready-to-run single-file build is coming in a later release — download it, allow launching, and it just runs. Stay tuned.

1. Download the `.py` file for the tool you want
2. Make it runnable: `chmod +x cache-cleaner.py`
3. Run it from a terminal — or use the included `.desktop` file to give it an icon: put the `.py` file in your home folder (the launcher looks for it there), put the `.desktop` file on your Desktop or in `~/.local/share/applications/` for your app menu, then right-click the icon → Allow Launching

## Notes

- These tools only ever touch the cache folders named above. Caches are safe to delete: the apps rebuild them on their own.
- I'm a beginner and these are my first programs. They work on my machine (Bazzite / KDE). Read the code before you run it — it's short, and it's all right there.
- More apps will be added to the cleaner over time — and anyone is free to add to it. Forks and pull requests welcome.
- Don't know how useful these actually are but they are my first code written by me. :)
