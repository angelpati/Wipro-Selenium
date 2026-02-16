import requests


try:
    data={
        "category": "Platform",
        "name": "Angel",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }
    #make a post request to a api end pint
    response = requests.post("https://videogamedb.uk:443/api/v2/videogame", json=data)
    print(response)

    #check if type status code is 200
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        #text of the response file
        print(response.text)
        #content of the response
        print(response.content)
        #status code of the response
        print(response.status_code)
        #headers
        print(response.headers)
        #history
        print(response.history)
        #url
        print(response.url)
        #fetch the single header
        content_type= response.headers.get('Content-Type')
        print(data)
    else: print(f"Error: Received status code{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")