from defines import getCreds, makeApiCall


def getUserPager(params):
    endPointParams = dict()
    endPointParams['access_token'] = params['access_token']
    url = params['endpoint_base'] + 'me/accounts'

    return makeApiCall(url, endPointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = getUserPager(params)

print("\n---- FACEBOOK PAGE INFO ----\n") # section heading
print("Page Name:") # label
print(response['json_data']['data'][0]['name']) # display name
print("\nPage Category:")# label
print(response['json_data']['data'][0]['category']) # display category
print ("\nPage Id:") # label
print (response['json_data']['data'][0]['id']) # display id