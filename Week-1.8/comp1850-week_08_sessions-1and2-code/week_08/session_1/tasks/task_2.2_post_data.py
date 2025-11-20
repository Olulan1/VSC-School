"""
Task 2.2: Send Data Using POST Requests

Goal: Learn to send data to an API using POST requests.

Exercises:
- Create a new post
- Add a new comment to a post
- Create a new user
"""

import httpx

# Exercise 2.1: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Define new post data and send POST request

data = {
    'name': "Waluigi",
    'Cool': True,
    'Residence': "Diamond mansion",
    "Smash invitation": 0
}
r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
request = httpx.post("https://jsonplaceholder.typicode.com/posts", data=data)
if request.status_code == 200:
    print("Success")
elif request.status_code == 201:
    print("Post created")
else:
    print(request)

# Exercise 2.2: Add a new comment to a post
url = "https://jsonplaceholder.typicode.com/comments"
# TODO: Define new comment data and send POST request



# Exercise 2.3: Create a new user
url = "https://jsonplaceholder.typicode.com/users"
# TODO: Define new user data and send POST request
