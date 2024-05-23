#!/usr/bin/python3
"""
Employee data query
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    to_do = endpoint + "/user/{}/todos".format(argv[1])
    name_uri = endpoint + "/users/{}".format(argv[1])
    res = get(to_do).json()
    name_res = get(name_uri).json()

    todo_num = len(res)
    completed = len([todo for todo in res
                         if todo.get("completed")])
    name = name_res.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, todo_num))
    for todo in res:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
