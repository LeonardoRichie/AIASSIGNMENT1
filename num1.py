def find_all_paths(maze):#find path
    def checkValid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] in ['0', 'g']

    def findneighbours(x, y):#find surroundings
        return [(x+i, y+j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)] if checkValid(x+i, y+j)]

    def find_paths_helper(x, y, path):
        if (x, y) == goal:
            all_paths.append(path)
            return

        for (nx, ny) in findneighbours(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))  
                find_paths_helper(nx, ny, path + [(nx, ny)])
                visited.remove((nx, ny))  

    start, goal = None, None

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "g":
                goal = (i, j)

    if start is None or goal is None:
        return "Start or goal not found in the maze."

    visited, all_paths = set(), []
    visited.add(start)
    find_paths_helper(*start, [start])

    return all_paths

def find_shortest_path(maze):#find shortest path
    all_paths = find_all_paths(maze)

    if not all_paths:
        return "No path found."

    shortest_path = min(all_paths, key=len)
    return shortest_path

def print_maze(maze):#print maze
    for row in maze:
        print(' '.join(row))
#maze list
maze = [
    ["S", "1", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "g", "0", "0", "1", "0"],
    ["0", "1", "0", "1", "1", "1", "0", "1", "0"],
    ["0", "1", "0", "1", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["0", "1", "0", "0", "0", "0", "0", "0", "0"]
]

all_paths = find_all_paths(maze)
shortest_path = find_shortest_path(maze)

print("All Paths:")
for path in all_paths:
    print(path)

print("\nShortest Path:")#print path
if isinstance(shortest_path, list):
    for x, y in shortest_path:
        maze[x][y] = 'X'
    print_maze(maze)
else:
    print(shortest_path)
