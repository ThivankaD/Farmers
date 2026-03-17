import os
import requests
import zipfile

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048
# Direct S3 endpoint (the previous URL now returns XML)
url = "https://md-datasets-cache-zipfiles-prod.s3.amazonaws.com/yshdbyj6zy-1.zip"
zip_name = "data.zip"

# Download the zipped dataset, following redirects (HTTP 301, etc.)
with requests.get(url, stream=True, allow_redirects=True) as r:
    r.raise_for_status()
    with open(zip_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
    zip_ref.filelist[0].filename = "data_raw.csv"
    zip_ref.extract(zip_ref.filelist[0])

os.remove(zip_name)

