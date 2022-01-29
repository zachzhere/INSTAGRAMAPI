from defines import getCreds, makeApiCall


def getUserPager(params):
    endPointParams = dict() # parameter to send to the endpoint
    endPointParams['access_token'] = params['access_token'] # tell facebook we want to exchange token
    url = params['endpoint_base'] + 'me/accounts'  # endpoint url

    return makeApiCall(url, endPointParams, params['debug'])


params = getCreds() # get creds
params['debug'] = 'yes' # set debug
response = getUserPager(params)  # get debug info

print("\n---- FACEBOOK PAGE INFO ----\n") # section heading
print("Page Name:") # label
print(response['json_data']['data'][0]['name']) # display name
print("\nPage Category:")# label
print(response['json_data']['data'][0]['category']) # display category
print ("\nPage Id:") # label
print (response['json_data']['data'][0]['id']) # display id