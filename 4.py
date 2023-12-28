def solution(l):
    first_pivot, triplets = 0, []
    
    while first_pivot < len(l) - 2:
        second_pivot = first_pivot + 1
        while second_pivot < len(l) - 1:
            third_pivot = second_pivot + 1
            while third_pivot < len(l):
                first = l[first_pivot]
                second = l[second_pivot]
                third = l[third_pivot]
                
                if isLuckyTriplet(first, second, third):
                    triplets.append((first, second, third))
                
                third_pivot += 1
            second_pivot += 1
        first_pivot += 1
        
    return triplets


def isLuckyTriplet(first, second, third):
    return third % second == 0 and second % first == 0 

print(solution([1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 9, 10, 14, 18, 27]))
print(solution([1, 2]))
print(solution([x for x in range(1, 20)]))