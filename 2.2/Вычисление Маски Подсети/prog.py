cidr = int(input("Введите маску:"))
full_baite = cidr//8
rest_baite = cidr % 8
output = []
for i in range(full_baite):
    output.append("255")
if rest_baite != 0:
    output.append(str(int("1"*rest_baite+"0"*(8-rest_baite), 2)))
while len(output) < 4:
    output.append("0")
print(output)
print(".".join(output))
