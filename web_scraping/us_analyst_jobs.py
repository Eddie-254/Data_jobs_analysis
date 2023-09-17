import requests
import json

url = "https://job-search-api1.p.rapidapi.com/v1/job-description-search"

querystring = {
    "q": "data analyst, data scientist, business intelligence, business analyst, data engineer",
    "page": "1",
    "country": "us"
}

headers = {
    "X-RapidAPI-Key": "04f28c11f5msh365fd3436cb8868p1e3a3cjsn9f7b5cdfcbab",
    "X-RapidAPI-Host": "job-search-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    # Specify the file path where you want to save the JSON data
    file_path = "us_jobs.json"
    
    # Open the file in write mode and write the JSON data
    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    
    print(f"Data has been saved to {file_path}")
else:
    print(f"Request failed with status code: {response.status_code}")
