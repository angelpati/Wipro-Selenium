
import requests

try:
    url = "https://jsonplaceholder.typicode.com/posts"

    # Query parameters
    params = {
        "userId": 2
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        posts = response.json()
        print(f"Number of posts returned: {len(posts)}")
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
