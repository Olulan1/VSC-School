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
slug2 = "A Hollow Knight: Silksong is breaking Steam, Nintendo's eShop"

#1 all lowercase
slug1 = slug1.lower()
slug2 = slug2.lower()

#2 no other characters besides letters -> using list comprehensions
slug1 = ("".join([char for char in slug1 if char.isalpha()]))
slug2 = ("".join([char for char in slug2 if char.isalpha()]))
print(slug2)

#3 no the, no a -> using list comprehensions
slug1 = slug1.split(" ")
slug2 = slug2.split(" ")
slug1= ("-".join([word for word in slug1 if word not in ("a", "the")]))
slug2 = ("-".join([word for word in slug2 if word not in ("a", "the")]))
print(slug2)

LenSlug1 = len(slug1)
LenSlug2 = len(slug2)

#4 
print(f"Length of slug1 is: {LenSlug1}")
if LenSlug1 > 25:
    while LenSlug1 > 25:
        idx = len(slug1)-1
        slug1 = slug1[:idx] + slug1[idx + 1:]
        LenSlug1 = len(slug1)
        print(slug1)

print(f"Length of slug2 is: {LenSlug2}")
if LenSlug2 > 25:
    while LenSlug2 > 25:
        idx = len(slug2)-1
        slug2 = slug2[:idx] + slug2[idx + 1:]
        LenSlug2 = len(slug2)
        print(slug2)

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
"""
slug1 = "Big dog steals the Sun"
slug2 = "A Hollow Knight: Silksong is breaking Steam, Nintendo's eShop"

#1
slug1 = slug1.lower()
slug2 = slug2.lower()

#2
slug1 = slug1.split(" ")
slug2 = slug2.split(" ")
print(slug1,"\n",slug2)
slug1 = ("".join([word for word in slug1 if word not in ("a", "the")])) # list comprehensions
slug2 = ("".join([word for word in slug2 if word not in ("a", "the")]))


#3 nvm

slug1 = list(slug1)
slug2 = list(slug2)
print(slug1,"\n",slug2)
slug1 = ("-".join([word for word in slug1 if word.isalpha()])) # list comprehensions
slug2 = ("-".join([word for word in slug2 if word.isalpha()]))
print(slug1,"\n",slug2)"""

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