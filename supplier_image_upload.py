#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
path = os.path.expanduser('~/supplier-data/images')

for image in os.listdir(path):
    if image.endswith('.jpeg'):
        with open(os.path.join(path, image), 'rb') as img:
            requests.post(url, files={'file': img})
