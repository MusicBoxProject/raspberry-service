import json
import subprocess
import shlex
from pprint import pprint

with open('config.json') as f:
    config = json.load(f)

"""pprint(Tags['configTags'])
"""
for element in config['configTags']:
    tag = element['tag']['uuid'].upper()
    pathc = './newPlaylist.sh %s ' % (tag)
    subprocess.call(pathc,shell=True)
    for media in element['playlist']['media']:
        pathc = './addMedia.sh %s %s ' % (tag,media['uri'])
        subprocess.call(pathc,shell=True)        
