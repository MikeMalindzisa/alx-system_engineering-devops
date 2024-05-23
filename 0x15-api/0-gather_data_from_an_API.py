#!/usr/bin/python3
"""
Queries JSON Placeholder API to retrieve employee data.
"""

import requests
import sys


def get_employee_data(user_id):
    """
    Retrieves todo data and user's name from JSON Placeholder API.

    Args:
        user_id (int): ID of the user.

    Returns:
        dict: A dictionary containing the employee's name, number of tasks,
              and number of completed tasks, along with the list of completed
              tasks titles.
    """
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{user_id}/todos"
    name_url = f"{main_url}/users/{user_id}"

    # Fetch todo and name data
    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    # Count total number of tasks and completed tasks
    total_tasks = len(todo_result)
    completed_tasks = sum(1 for todo in todo_result if todo.get("completed"))

    # Get employee name
    employee_name = name_result.get("name")

    # Get list of completed tasks titles
    completed_tasks_titles = [todo.get("title") for todo in todo_result
                              if todo.get("completed")]

    return {
        "name": employee_name,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completed_tasks_titles": completed_tasks_titles
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    try:
        user_data = get_employee_data(user_id)
        print("Employee {} is done with tasks ({}/{}):".format(
                user_data["name"],
                user_data["completed_tasks"],
                user_data["total_tasks"]))
        for title in user_data["completed_tasks_titles"]:
            print("\t{}".format(title))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
