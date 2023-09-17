import requests
import json

url = "https://www.talentmate.com/jobs"

payload = "job_title=data&job_type=&date_posted=0&city=&country=&min_salary=&max_salary=&currency=0"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_clck=1alpm8z|2|ff2|0|1354; _gid=GA1.2.1936394676.1694860764; _gat_UA-218045008-1=1; _ga_TE5PH2G3ZY=GS1.1.1694860763.1.1.1694861534.55.0.0; _ga=GA1.1.440475733.1694860764; _clsk=prngbg|1694861535226|5|1|p.clarity.ms/collect; XSRF-TOKEN=eyJpdiI6Inh4MzN2VlFMd1JLc3hHSjF6V0wzZ0E9PSIsInZhbHVlIjoidlk2czBON2JQVTN1bW01aVIzMjA5ckFnOGRkMGpYVll2SitCbGxnK1UwQkZzTUpHU3VndW9TbFZ1cG1BOFJaWHI0ODA2aHR5dklrK2tvNGlRcy81eVJMdS92aUNDVy9KT09jVENncTczWTg2c01LeFRFVDJRMXowUlRKb3hCcEEiLCJtYWMiOiIyZmQ1NzQwMDUxZmVmNDYxYzIyOTgxYWMxYjM3MDg2NTFiNWU1MTJlZGRlYjZhYmFlYzY5MTcxMTk1N2Y5YmM5IiwidGFnIjoiIn0%3D; talentmate_session=mZLA9btvgjikPYFVY0s0c5iQ7e9Gdz7GertayLfd; XSRF-TOKEN=eyJpdiI6IkU4UmdoVU5TL1kwWGZtbnBxVFJORmc9PSIsInZhbHVlIjoiRUNqTFd3K05kZ3ZTcHZ4UHJTSjhHZy85M01nSDNjWlo2emZQVkJMZWNKMUFadEJ0WjMwRVg0ZEtjZDY3RjhSc2lBZm1FUnd5UWJjUFFqWElocENDVTdFYUREMzNxam54MGRKSHlaeXAiLCJtYWMiOiIwYmVjMTBjMmU5ZTA4NTk5ZTM2OWEzYjUxYTMyYjczNTZkYjg4NmZhMTYyNjUwMTFmNjAyOTZkOTRkYWJmZTJmIiwidGFnIjoiIn0%3D; talentmate_session=hqv19nZmR71wEf8tC4GhiuVFBCZ5q7RBdd4b7vRV',
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
    file_path = "uae_data_jobs.json"
    
    # Open the file in write mode and write the JSON data
    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)
    
    print(f"Data has been saved to {file_path}")
else:
    print(f"Request failed with status code: {response.status_code}")
