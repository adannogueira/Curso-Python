n = -120
help


'''def reverse(x: int):
    if x == 0:
        return x
    else:
        reverse = 0
        digit = 0
        while x != 0:
            digit = x % 10
            reverse = (reverse * 10) + digit
            x = x // 10
        return reverse

a = 123
b = -123
c = 120
d = 0
print(reverse(a))
print(reverse(b))
print(reverse(c))
print(reverse(d))'''