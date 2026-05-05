# Smart Water Bottle Reminder

count = 0
while True:
    user = input("Enter (drink / skip): ")
    if user == "drink":
        count += 1
        print("Good! Water count =", count)
    elif user == "skip":
        print("Try to stay hydrated!")
    else:
        print("Invalid Input")
    if count == 5:
        print("Hydration Goal Complete 🎯")
        break