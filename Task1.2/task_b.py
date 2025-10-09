"""
Slug: a short identifier for the article, which is often based on the article's title.

Slug operation examples:
- making all letters lowercase,
- removing short words like “a”
- replacing spaces with hyphens
- A slug may also be truncated so it is 25 characters

For example, the tech news site Ars Technica recently published an article entitled:

“Hollow Knight: Silksong is breaking Steam, Nintendo's eShop”

The slug for this article is

hollow-knight-silksong-is-breaking-steam

In a file named task_b.py, write a program that transforms a title entered by the user into a slug
suitable for online publishing.

Your slug must
• Not contain any uppercase letters
• Not contain the words “a” or “the” at the start, or between other words
• Use hyphens in place of spaces
• Have a maximum length of 25 characters

Use a variable named slug to represent the final value for the slug, after applying the
transformations listed above.

Use exactly the following code to display the slug. This should be the only print statement in your
program.
print(f"Slug = {slug}")
"""

slug1 = "Big dog steals the Sun"
slug2 = "Hollow Knight: Silksong is breaking Steam, Nintendo's eShop"

#1
slug1 = slug1.lower()
slug2 = slug2.lower()

#2
slug1 = slug1.split(" ")
slug2 = slug2.split(" ")
print("-".join([word for word in slug1 if word not in ("a", "the")])) # list comprehensions
print("-".join([word for word in slug2 if word not in ("a", "the")]))

#3 
print("-".join([word for word in slug2 if word not in ("a", "the")]))

"""
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> a = "lani is learning python 324234234234:::???"
>>> [char for char in a if char.isalpha()]
['l', 'a', 'n', 'i', 'i', 's', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n']
>>> "".join([char for char in a if char.isalpha()])
'laniislearningpython'
>>>
"""