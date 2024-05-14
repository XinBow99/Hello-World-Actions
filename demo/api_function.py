import requests


# Simple test function on github ACTIONS
def curl_github():
    response = requests.get("https://api.github.com")
    status_code = response.status_code
    
    return status_code

def curl_github_bad():
    return 404
    