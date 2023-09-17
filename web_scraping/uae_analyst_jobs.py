import requests
import json

url = "https://www.talentmate.com/jobs"

payload = "job_title=analyst&job_type=&date_posted=0&city=&country=&min_salary=&max_salary=&currency=0"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_clck=1alpm8z|2|ff2|0|1354; _gid=GA1.2.1936394676.1694860764; _gat_UA-218045008-1=1; _ga_TE5PH2G3ZY=GS1.1.1694860763.1.1.1694860854.52.0.0; _ga=GA1.1.440475733.1694860764; _clsk=prngbg|1694860855112|3|1|p.clarity.ms/collect; XSRF-TOKEN=eyJpdiI6IkEyWTZlZnRoSUdSNEZPYXAwMUw1RGc9PSIsInZhbHVlIjoiZnVVc3dEZ3ViamVwTWo3USs0N2Y4SDZNR1czYi9oSzVJQ2t3eUZqb1ROcEd2eTd2ZkJZcWhaFmluS29rWlNuM0dDWHR2cnl5eW1nMzNMWW15ZVVxQk9jTGFYTGdMMEV5QjJwLytmcVQ0b1UyRWIybjlnVUpobXlhbFg3SHpOazgiLCJtYWMiOiIwYmVjMTBjMmU5ZTA4NTk5ZTM2OWEzYjUxYTMyYjczNTZkYjg4NmZhMTYyNjUwMTFmNjAyOTZkOTRkYWJmZTJmIiwidGFnIjoiIn0%3D; talentmate_session=yao0VPw4lA7F72IYA4j53k3yrHRiY8h5BomNidIQ; XSRF-TOKEN=eyJpdiI6IkhWdVk2cy9mcXQ4R01aQzhlN0RTaGc9PSIsInZhbHVlIjoiZlNwT3lmdnhSblVuWHhwaUVZODhNWVRlYi9BeXIySHhVL3JTb0lGTlBrMWRvblJ5RWlPS3VQOGVON1hYM01jTkFWSHpKMFNJNytwL1NRY2Z4dXY4ajgrRDBvdmJWTmNoNUJrdFF1b0dlWmwwR3JPMzRiU1pUUEVLWGxsQWxZeksiLCJtYWMiOiJmMDgyYjJhZDEzMGViZTEwZGJhY2FjYjU3MDhlMTg0NzIwZTA1MWY3YmVhNWNmNGEwNjU0MjU3OTdlMWY4YWJjIiwidGFnIjoiIn0%3D; talentmate_session=u50gVBXmBCs6xt6CV7CeVtD2qWkmpSlwquaC8TE8',
    'Origin': 'https://www.talentmate.com',
    'Referer': 'https://www.talentmate.com/jobs?search=data%20analyst,%20data%20scientist,%20business%20intelligence,%20business%20analyst,%20data%20engineer&country=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': 'zdsGpsxa7O7FDEOp29gTgsVHsRwmZZLgYkJSRVmU',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Check if the request was successful
if response.status_code == 200:
    # Specify the file path where you want to save the JSON data
    file_path = "uae_jobs.json"
    
    # Open the file in write mode and write the JSON data
    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    
    print(f"Data has been saved to {file_path}")
else:
    print(f"Request failed with status code: {response.status_code}")
