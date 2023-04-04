import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

url =  os.environ.get("PLUGINBASEAI_API_URL")
pluginbaseai_api_key = os.environ.get('PLUGINBASEAI_API_KEY')
openai_api_key = os.environ.get('OPENAI_API_KEY')

# define headers
headers = {
    "Authorization": f"Bearer {pluginbaseai_api_key}",
    "Content-Type": "application/json",
}

# example method to list all available plugins by APi
def test_plugins_list():
    endpoint = url + "plugins/list"

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        plugin_list = response.json()
        print(plugin_list)
    else:
        print(f"Request failed with status code {response.status_code}.")

# example method to use a plugin
def test_plugins_use():
    endpoint = url + "generate"
    data = {
        "plugin": "Calculator",
        "text": "what's square root of 607",
        "llm": "openai",
        "llm_api_key": openai_api_key,
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)



test_plugins_list()

test_plugins_use()