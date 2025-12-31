# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url',
    default='https://annarodrigue-3030.' +
    'theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai')
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default='https://sentianalyzer.24kl2ns2x1ex.' + 
    'us-south.codeengine.appdomain.cloud/')


def get_request(endpoint, **kwargs):
    # Add code for get requests to back end
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    request_url = backend_url+endpoint+"?"+params
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception:
        # If any error occurs
        print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    # Add code for retrieving sentiments
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    # Add code for posting review
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception:
        print("Network exception occurred")
