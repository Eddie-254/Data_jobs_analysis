import requests
import json

url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query": "data analyst in us",
    "page": "10",
    "num_pages": "20",
    "date_posted": "all",
    "job_titles": "data analyst, data scientist, business intelligence, business analyst, data engineer"
}

headers = {
    "X-RapidAPI-Key": "04f28c11f5msh365fd3436cb8868p1e3a3cjsn9f7b5cdfcbab",
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    # Specify the file path where you want to save the JSON data
    file_path = "search_results.json"
    
    # Open the file in write mode and write the JSON data
    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    
    print(f"Data has been saved to {file_path}")
else:
    print(f"Request failed with status code: {response.status_code}")
