# About this script
Some applications generate files that use a random string as a name. e.g this happens with the images downloaded through Viber. If you want to keep these images, it is convenient to have a more meaningful name (that denotes a chronological order too). This is the reason why this script exists.

The script takes as input a folder and copies all the contained files, while renaming them to have the date in their name in this format `YYYYMMDD_hhmmss.<extension>` (eg: 20220807_191404.jpg).


The script takes care not to delete or overwrite anything by mistake. For this reason:
- the files are actually copied to a new folder, not renamed
- if two or more files happen to have the same timestamp, a number is appended to the name in order to make it unique.
