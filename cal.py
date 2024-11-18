import osmnx as ox
import networkx as nx
import numpy as np
import pandas as pd

# Step 1: 加载本地 OSM 文件
osm_file = "map.osm"  # 替换为你的 OSM 文件路径
graph = ox.graph_from_xml(osm_file, simplify=True)  # 加载路网数据

# Step 2: 定义起点和终点的坐标
origins = [(22.5277249, 113.9340445), (22.5285296, 113.9244485)]  # 替换为实际起点坐标
destinations = [(22.5030617, 113.8739242), (22.4999635, 113.8772676)]  # 替换为实际终点坐标

# 将坐标映射到最近的图节点
orig_nodes = [ox.nearest_nodes(graph, lon, lat) for lat, lon in origins]
dest_nodes = [ox.nearest_nodes(graph, lon, lat) for lat, lon in destinations]

# Step 3: 计算 OD 矩阵
# 初始化 OD 矩阵
od_matrix = np.zeros((len(orig_nodes), len(dest_nodes)))

# 遍历起点和终点，计算最短路径距离
for i, orig in enumerate(orig_nodes):
    for j, dest in enumerate(dest_nodes):
        try:
            # 使用 networkx 计算最短路径距离（单位：米）
            distance = nx.shortest_path_length(graph, orig, dest, weight="length")
            od_matrix[i, j] = distance
        except nx.NetworkXNoPath:
            # 如果无路径可达，设为无穷大
            od_matrix[i, j] = np.inf

# Step 4: 可视化 OD 矩阵
# 转为 Pandas DataFrame 方便查看
od_df = pd.DataFrame(
    od_matrix,
    columns=[f"Dest {i+1}" for i in range(len(dest_nodes))],
    index=[f"Orig {i+1}" for i in range(len(orig_nodes))]
)

print("OD Matrix (meters):")
print(od_df)

# Step 5: 分析可达性（示例：计算平均可达性）
# 计算每个起点的平均可达性
average_accessibility = np.mean(od_matrix, axis=1)
print("Average Accessibility (meters):", average_accessibility)
