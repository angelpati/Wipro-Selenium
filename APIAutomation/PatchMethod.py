import requests


try:
    data={
        "name": "Apple MacBook Pro 16"
    }
    #make a post request to a api end pint
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819c5368bb019c554adfaf0305", json=data)
    print(response)

    #check if type status code is 200
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else: print(f"Error: Received status code{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")