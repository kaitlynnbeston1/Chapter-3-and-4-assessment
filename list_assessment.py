# Formative Assessment for Ch. 3 and 4


    # 1) Create a list of 4 things that you like,
#        (food, sports, subjects, etc)
bands = ["bullet for my valentine", "bring me the horizon", "metallica", "slayer"]
print("Original list:")
for band in bands:
    print(band)

       #a) Print the last item in your list in two different ways.
print("Printing last item 3 ways:")
print(f"{bands[3]}")
print(f"{bands[-1]}")


# b) Delete the first item in your list.
del bands[0]


       # c) Add a new item to your list.
bands.append("all that remains")

print("New list:")
for band in bands:
    print(band)

    
    '''
    2) Create a list of 4 classmates names, all lower case.
       a) Print the following sentence 4 times with a loop and
          replace the blank with a names from your list.
          Capitalize the names.:
               "One of my clasmates is named ________"
'''
classmates = ["kyler", "jake", "abdula", "kyle"]
for classmate in classmates:
    print(f"One of my classmates is named {classmate.title()}.")
'''
    3) Use range() to create a list of odd positive integers
       less than 20 and print out the list in reverse order.
'''
for num in range(1, 21, 2):
    print(num)
