#!/usr/bin/python3
"""Fetches data from a REST API for a given employee ID."""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: {}" .format(sys.argv[0]))
        sys.exit(1)

    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = base_url + 'users'

    try:
        users_data = requests.get(users_url).json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)

    all_employee_data = {}

    for user in users_data:
        employee_id = str(user['id'])
        todos_url = base_url + 'todos?userId={}'.format(employee_id)
        try:
            todos_data = requests.get(todos_url).json()
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            continue

        user_tasks = [{"username": user['username'], "task": task['title'],
                       "completed": task['completed']} for task in todos_data]
        all_employee_data[employee_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)

    print("Data exported successfully to todo_all_employees.json")
