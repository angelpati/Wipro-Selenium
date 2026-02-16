import requests

try:
    data={
        "name":"Angel"
    }

    # make a get request to a api end pint
    response = requests.post("https://jsonplaceholder.typicode.com/users",json=data)
    print(response)

    # check if type status code is 200
    if response.status_code == 201:
        print("Status code is 201 k")
        # parse the json file
        users = response.json()
        print(users)


    else:
        print(f"Error: Received status code{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")