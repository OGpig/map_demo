import osmnx as ox
import matplotlib.pyplot as plt

# 指定 OSM 文件路径
osm_file = "map (2).osm"  # 替换为你的 osm 文件路径

# 加载 OSM 文件，使用 graph_from_xml 替代 graph_from_file
graph = ox.graph_from_xml(osm_file)  # 加载路网数据

# 提取节点和边
nodes, edges = ox.graph_to_gdfs(graph)

# 创建绘图
fig, ax = plt.subplots(figsize=(12, 12))

# 绘制路网
edges.plot(ax=ax, linewidth=0.5, edgecolor="black", label="Edges")
nodes.plot(ax=ax, markersize=5, color="red", label="Nodes")

# 设置标题和图例
ax.set_title("OSM Network - Points and Lines", fontsize=16)
ax.legend()

# 显示绘图
plt.show()
