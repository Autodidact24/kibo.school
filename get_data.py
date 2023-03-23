import pandas as pd

import json
import requests


url = "https://global-warming.org/api/co2-api"

# TODO: Make the request to the API and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the JSON data to a Python dictionary
    data = response.json()

    # TODO: Convert the dictionary to a Pandas dataframe
    df = pd.DataFrame.from_dict(data["co2"])
    print(df.head())
else:
    print("Request failed")


#TODO: Write the output into a CSV
df.to_csv("co2_trends.csv", index=False)
