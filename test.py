"""
This script sends an image to the Flask server for processing and times the request.
"""

import time
import requests


# your localhost url. If running on port 5000
URL = "http://localhost:5000/process"

# Path to image file
#filess = {"img": open("img.jpg", "rb")}
with open("img.jpg", "rb") as img:
    filess = {"img": img}
starttime = time.time()
# Send a POST request with the image and a timeout of 5 seconds
results = requests.post(URL, files=filess, timeout=5)
# Print the time taken and the server's response
print("time taken:", time.time() - starttime)
print(results.text)
