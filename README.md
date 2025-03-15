# GitHub Actions Demo: Automating a Python Script

### ⚠️ **GitHub Actions Status: Disabled**
This repository’s GitHub Actions workflow is currently **disabled**. To view or re-enable it, follow these steps:

1. **Go to the GitHub repository** in your browser.
2. **Click on the "Actions" tab** (at the top of the repo).
3. If you see a message saying **“This workflow has been disabled”**, click **"Enable workflow"**.
4. Once enabled, the workflow will run according to its schedule or when triggered manually.

You can also manually trigger a workflow run by clicking **"Run workflow"** in the Actions tab. 🚀



## 📌 Overview
This project is a **simple GitHub Actions demo** that runs a Python script (`main.py`) at regular intervals. The script fetches job listings from an API and logs the results into `log.txt`. GitHub Actions automates this process, ensuring the script runs without manual intervention.

## 🚀 What Happens in This Project?
1. **GitHub Actions** automatically runs `main.py` every minute.
2. The script **fetches job listings** from an API (`arbeitnow.com`).
3. Extracted job details are **logged into `log.txt`**.
4. GitHub Actions **commits and pushes `log.txt`** back to the repository.

## 🔧 Understanding the GitHub Actions Workflow
The workflow is defined in `.github/workflows/actions.yml`.

### **1️⃣ When Does It Run?**
- **Every minute** (`cron: '1 * * * *'`).
- **Manually**, from the GitHub Actions tab (`workflow_dispatch`).

### **2️⃣ What Are the Steps?**
- **Step 1**: Download repository files.
- **Step 2**: Set up Python (`3.9`).
- **Step 3**: Install dependencies (`pip install -r requirements.txt`).
- **Step 4**: Run `main.py`.
- **Step 5**: If `log.txt` changes, **commit and push it**.

## 📝 Breakdown of `main.py`
This script fetches job listings and logs the results.

### **How It Works**:
1. **Fetches API Data**: Requests job listings from `https://www.arbeitnow.com/api/job-board-api`.
2. **Parses Jobs**: Extracts company name and job title.
3. **Logs to File**: Saves job details in `log.txt`.
4. **Handles Errors**: If the request fails, logs an error message.

### **Code Highlights**:
```python
import os
import requests

def simple_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{message}\n")

if __name__ == "__main__":
    try:
        r = requests.get('https://www.arbeitnow.com/api/job-board-api')
        if r.status_code == 200:
            jobs = r.json()["data"]
            for job in jobs:
                simple_log(f"Company: {job['company_name']}, Position: {job['title']}")
        else:
            simple_log(f"Failed to retrieve job data. Status code: {r.status_code}")
    except Exception as e:
        simple_log(f"An error occurred: {str(e)}")
```

## 🔄 How to Test Locally
If you want to run the script manually, follow these steps:

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Script
```bash
python main.py
```

### 3️⃣ Check the Output
```bash
cat log.txt
```

## 🔮 Future Enhancements
- **Improve logging format** (e.g., timestamps, structured output).
- **Use environment variables** for API URLs.
- **Enhance GitHub Actions** (e.g., send notifications on failures).

This README serves as a **learning guide** to understand how GitHub Actions automates a simple Python workflow. 🚀


