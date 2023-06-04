import hashlib
import json
import os
import urllib.request
import tqdm

# Load the JSON file
with open('credits.rawiconurl.json', 'r', encoding="utf-8") as f:
    credits_ = json.load(f)

# Download the images and update the JSON file with relative paths
for contributor in tqdm.tqdm(credits_['contributors'], unit="users"):
    icon_url = contributor['icon']
    filename = hashlib.sha1(icon_url.encode("utf-8")).hexdigest() + ".jpg"
    file_path = os.path.join('credits/images', filename)
    relative_path = "static/credits/images/" + filename
    urllib.request.urlretrieve(icon_url, file_path)
    contributor['icon'] = relative_path

# Save the updated JSON file
with open('static/credits/credits.json', 'w', encoding="utf-8") as f:
    json.dump(credits_, f)

# Print the updated JSON file
print(json.dumps(credits_, indent=2))