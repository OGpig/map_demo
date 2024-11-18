class MapData:
    def __init__(self):
        self.nodes = {}  # 存储所有节点
        self.roads = {}  # 存储所有道路
        self.buildings = {}  # 存储所有建筑

    def add_node(self, node_id, latitude, longitude):
        """添加一个节点"""
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, latitude, longitude)

    def add_road(self, road_id, name, node_ids):
        """添加一条道路"""
        nodes = [self.nodes[node_id] for node_id in node_ids if node_id in self.nodes]
        self.roads[road_id] = Road(road_id, name, nodes)

    def add_building(self, building_id, name, node_ids, levels=None):
        """添加一个建筑物"""
        nodes = [self.nodes[node_id] for node_id in node_ids if node_id in self.nodes]
        self.buildings[building_id] = Building(building_id, name, nodes, levels)

    def __repr__(self):
        return (f"MapData(nodes={len(self.nodes)}, roads={len(self.roads)}, "
                f"buildings={len(self.buildings)})")