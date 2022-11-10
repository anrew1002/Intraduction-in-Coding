with open('plist.txt', 'r') as f:
    f = f.readline().strip()
    f = f.replace('[', '(').replace(']', '),')[:-1]
    print(f)
