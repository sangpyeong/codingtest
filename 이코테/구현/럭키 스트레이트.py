n = input()


right = 0
left = 0
for i in range(len(n)):
    if i < len(n)/2:
        right += int(n[i])
    else:
        left += int(n[i])

if right == left:
    print("LUCKY")
else:
    print("READY")
