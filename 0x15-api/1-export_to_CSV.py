#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        base_url + "users/{}".format(employee_id)
    ).json()
    username = user.get("username")
    todos = requests.get(
        base_url + "todos", params={"userId": employee_id}
    ).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo.get("completed"),
                todo.get("title")
            ])
