import requests



try:

    # make a get request to a api end pint
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)

    # check if type status code is 200
    if response.status_code == 200:
        print("Status code is 200 k")
        # parse the json file
        users = response.json()
        for user in users:
            print(user["username"].upper())


except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")