#!/usr/bin/env python3

from PIL import Image
import os

path = os.path.expanduser('~/supplier-data/images')

for image in os.listdir(path):
    if image.endswith('.tiff'):
        img = Image.open(os.path.join(path, image))
        img = img.convert('RGB')
        img = img.resize((600, 400))
        new_name = image.replace('.tiff', '.jpeg')
        img.save(os.path.join(path, new_name), 'JPEG')
