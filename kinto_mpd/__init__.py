"""kinto_mpd - A kinto plugin to start/stop playing a playlist in MPD"""

from kinto.core.events import ResourceChanged
from mpd import MPDClient

client = MPDClient()

__version__ = '0.1.0'
__author__ = 'Mathieu Agopian <mathieu@agopian.info>'
__all__ = []


def includeme(config):
    print("I am the ElasticSearch MPD plugin!")
    config.add_subscriber(on_resource_changed, ResourceChanged)


def on_resource_changed(event):
    resource_name = event.payload['resource_name']

    if resource_name != "record":
        return

    for change in event.impacted_records:
        print("Record changed:", change)
        record = change['new']
        if record.get('status', 'off') == 'on':
            client.clear()
            client.load(record['id'])
            client.play(0)
        else:
            client.stop()
