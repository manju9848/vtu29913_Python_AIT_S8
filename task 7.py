# Monkey and Banana Problem - Moving the Box

monkey_position = 0
box_position = 2
banana_position = 4

print("Initial State:")
print("Monkey position:", monkey_position)
print("Box position:", box_position)
print("Banana position:", banana_position)

# Move monkey to the box
print("\nMonkey moves from 0 to 2.")
monkey_position = box_position

# Push the box towards the banana
def push_box():
    global monkey_position, box_position

    while box_position < banana_position:
        box_position += 1
        monkey_position += 1
        print("Monkey pushes the box to position", box_position)

# Call push_box operation
push_box()

# Check final state
print("\nFinal State:")
print("Monkey position:", monkey_position)
print("Box position:", box_position)
print("Banana position:", banana_position)

if box_position == banana_position:
    print("Success! The box is positioned correctly.")
    print("Monkey can now get the banana.")
else:
    print("Failure! The box is not in the correct position.")
