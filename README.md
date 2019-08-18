# parse-bookmarks

> Parse Google bookmarks file to find a list of bookmarks that may no longer be usable.

## Overview
In an effort to clean up my Google bookmarks, I wanted a method for determining
which bookmarks may no longer exist. The idea is to export a Google bookmarks
.html file, use a python script to parse and connect to each bookmark in the file,
and finally create a text file with a list of bookmarks that returned a 404 or
connection error.

## Usage
* Export Google bookmarks
* Move bookmarks file into same directory as the run.py file
* Update settings.py file
* Execute run.py file
* Open output file
* Open Chrome bookmarks manager and delete any bookmarks that are in the output file

## Notes
* Redirects are not taken into consideration, only 404 responses and connection errors
* Ensure bookmark no longer works before deleting
