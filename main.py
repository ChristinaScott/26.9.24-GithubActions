import os
import requests

def simple_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")


if __name__ == "__main__":
    try:
        r = requests.get('https://www.arbeitnow.com/api/job-board-api')
        if r.status_code == 200:
            api_content = r.json()
            jobs = api_content["data"]
            for job in jobs:
                simple_log(f"Company {job['company_name']}\nPosition: {job['title']}")
        else:
            simple_log(f"Failed to retrieve job data. Status code: {r.status_code}")
    except Exception as e:
        simple_log(f"An error occurred: {str(e)}")