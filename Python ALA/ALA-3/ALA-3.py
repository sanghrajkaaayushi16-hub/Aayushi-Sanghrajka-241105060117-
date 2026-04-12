a = 4
b = 6

max_val = a if a > b else b

while True:
    if max_val % a == 0 and max_val % b == 0:
        print("LCM =", max_val)
        break
    max_val += 1