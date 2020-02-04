from work.file_handler import read_input
from work.file_handler import generate_output
from work.BFS import bfs_search
from work.AS import a_search
from work.UCS import ucs_search

input_file_name = './test_case/input_5.txt'
output_file_name = 'output.txt'


def find_optimal_path():
    # 获取input数据
    algorithm_type, size, src, max_elevation, target_num, targets_coordinate, geo_map = read_input(input_file_name)
    paths = []

    # 执行search算法
    if algorithm_type == 'BFS':
        visited = bfs_search(geo_map, src, set(targets_coordinate), max_elevation)
        # print(visited)
        # 生成路径数组
        for coordinate in targets_coordinate:
            path = []
            if coordinate in visited:
                while coordinate != (-1, -1):
                    path.append(coordinate)
                    coordinate = visited[coordinate]
                path.reverse()
            paths.append(path)

    elif algorithm_type == 'UCS':
        paths = ucs_search(geo_map, src, targets_coordinate, max_elevation)
        # print(paths)

    elif algorithm_type == 'A*':
        paths = a_search(geo_map, src, targets_coordinate, max_elevation)
        # print(paths)

    # 路径写入文件
    generate_output(output_file_name, paths)


if __name__ == '__main__':
    find_optimal_path()
