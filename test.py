import osmnx as ox
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import networkx as nx

# 设置文件路径
osm_file = "map.osm"

# Step 1: 提取道路信息
graph = ox.graph_from_xml(osm_file)

# Step 2: 提取建筑信息
tree = ET.parse(osm_file)
root = tree.getroot()

buildings = []
nodes = {}

# 提取节点信息
for node in root.findall("node"):
    node_id = node.attrib['id']
    lat = float(node.attrib['lat'])
    lon = float(node.attrib['lon'])
    nodes[node_id] = (lon, lat)

# 提取建筑信息
for way in root.findall("way"):
    building = False
    for tag in way.findall("tag"):
        if tag.attrib.get('k') == 'building':
            building = True
            break
    if building:
        building_nodes = []
        for nd in way.findall("nd"):
            ref = nd.attrib['ref']
            if ref in nodes:
                building_nodes.append(nodes[ref])
        if building_nodes:
            buildings.append(building_nodes)

# Step 3: 绘制结果
fig, ax = plt.subplots(figsize=(10, 10))

# 绘制道路
ox.plot_graph(graph, ax=ax, show=False, close=False)

# 绘制建筑
#for building in buildings:
#    x, y = zip(*building)
#    ax.fill(x, y, color='gray', alpha=0.5, label='Building')

# 绘制节点
#for node_id, (lon, lat) in nodes.items():
#    ax.plot(lon, lat, 'o', color='red', markersize=2, label='Node')

# 设置标题
ax.set_title("Roads, Buildings, and Nodes from OSM")

# 显示绘图
plt.show()
