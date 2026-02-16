#Write code to check if response status code is not 200 and raise an exception.
import requests
try:


    # make a get request to a api end pint
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    response.raise_for_status()
    print("Status code is 200 k")


    users = response.json()
    print(users)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

