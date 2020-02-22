import sys
from flask import Flask, Response, send_from_directory
from peasoup import utils, config

app = Flask(__name__)


@app.route('/')
def get_podcast_xml():
    podcasts = utils.get_episodes(config.PODCASTS_DIRECTORY)
    xml = utils.generate_podcast_xml(podcasts)
    return Response(
        response = xml,
        status=200,
        mimetype="application/xml")


@app.route('/episodes/<slug>')
def get_podcast_episode(slug):
    filename = utils.from_slug(slug)
    return send_from_directory(
        config.PODCASTS_DIRECTORY, filename)


if __name__ == '__main__':
    # slugify the dir in case the server has been started
    # and we use a cache xml
    utils.slugify_podcasts_dir()
    app.run(host="0.0.0.0", port=9999)
