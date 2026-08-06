from os import listdir
from os.path import isfile, join
from collections import deque


def print_filenames_bfs(dir):
    """BFS approach"""
    search_queue = deque([dir])
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            full_path = join(dir, file)
            if isfile(full_path):
                print(file)
            else:
                search_queue.append(full_path)


def print_filenames_dfs(dir):
    for file in sorted(listdir(dir)):
        full_path = join(dir, file)
        if isfile(full_path):
            print(file)
        else:
            print_filenames_dfs(full_path)


if __name__ == "__main__":
    print("==Output in BFS==")
    print_filenames_bfs("test_dir")
    print("==Output in DFS==")
    print_filenames_dfs("test_dir")
