#!/usr/bin/python3
""" A python script that fetches info about a given employee using an api
and exports it in csv format
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # To get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    # To get info from  the api
    response = requests.get(user_url)

    # To pull data from api
    data = response.text

    # To parse the data into a JSON format
    data = json.loads(data)

    # To extract user data, in this case, username of employee
    user_name = data[0].get('username')
    # print("id is: {}".format(user_id))
    # print("name is: {}".format(user_name))

    # To get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    # To get info from api
    response = requests.get(tasks_url)

    # To pull the data from an api
    tasks = response.text

    # To parse the data into JSON format
    tasks = json.loads(tasks)

    # To build the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # You can also use the get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
