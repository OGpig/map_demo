class Building:
    def __init__(self, building_id, name, nodes, levels=None):
        self.building_id = building_id  # 建筑物的唯一标识
        self.name = name  # 建筑物名称
        self.nodes = nodes  # 描述建筑物轮廓的节点列表（节点ID）
        self.levels = levels  # 楼层数（可选）

    def __repr__(self):
        return f"Building(id={self.building_id}, name={self.name}, levels={self.levels})"
