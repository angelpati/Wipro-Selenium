#Implement timeout handling (2 seconds) and catch Timeout exception.


import requests

try:

    # make a get request to a api end pint
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
    print(response)

    # check if type status code is 200
    if response.status_code == 200:
        print("Status code is 200 k")
        # parse the json file
        users = response.json()
        for user in users:
            print(user)

except requests.exceptions.Timeout:
    print("Request timed out after 2 seconds.")

# Catch HTTP errors
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")