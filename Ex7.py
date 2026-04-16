import time
import requests

def get_response_time(url):
    start = time.time()
    requests.get(url, verify=False)
    end = time.time()
    return end - start

def get_status_code(url):
    timpi = []
    for i in range(repetari):
        timp = get_response_time(url)
        timpi.append(timp)
    medie = sum(timpi) / len(timpi)
    return (min(timpi), medie, max(timpi), )    