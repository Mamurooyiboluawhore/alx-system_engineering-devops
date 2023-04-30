#!/usr/bin/python3
""" a python script that uses REST API"""
import json
import requests
import sys

if __name__ == "__main__":
    """the url without the path"""
    url = "https://jsonplaceholder.typicode.com"
    userEP = "{}/users".format(url)
    user_name = requests.get(userEP).json()
    taskEP = "{}/todos".format(url)
    tasks = requests.get(taskEP).json()
    utask = {user.get("id"): [{"username": user.get('username'),
                               "task": task.get('title'),
                               "completed": task.get('completed')}
                              for task in tasks
                              if task.get("userId") == user.get("id")]
             for user in user_name}

    with open("todo_all_employees.json", 'w', encoding='utf-8') as file:
        json.dump(utask, file)
