#!/usr/bin/python3
""" a python script that uses REST API"""
import csv
import requests
import sys

if __name__ == "__main__":
    """the url without the path"""
    url = "https://jsonplaceholder.typicode.com"
    id_ = int(sys.argv[1])
    userEP = "{}/users/{}".format(url, id_)
    user_ID = requests.get(userEP).json().get('username')
    taskEP = "{}/todos".format(url)
    tasks = requests.get(taskEP).json()
    utask = [[id_, user_ID, task.get("completed"),
             task.get("title")]
             for task in tasks if id_ == task.get("userId")]

    # opening with csv
    with open("{}.csv".format(id_), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(utask)
