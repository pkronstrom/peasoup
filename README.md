# What on earth?

This script screens a directory for audio files,
generates an xml file read by podcast clients and
serves the podcasts on a given url.

Not really tested, just a demoish thingy.

# Instructions

## Test the app

1. `poetry install`
2. modify the peasoup/config.py to your liking
3. create a directory for podcasts and add some files to it
4. `poetry run python app.py`

Access the podcast xml at <my-server-url>:9999
