#!/usr/bin/python3
""" a python script that uses REST API"""
import json
import requests
import sys

if __name__ == "__main__":
    """the url without the path"""
    url = "https://jsonplaceholder.typicode.com"
    id_ = int(sys.argv[1])
    userEP = "{}/users/{}".format(url, id_)
    user_name = requests.get(userEP).json().get('username')
    taskEP = "{}/todos".format(url)
    tasks = requests.get(taskEP).json()
    utask = {id_: [{"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_name}
                   for task in tasks if task.get("userId") == id_]}

    with open("{}.json".format(id_), 'w', encoding='utf-8') as file:
        json.dump(utask, file)

    print(utask)
