from queue import Queue


# geo_map是一个二维数组，存地图
# src是出发点坐标
# dest_list是目标点坐标set
# max_elevation是最大海拔跨度
def bfs_search(geo_map, src, dest_list, max_elevation):
    # 目标点数量
    dest_num = len(dest_list)

    # visited是一个map，key是坐标tuple，value是前驱坐标tuple
    visited = dict()
    visited[src] = (-1, -1)

    # bfs_queue用来存储访问过的坐标
    bfs_queue = Queue()
    bfs_queue.put(src)

    # 长宽定义
    height = len(geo_map)
    width = len(geo_map[0])

    while (not bfs_queue.empty()) and (dest_num != 0):
        col, row = bfs_queue.get()

        # 如果该节点是目标
        if (col, row) in dest_list:
            dest_num = dest_num - 1
        neighbor = [-1, 0, 1]

        for i in neighbor:
            for j in neighbor:

                # 去除自己
                if (i == 0) and (j == 0):
                    continue

                # 获得邻居坐标
                neighbor_row = row + i
                neighbor_col = col + j

                # 删除越界邻居
                if neighbor_row < 0 or neighbor_row >= height or neighbor_col < 0 or neighbor_col >= width:
                    continue

                # 获得海拔差距
                diff = abs(geo_map[row][col] - geo_map[neighbor_row][neighbor_col])
                if diff > max_elevation:
                    continue

                # 去除访问过的节点
                if (neighbor_col, neighbor_row) in visited:
                    continue

                # 将邻居节点加入visited和bfs_queue
                visited[(neighbor_col, neighbor_row)] = (col, row)
                bfs_queue.put((neighbor_col, neighbor_row))

    return visited
