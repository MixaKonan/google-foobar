def solution(src, dest):
    src = (int(src / 8), src % 8)
    dest = (int(dest / 8), dest % 8)
    visited = {}
    moves = []
    dive(src, dest, visited, 0, moves)
    return min(moves)


def dive(src, dest, visited, move, moves):
    current_visited = dict(visited)
    if len(moves) > 0 and move > min(moves):
        return

    if src == dest:
        if move not in moves:
            moves.append(move)
        return
    
    if src[0] < 0 or src[0] > 7 or src[1] < 0 or src[1] > 7:
        return
    
    if src in current_visited:
        return

    current_visited[src] = True

    return [dive((src[0] - 2, src[1] - 1), dest, current_visited, move + 1, moves), dive((src[0] - 2, src[1] + 1), dest, current_visited, move + 1, moves),
            dive((src[0] - 1, src[1] - 2), dest, current_visited, move + 1, moves), dive((src[0] - 1, src[1] + 2), dest, current_visited, move + 1, moves),
            dive((src[0] + 1, src[1] - 2), dest, current_visited, move + 1, moves), dive((src[0] + 1, src[1] + 2), dest, current_visited, move + 1, moves),
            dive((src[0] + 2, src[1] - 1), dest, current_visited, move + 1, moves), dive((src[0] + 2, src[1] + 1), dest, current_visited, move + 1, moves)]


print(solution(19, 36))
print(solution(0, 1))
print(solution(0, 63))