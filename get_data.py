# ...existing code...
import requests

# Direct CSV (not a zip file)
url = "https://www.research-collection.ethz.ch/bitstreams/42a2f58b-d925-4352-908f-91db854466a1/download"
csv_name = "data_raw.csv"

# Download and save as CSV
response = requests.get(url, allow_redirects=True)
response.raise_for_status()

with open(csv_name, "wb") as f:
    f.write(response.content)
# ...existing code...