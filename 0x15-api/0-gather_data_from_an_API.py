#!/usr/bin/python3
""" a python script that uses REST API"""

import requests
import sys

if __name__ == "__main__":
    """the url without the path"""
    url = "https://jsonplaceholder.typicode.com"
    id_ = int(sys.argv[1])
    userEP = "{}/users/{}".format(url, id_)
    user_ID = requests.get(userEP).json().get('name')
    taskEP = "{}/todos".format(url)
    tasks = requests.get(taskEP).json()
    utask = [task for task in tasks if task.get("userId") == id_]
    ctask = [task for task in utask if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(user_ID, len(ctask), len(utask)))

    for task in ctask:
        print("\t {}".format(task.get('title')))
