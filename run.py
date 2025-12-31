#!/usr/bin/env python3

import os
import requests

url = "http://localhost/fruits/"
path = os.path.expanduser('~/supplier-data/descriptions')

for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        lines = f.read().strip().split('\n')

        data = {
            "name": lines[0],
            "weight": int(lines[1].split()[0]),
            "description": lines[2],
            "image_name": file.replace('.txt', '.jpeg')
        }

        requests.post(url, json=data)
