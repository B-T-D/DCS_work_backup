# if vs elif issue

n = 13
result = n
if n > 12:
    result = result + 12
# if n < 5:
elif n < 5:
    result = result + 5
else:
    result = result + 2

print(result)
