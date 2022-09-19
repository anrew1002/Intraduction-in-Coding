with open("Blacklistet Networks.txt") as f:
    networks = f.read().splitlines()
counter = 0
print(len(networks))
for line in networks:
    # print(line.split("/")[1])
    counter += 2**(32-int(line.split("/")[1]))
print(counter)
