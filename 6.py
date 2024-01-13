def solution(start, length):
    initial_length = length
    value = 0
    while length != 0:
        for num in range(start, start + length):
            value = value ^ num
        start += initial_length
        length -= 1
    
    return value

print(solution(10, 1))
print(solution(0, 3))
print(solution(17, 4))