
lst = []
N = int(input("Enter a number: "))
for _ in range(N):
    cmd = input("Enter a command: ").strip().split()
    if not cmd:
        continue
    if cmd[0] == 'insert' and len(cmd) == 3:
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'remove' and len(cmd) == 2:
        lst.remove(int(cmd[1]))
    elif cmd[0] == 'append' and len(cmd) == 2:
        lst.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        lst.sort()  
    elif cmd[0] == 'pop':
        lst.pop()
    elif cmd[0] == 'reverse':
        lst.reverse()
    else:
        print(f"Invalid command or missing arguments: {cmd}")
