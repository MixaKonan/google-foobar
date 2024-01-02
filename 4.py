def solution(l):
    count = 0
    for index in range(0, len(l)):
        count += findTripletsCount(index, l)

    return count
        

def findTripletsCount(first_index, l):
    count = 0
    first = l[first_index]
    dividends_of_first = [num for num in l[first_index + 1:] if num % first == 0]
    for second_index, second in enumerate(dividends_of_first):
        dividends_of_second = [num for num in dividends_of_first[second_index + 1:] if num % second == 0]
        count += len(dividends_of_second)
        
    return count

# print(solution([1, 1, 1]))
# print(solution([1, 2, 3, 4, 5, 6]))
# print(solution([1, 2, 8, 9, 10, 14, 16, 18, 27]))
# print(solution([1, 2, 7, 13, 17, 23]))
# print(solution([]))

print(solution([x for x in range(2, 9999)]))