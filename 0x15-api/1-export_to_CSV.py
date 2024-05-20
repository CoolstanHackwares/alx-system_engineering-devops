#!/usr/bin/python3
"""Fetches data from a REST API for an employee ID and exports it to CSV."""
import requests
import sys
import csv

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

    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user_data['name'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    print("Data exported to", filename)
