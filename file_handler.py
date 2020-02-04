import os


def read_input(filename):
    with open(filename, 'r') as file:
        algorithm_type = file.readline().rstrip()
        size = tuple(map(int, file.readline().split(' ')))
        src = tuple(map(int, file.readline().split(' ')))
        max_elevation = int(file.readline())
        target_num = int(file.readline())

        targets_coordinate = []
        for i in range(0, target_num):
            coordinate = tuple(map(int, file.readline().split(' ')))
            targets_coordinate.append(coordinate)

        geo_map = []
        for i in range(0, size[1]):
            line = list(map(int, file.readline().split(' ')))
            geo_map.append(line)

        return algorithm_type, size, src, max_elevation, target_num, targets_coordinate, geo_map


def generate_output(filename, paths):
    # 删除原output文件
    if os.path.exists(filename):
        os.remove(filename)

    # 写所有的路径
    with open(filename, 'w') as file:
        for path in paths:
            if not path:
                file.write('FAIL\n')
            else:
                for coordinate in path:
                    file.write(str(coordinate[0]) + ',' + str(coordinate[1]) + ' ')
                file.write('\n')

# if __name__ == '__main__':
#     print(read_input('input2.txt'))
