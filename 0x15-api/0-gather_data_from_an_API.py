#!/usr/bin/python3
"""Fetches data from a REST API for a given employee ID."""
import sys
import requests

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

    completed_tasks = [task for task in todos_data if task['completed']]
    total_tasks = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], len(completed_tasks), total_tasks))
    [print("\t", task['title']) for task in completed_tasks]
