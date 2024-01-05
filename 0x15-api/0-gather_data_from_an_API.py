#!/usr/bin/python3
"""A python script that fetches info about a given employee's ID using an api"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # To get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    # To get info from the api
    response = requests.get(user_url)

    # To pull data from the api
    data = response.text

    # To parse the data into a JSON format
    data = json.loads(data)

    # To extract the user data, in this case, name of employee
    name = data[0].get('name')

    # print("id is: {}".format(user_id))
    # print("name is: {}".format(name))

    # To get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    # To get info from the api
    response = requests.get(tasks_url)

    # To pull data from the api
    tasks = response.text

    # To parse the data into a JSON format
    tasks = json.loads(tasks)

    # To initialize the completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    # To initialize an empty list for completed tasks
    completed_tasks =[]

    # To loop through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            # To print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # To print the output in the required format, run the code below
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
