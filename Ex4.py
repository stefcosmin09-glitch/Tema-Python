import requests

with open("urls.txt", "r") as f:
    for line in f:
        url = line.strip()
        response = requests.get(url)
        if 200 <= response.status_code <= 299:
            with open("success.txt", "a") as success_file:
                success_file.write(f"{url}\n")
        else:
            with open("error.txt", "a") as error_file:
                error_file.write(f"{url}\n")

