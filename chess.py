def chess(n : int) -> int:
    if n == 0:
        return 1
    return chess(n-1)*2

print(chess(4)) 

def sum_total(n : int) -> int:
    if n == 0:
        return 1
    return sum_total(n - 1) + chess(n)


print(sum_total(4))
