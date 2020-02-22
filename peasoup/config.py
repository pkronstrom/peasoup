
# Change this to a directory where the podcast files lie.
# The server currently only supports for flat directories
PODCASTS_DIRECTORY = "/path/to/samba/shared/podcasts/dir"

# The baseurl should be something that is accessible from
# the outside world (or at least from local network) in
# order to use with your podcast client.
# Probably something like http://my-ddns-name.dy.fi:9999
SERVER_BASEURL = "http://localhost:9999"

# Current list of allowed extensions.
# The rest of the filetypes are ignored.
ALLOWED_EXTENSIONS = [".mp3", ".m4a", ".m4b", "aac", ".ogg", ".wma", ".flac", ".alac"]

# Podcast specific info that is
# rendered to the XML file
PODCAST_NAME = "Peasoup Podcast"
PODCAST_DESCRIPTION = (
    "This is my peasoup.\n"
    "Probably needs some mustard and onion."
)
# This might need to be something accessible depending on
# the podcast client
PODCAST_WEBSITE = "http://www.my-podcast-website.com"
PODCAST_CONTAINS_EXPLICIT_CONTENT = False
