fixed = []

with open('phone_numbers.txt', 'r') as file:
    content = file.readlines()

for number in content:
    number = number.strip().replace(" ", "").replace("-", "")
    
    # If the number starts with "+", prepend "0"
    if number.startswith("+") and not number.startswith("+972"):
        number = "0" + number[1:]

    # If the number doesn't start with "0", skip to the next iteration
    if number[0] != "0":
        continue

    if len(number) < 9 or len(number) > 10:
        continue

    fixed.append(number)

with open('fixed_phone_numbers.txt', 'w') as file:
    for number in fixed:
        file.write(number + "\n")