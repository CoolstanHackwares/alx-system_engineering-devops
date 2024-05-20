#!/usr/bin/python3
"""
Fetches data from a REST API for an employee ID and exports it to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/{}'.format(employee_id)
    todos_url = base_url + 'todos?userId={}'.format(employee_id)

    try:
        user_data = requests.get(user_url).json()
        todos_data = requests.get(todos_url).json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    output = {employee_id: tasks}
    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as json_file:
        json.dump(output, json_file)

    print("Data exported to", filename)
