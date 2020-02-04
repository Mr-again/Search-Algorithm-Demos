def ucs_search(geo_map, src, dest_list, max_elevation):
    paths = []

    # 遍历目标点坐标数组，进行搜索
    for dest in dest_list:
        # 用于存储一次搜索的路径
        path = []

        flg, pre_point, closed_list = ucs_search_one_dest(geo_map, src, dest, max_elevation)
        # print(pre_point)
        # print(closed_list)

        if not flg:
            paths.append(path)
        else:
            path.insert(0, dest)
            while pre_point != (-1, -1):
                path.insert(0, pre_point)
                pre_point = closed_list.get(pre_point)[0]
            paths.append(path)
            
    return paths


# geo_map是一个二维数组，存地图
# src是出发点坐标
# dest是目标点坐标list
# max_elevation是最大海拔跨度
def ucs_search_one_dest(geo_map, src, dest, max_elevation):
    height = len(geo_map)
    width = len(geo_map[0])

    # open、closed表
    open_list = [[0, src, (-1, -1)]]
    closed_list = dict()

    while open_list:
        # 当前节点
        tmp_cost, temp_point, pre_point = open_list.pop(0)

        # 找到目标点
        if temp_point == dest:
            return True, pre_point, closed_list

        neighbor = [-1, 0, 1]
        for i in neighbor:
            for j in neighbor:

                # 去除自己
                if (i == 0) and (j == 0):
                    continue

                # 获得邻居坐标
                neighbor_row = temp_point[1] + i
                neighbor_col = temp_point[0] + j

                # 删除越界邻居
                if neighbor_row < 0 or neighbor_row >= height or neighbor_col < 0 or neighbor_col >= width:
                    continue

                # 获得海拔差距
                diff_elevation = abs(geo_map[temp_point[1]][temp_point[0]] - geo_map[neighbor_row][neighbor_col])
                if diff_elevation > max_elevation:
                    continue

                # 获得f_cost增加量
                if abs(i * j) == 1:
                    diff_cost = 14
                else:
                    diff_cost = 10

                cost = diff_cost + tmp_cost
                # 判断在不在closed里
                if (neighbor_col, neighbor_row) in closed_list:
                    if cost < closed_list[(neighbor_col, neighbor_row)][1]:
                        closed_list.pop((neighbor_col, neighbor_row))
                        open_list.append(
                            [cost, (neighbor_col, neighbor_row), temp_point])
                    continue

                # 判断在不在open里
                flg = -1
                for k in range(len(open_list)):
                    if open_list[k][1] == (neighbor_col, neighbor_row):
                        flg = k
                        break

                if flg == -1:
                    open_list.append([cost, (neighbor_col, neighbor_row), temp_point])
                else:
                    if cost < open_list[flg][0]:
                        open_list.pop(flg)
                        open_list.append([cost, (neighbor_col, neighbor_row), temp_point])

        # tmp_point加入closed
        closed_list[temp_point] = [pre_point, tmp_cost]

        # sort open
        open_list.sort()

    return False, (-1, -1), closed_list
