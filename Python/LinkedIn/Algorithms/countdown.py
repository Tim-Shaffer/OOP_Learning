# use recursion to implement a countdown counter
def countdown(x):
    if x == 0:
        print("Done!")
        return  # this is the necessary break to avoid an infinite loop!
    else:
        print(x, "...")
        countdown(x-1)
        print("reverse step ", x)


countdown(5)