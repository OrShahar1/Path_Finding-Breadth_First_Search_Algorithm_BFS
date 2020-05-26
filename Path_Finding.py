import queue


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


class Path_Finding():
    def __init__(self ,maze):
        self.maze = maze

    def printMaze(self , path=""):
        for x, pos in enumerate(self.maze[0]):
            if pos == "O":
                start = x

        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                i -= 1

            elif move == "R":
                i += 1

            elif move == "U":
                j -= 1

            elif move == "D":
                j += 1
            pos.add((j, i))

        for j, row in enumerate(self.maze):
            for i, col in enumerate(row):
                if (j, i) in pos:
                    print("+ ", end="")
                else:
                    print(col + " ", end="")
            print()


    def valid(self, moves):
        for x, pos in enumerate(self.maze[0]):
            if pos == "O":
                start = x

        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1

            elif move == "R":
                i += 1

            elif move == "U":
                j -= 1

            elif move == "D":
                j += 1

            if not (0 <= i < len(self.maze[0]) and 0 <= j < len(self.maze)):
                return False
            elif (self.maze[j][i] == "#"):
                return False

        return True


    def findEnd(self, moves):
        for x, pos in enumerate(self.maze[0]):
            if pos == "O":
                start = x

        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1

            elif move == "R":
                i += 1

            elif move == "U":
                j -= 1

            elif move == "D":
                j += 1

        if self.maze[j][i] == "X":
            print("Found: " + moves)
            self.printMaze(moves)
            return True

        return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze = Path_Finding(createMaze())

while not maze.findEnd( add):
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if maze.valid(put):
            nums.put(put)