"""
Task 2.1: Fetch and Display Posts Using GET Request

Goal: Learn to make GET requests to an API and display the results.

Exercises:
- Fetch and display all posts (first 5)
- Fetch a single post by ID
- Fetch users and display their names
"""

import httpx

# Exercise 1.1: Fetch and display all posts (first 5)
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Send GET request and display first 5 posts

getr = httpx.get(f"{url}")
"""if getr.status_code == 200:
    data = getr.json()
    for i in range (0,5):
        print(data[i])
else:
    print(getr)"""

# Exercise 1.2: Fetch a single post by ID
url = "https://jsonplaceholder.typicode.com/posts/1"
# TODO: Send GET request and display the post details
# print(data[1])

# Exercise 1.3: Fetch users and display their names
url = "https://jsonplaceholder.typicode.com/users"
# TODO: Send GET request and display user names

getusers = httpx.get(url)
if getusers.status_code == 200:
    users = getusers.json()
    for i in range (0,len(users)):
        print(users[i]['name'])