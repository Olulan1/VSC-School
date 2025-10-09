import sys
try:
    userIn = int(input("Please input an integer grade from 1-100: "))
    if not (0 <= userIn <= 100):
        raise Exception()
    else:
        pass
except Exception:
    sys.exit('Error: Grade must be an integer between 0 and 100')

if userIn <= 39:
    "Failed."
    print(f"{userIn} is a Fail")
elif userIn <= 69:
    "Passed"
    print(f"{userIn} is a Pass")
elif userIn <= 100:
    "Distinction achieved."
    print(f"{userIn} is a Distinction. Congratulations.")
elif  userIn == "":
    sys.exit('Error: Grade must be an integer between 0 a   nd 100')
else:
   sys.exit('Error: Grade must be an integer between 0 and 100')
