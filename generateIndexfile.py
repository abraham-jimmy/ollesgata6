#!/usr/bin/env python3
import os

# folder with images
image_dir = "."
# output file
html_file = "index.html"

# list image files
images = [f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))]

with open(html_file, "w") as f:
    f.write("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>yo bror</title>
  <style>
    body {
      background-color: #000;
      color: #fff;
      font-family: sans-serif;
      text-align: center;
    }
    img {
      max-width: 90%;
      margin: 20px 0;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
  </style>
</head>
<body>
  <h1>Olles Gata 6</h1>
""")

    for img in images:
        f.write(f"  <div><img src='{img}' alt='{img}'></div>\n")

    f.write("""
  <i>prutt</i>
</body>
</html>
""")

print(f"✅ Created {html_file} with {len(images)} images.")

