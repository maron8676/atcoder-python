class UnionFindNode(object):
    """
    Union-Find構造
    ノードのグループ併合や、所属グループ判定を高速に処理する
    """

    def __init__(self, group_id, parent=None, value=None):
        self.group_id_ = group_id
        self.parent_ = parent
        self.value = value
        self.size_ = 1

    def __str__(self):
        template = "UnionFindNode(group_id: {}, \n\tparent: {}, value: {}, size: {})"
        return template.format(self.group_id_, self.parent_, self.value, self.size_)

    def is_root(self):
        return not self.parent_

    def parent(self):
        parent = self
        while not parent.is_root():
            parent = parent.parent_
            self.parent_ = parent
        return parent

    def find(self):
        parent = self.parent()
        return parent.group_id_

    def size(self):
        parent = self.parent()
        return parent.size_

    def unite(self, unite_node):
        parent = self.parent()
        unite_parent = unite_node.parent()

        if parent.group_id_ != unite_parent.group_id_:
            if parent.size() > unite_parent.size():
                unite_parent.parent_ = parent
                parent.size_ = parent.size_ + unite_parent.size_
            else:
                parent.parent_ = unite_parent
                unite_parent.size_ = parent.size_ + unite_parent.size_


if __name__ == "__main__":
    node_list = [UnionFindNode(i) for i in range(4)]
    node_list[0].unite(node_list[3])
    node_list[1].unite(node_list[2])
    node_list[0].unite(node_list[2])
    print("\n".join(list(map(str, node_list))))
    print()
    print("\n".join(list(map(lambda x: str(x.parent()), node_list))))
