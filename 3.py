def solution(src, dest):
    if isStraightAdjacent(src, dest):
        return 3
    
    if isDiagonalAdjacent(src, dest):
        return 4
    
    
def isStraightAdjacent(src, dest):
    return src - 1 == dest or src + 1 == dest or src + 8 == dest or src - 8 == dest


def isDiagonalAdjacent(src, dest):
     return src - 7 == dest or src + 7 == dest or src + 9 == dest or src - 9 == dest


print(solution(0, 1))
print(solution(0, 9))