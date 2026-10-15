
# Vacuum Cleaner Problem in AI

rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while True:
    print("\nCurrent Location:", location)
    print("Room Status:", rooms)

    if rooms[location] == 'Dirty':
        print("Action: Suck")
        rooms[location] = 'Clean'
    elif location == 'A':
        print("Action: Move Right")
        location = 'B'
    elif location == 'B':
        print("Action: Move Left")
        location = 'A'

    if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
        print("\nBoth rooms are clean!")
        break

print("Final Room Status:", rooms)
