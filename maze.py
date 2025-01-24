from collections import deque

def find_positions(maze, target):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == target:
                return (i, j)
    return None

def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    start = find_positions(maze, 'S')
    end = find_positions(maze, 'E')

    if not start or not end:
        return "Ошибка: в лабиринте нет S или E!"

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path  # Выводит найденный путь

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Варианты передвижения
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in [0, 'E'] and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None  # Если путь невозможно проложить


maze = [
    ['S', 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 'E']
]

print(bfs(maze))