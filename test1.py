def solution():
    result = []

    arr = list(input().split())
    data = []
    for i in arr:
        if i == "BOOL":
            data.append(1)
        elif i == "SHORT":
            data.append(2)
        elif i == "FLOAT":
            data.append(4)
        elif i == "INT":
            data.append(8)
        elif i == "LONG":
            data.append(16)
    start = 0
    for i in range(len(data)):
        if data[i] == 16:
            while (start % 8 != 0):
                result.append('.')
                start += 1
            if start != 0:
                result.append(',')
            for j in range(16):
                if j == 8:
                    result.append(',')
                start += 1
                result.append('#')
        elif data[i] == 8:
            while (start % 8 != 0):
                result.append('.')
                start += 1
            if start != 0:
                result.append(',')
            for j in range(8):
                start += 1
                result.append('#')
        elif data[i] == 4:
            while (start % 4 != 0):
                result.append('.')
                start += 1
            if start % 8 == 0 and start != 0:
                result.append(',')
            for j in range(4):
                start += 1
                result.append('#')

        elif data[i] == 2:
            while (start % 2 != 0):
                result.append('.')
                start += 1
            if start % 8 == 0 and start != 0:
                result.append(',')
            for j in range(2):
                start += 1
                result.append('#')

        elif data[i] == 1:
            if start % 8 == 0 and start != 0:
                result.append(',')
            start += 1
            result.append('#')
    while (start % 8 != 0):
        start += 1
        result.append('.')
    if start > 128:
        print("HALT")
    else:
        result = ''.join(s for s in result)
        print(result)


solution()
