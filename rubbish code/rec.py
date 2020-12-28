def test(n):
    if n>0: return 5
    return test(n-1)

print(test(6))
