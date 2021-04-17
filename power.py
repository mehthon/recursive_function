def power(num,pow):
    if pow == 1:
        return num
    else:
        return num * power(num,pow - 1)

print(power(int(input()),int(input())))
