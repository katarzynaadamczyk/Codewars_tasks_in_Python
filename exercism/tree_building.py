''' exercise Tree Building '''

from sklearn import tree


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id
        
    def __repr__(self) -> str:
        return 'Record ' + str(self.record_id) + ' has as parent ' + str(self.parent_id)


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []
    
    def __repr__(self) -> str:
        return 'Node ' + str(self.node_id) + ' has ' + str(len(self.children))


def BuildTree(records):
    if not records:
        return None
    records.sort(key=lambda x: (-x.parent_id, -x.record_id))
    ordered_id = sorted([i.record_id for i in records])
    if ordered_id[-1] != len(ordered_id) - 1 or ordered_id[0] != 0:
        raise ValueError("Record id is invalid or out of order.")
    trees, root = {}, None
    for record in records:
        if record.parent_id == record.record_id != 0:
            raise ValueError('Only root should have equal record and parent id.')
        if record.record_id < record.parent_id:
            raise ValueError('Node parent_id should be smaller than it\'s record_id.')
        trees.setdefault(record.parent_id, [])
        new_node = Node(record.record_id)
        new_node.children = list(reversed(trees.get(record.record_id, [])))
        if record.record_id == 0:
            root = new_node
        else:
            trees[record.parent_id].append(new_node)
    return root


def main():
    records = [
    Record(0, 0),
    Record(1, 0),
    Record(2, 0)
    ]
    root = BuildTree(records)
    print(root)

if __name__ == '__main__':
    main()
    