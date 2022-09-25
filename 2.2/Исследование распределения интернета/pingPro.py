with open("ping.txt", "r") as f:
    f.readline()
    input_list = f.readlines()
ping = []
output_list = []
for i in input_list:
    ping.append(i[-16:].strip())
#ping = ping[:10]

for i in ping:
    # print(i)
    for j in range(16-5):
        if i[j]+i[j+1]+i[j+2]+i[j+3] == "time":
            output_list.append(i[j+5:-3].replace(".", ","))
print(output_list[:10])
with open("result.txt", "w") as f:
    for i in output_list:
        f.write(i+"\n")
