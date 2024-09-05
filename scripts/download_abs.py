import os
import requests
import zipfile

url_list = [
    "https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip",
    "https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_SA2_for_AUS_short-header.zip",
    "https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_WPP_SA2_for_AUS_short-header.zip"
]

target_directory = "data\\raw\\ABS_data"

# Create the ABS_data directory if it doesn't exist
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

for url in url_list:
    file_name = url.split("/")[-1]
    
    # Check if the file already exists
    if not os.path.exists(os.path.join(target_directory, file_name)):
        # Download the zip file
        response = requests.get(url)
        with open(os.path.join(target_directory, file_name), "wb") as file:
            file.write(response.content)

        # Extract the contents of the zip file
        with zipfile.ZipFile(os.path.join(target_directory, file_name), "r") as zip_ref:
            zip_ref.extractall(target_directory)

        print(f"File {file_name} downloaded and extracted.")
    else:
        print(f"File {file_name} already exists. Skipping download.")
