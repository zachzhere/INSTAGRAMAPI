import requests
import json
import configparser

def readConfigFile():
    parser = configparser.ConfigParser()
    parser.read("Config.ini")
    return parser

def getCreds():
    parser = readConfigFile()
    accessToken = parser.get("API", "ACCESS_TOKEN")
    clientId = parser.get("API", "CLIENT_ID")
    clientSecret = parser.get("API", "CLIENT_SECRET")
    pageId = parser.get("API", "PAGE_ID")
    instagramaAccountId = parser.get("API", "INSTAGRAM_ACCOUNT_ID")

    creds = dict()
    creds[
        'access_token'] = accessToken

    creds['client_id'] = clientId
    creds['client_secret'] = clientSecret
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = pageId
    creds['instagram_account_id'] = instagramaAccountId
    return creds


def makeApiCall(url, endPointParams, type):
    if type == 'POST':
        data = requests.post(url, endPointParams)
    else:
        data = data = requests.get(url, endPointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endPointParams
    response['endpoint_params_pretty'] = json.dumps(endPointParams, indent=4)

    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    return response


def displayApiCallData(response):
    print("\nUrl:")
    print(response['url'])
    print("\nEndpoint Params:")
    print(response['endpoint_params_pretty'])
    print("\nResponse:")
    print(response['json_data_pretty'])
