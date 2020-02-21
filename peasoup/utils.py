import os
from datetime import timedelta

from podgen import Podcast, Episode, Media
import mutagen

from . import config


def get_episodes(dir):

    def is_allowed(fname):
        return os.path.splitext(fname)[1] in config.ALLOWED_EXTENSIONS

    def get_file_info(fname):
        path = os.path.join(config.PODCASTS_DIRECTORY, fname)
        return {
            'duration': timedelta(seconds = mutagen.File(path).info.length),
            'size': os.stat(path).st_size
        }

    def episode_from_filename(filename):
        info = get_file_info(filename)
        return Episode(
            title = filename,
            media = Media(
                os.path.join(config.SERVER_BASEURL, 'episodes', filename),
                info.get('size'),
                None, # type
                info.get('duration')
            )
        )

    return [
        episode_from_filename(f)
        for f in os.listdir(dir)
        if is_allowed(f)
    ]


def generate_podcast_xml(podcasts):
    podcast = Podcast(
        name = config.PODCAST_NAME,
        description = config.PODCAST_DESCRIPTION,
        website = config.PODCAST_WEBSITE,
        explicit = config.PODCAST_CONTAINS_EXPLICIT_CONTENT,
        withhold_from_itunes = True
    )
    podcast.episodes = podcasts
    return podcast.rss_str()


def save_podcast_xml(xml):
    filepath = os.path.join(config.PODCASTS_DIRECTORY, "podcast.xml")
    with open(filepath, 'w') as f:
        f.write(xml)
