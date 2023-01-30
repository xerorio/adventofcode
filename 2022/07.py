# part 1

def part_1():
    with open('07.txt', 'r') as f:
        commands = f.readlines()

    dirs = {"/home": 0}
    path = "/home"

    for command in commands:
        # Commands start with $
        if command[0] == "$":
            # Do nothing, file sizes handled later
            if command[2:4] == "ls":
                pass
            # Manage changing the path 
            elif command[2:4] == "cd":
                # Go back to the root
                if command[5:6] == "/":
                    path = "/home"
                # Go back in the path
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]
                # Change the path
                else:
                    dir_name = command[5:]              # Get name of directory
                    path = path + "/" + dir_name        # Add to the path
                    dirs.update({path: 0})               # Update our dictionary
        # Do nothing when listing directories available
        elif command[0:3] == "dir":
            pass
        # size of a file
        else:
            size = int(command[:command.find(" ")])     # Get size of file
            # Update size for every directory down to /home
            path_copy = path
            for i in range(path.count("/")):
                dirs[path_copy] += size
                path_copy = path_copy[:path_copy.rfind("/")]

    total = 0
    for d in dirs:
        if dirs[d] < 100000:
            total += dirs[d]
    print(total)

# part_1()


# part 2

def part_2():
    with open('07.txt', 'r') as f:
        commands = f.readlines()

    dirs = {"/home": 0}
    path = "/home"

    for command in commands:
        # Commands start with $
        if command[0] == "$":
            # Do nothing, file sizes handled later
            if command[2:4] == "ls":
                pass
            # Manage changing the path 
            elif command[2:4] == "cd":
                # Go back to the root
                if command[5:6] == "/":
                    path = "/home"
                # Go back in the path
                elif command[5:7] == "..":
                    path = path[0:path.rfind("/")]
                # Change the path
                else:
                    dir_name = command[5:]              # Get name of directory
                    path = path + "/" + dir_name        # Add to the path
                    dirs.update({path: 0})               # Update our dictionary
        # Do nothing when listing directories available
        elif command[0:3] == "dir":
            pass
        # size of a file
        else:
            size = int(command[:command.find(" ")])     # Get size of file
            # Update size for every directory down to /home
            path_copy = path
            for i in range(path.count("/")):
                dirs[path_copy] += size
                path_copy = path_copy[:path_copy.rfind("/")]

    limit = 30000000 - (70000000 - dirs["/home"])
    valid_dirs = []
    for d in dirs:
        if limit <= dirs[d]:
            valid_dirs.append(dirs[d])
    print(min(valid_dirs))

# part_2()
