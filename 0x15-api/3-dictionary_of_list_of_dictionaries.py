#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""
import json
import requests
from collections import defaultdict

todos_url = "https://jsonplaceholder.typicode.com/todos"
users_url = "https://jsonplaceholder.typicode.com/users"

def gather_employee_data():
    """ Gather to-do list information of all employees """
    employee_data = defaultdict(list)

    # Fetch all to-do items
    todos = requests.get(todos_url).json()

    # Group to-do items by user ID
    for todo in todos:
        user_id = todo['userId']
        employee_data[user_id].append({
            'task': todo['title'],
            'completed': todo['completed']
        })

    # Fetch usernames for all user IDs
    users = requests.get(users_url).json()
    username_map = {user['id']: user['username'] for user in users}

    # Add usernames to employee data
    for user_id, tasks in employee_data.items():
        username = username_map.get(user_id, "Unknown")
        for task in tasks:
            task['username'] = username

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(employee_data, jsonfile, indent=4)

if __name__ == "__main__":
    gather_employee_data()
