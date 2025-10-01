# for loop
for number in range(1, 10, 2):
    print("Atempt", number + 1, number * ".")
# for.. else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Atempted 3 times and failed")

#    nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# iterables
# while loops
number = 100
while number > 0:
    print(number)
    number //= 2
command = ""

while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
# infinite loops

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
