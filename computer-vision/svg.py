import os
import random
import requests
from PIL import Image
import numpy as np
import cv2
import svgwrite

# Create output directory
os.makedirs("images", exist_ok=True)
os.makedirs("svgs", exist_ok=True)

# Simulated: Using a subset of public TinyImageNet image URLs
tiny_imagenet_urls = [
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01443537/n01443537_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01484850/n01484850_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01491361/n01491361_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01494475/n01494475_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01498041/n01498041_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01514668/n01514668_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01518878/n01518878_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01530575/n01530575_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01531178/n01531178_0.JPEG",
    "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/data/n01532829/n01532829_0.JPEG",
]

# Randomly select 10 URLs
selected_urls = random.sample(tiny_imagenet_urls, 10)

def raster_to_svg(image_path, svg_path):
    # Convert image to grayscale and threshold
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create SVG
    dwg = svgwrite.Drawing(svg_path, profile='tiny')
    for contour in contours:
        points = [(int(x), int(y)) for [[x, y]] in contour]
        if len(points) > 1:
            dwg.add(dwg.polyline(points, stroke='black', fill='none', stroke_width=1))
    dwg.save()

# Download and convert images
for i, url in enumerate(selected_urls):
    img_name = f"images/img_{i}.jpeg"
    svg_name = f"svgs/img_{i}.svg"
    
    # Download image
    response = requests.get(url)
    with open(img_name, 'wb') as f:
        f.write(response.content)

    # Convert to SVG
    raster_to_svg(img_name, svg_name)
    print(f"Saved SVG: {svg_name}")
