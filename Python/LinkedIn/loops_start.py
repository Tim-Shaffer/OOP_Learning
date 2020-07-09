#
# Example file for working with loops
#

def main():
    x = 0

  # define a while loop
#   while (x<5):
#         print(x)
#         x = x + 1

  # define a for loop (start at first but does not include the second number)
    # for x in range(5, 10):
    #     print(x)

  # use a for loop over a collection
    # days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print(d)
    
 
  # use the break and continue statements
    # for x in range(5, 10):
    #     # if (x==7): break
    #     if (x%2 == 0): continue # skips the rest of the processing and returns to the next iteration of the for loop
    #     print(x)

  #using the enumerate() function to get index 
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    # enumerate allows for the index of the array to be noted
    for i,d in enumerate(days):
        print(i, d)

if __name__ == "__main__":
  main()
