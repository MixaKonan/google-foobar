# def solutionx(xs):
    
#     if len(xs) == 1:
#         return str(xs[0])
    
#     value = 1
#     biggest_negative = None

#     for num in xs:
#         if num < 0:
#             negative_count += 1
#             if biggest_negative is None:
#                 biggest_negative = num
#             elif num > biggest_negative:
#                 biggest_negative = num
        
#         value = value * num if num != 0 else value
    
#     return str(int(value))
def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    negative_nums = [number for number in xs if number < 0]
    non_negative_nums = [number for number in xs if number >= 0]

    if len(negative_nums) <= 1 and all([x == 0 for x in non_negative_nums]):
        return '0'

    positive_nums = [number for number in non_negative_nums if number != 0]

    if len(negative_nums) % 2 == 1:
        negative_nums.sort()
        negative_nums.pop()
    
    value = 1
    for number in positive_nums + negative_nums:
        value *= number

    return str(value)
    

print(solution([0]) == '0')
print(solution([1]) == '1')
print(solution([-1]) == '-1')
print(solution([10, -1]) == '10')
print(solution([-1, 10]) == '10')
print(solution([-1, -2]) == '2')
print(solution([-4, 0]) == '0')
print(solution([0, -4]) == '0')
print(solution([-1, -2, -3]) == '6')
print(solution([-2, -3, -4, 0, 5]) == '60')
print(solution([2, 0, 2, 2, 0]) == '8')
print(solution([999, 999, 999, -999, 0]) == str(999**3))

        
