import sys
states = {"red": 4, "red_amber": 3, "green": 5 , "amber": 3 }

try:
    steps = int(input("Input the number of steps you would like to see: "))
except ValueError as e:
    sys.exit("That is not an integer!")

state = "red"
iterations = 0
for i in range(0, steps+1):
    if (state == "red") & (iterations ==0) | (state == "amber") & (iterations == states["amber"]):
        if (iterations == 3) & (iterations == states["amber"]):
            iterations = 0
        if (iterations == 0):
            state = "red"
    elif (state == "red") & (iterations == states["red"]) | (state == ("red_amber")) & (iterations < states["red_amber"]):
        if (iterations == 4) & (state == "red"):
            iterations = 0
        state = "red_amber"
    elif (state == "red_amber") & (iterations == states["red_amber"]) | (state == "green") & (iterations < states["green"]):
        if (iterations ==3) & (state == "red_amber"):
            iterations = 0
        state = "green"
    elif (state == "green") & (iterations == states["green"]) | (state == "amber") & (iterations <states["amber"]):
        if (iterations ==5) & (state == "green"):
            iterations = 0
        state = "amber"
    iterations+=1
    if i < 10:
        print(f"Time 00{i} State {state}")
    elif  100 > i >= 10:
        print(f"Time 0{i} State {state}")
    else:
        print(f"Time {i} State {state}")

    
    


