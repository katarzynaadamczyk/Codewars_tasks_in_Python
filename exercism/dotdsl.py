''' exercise dotdsl '''


NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if type(data) == type([]):
            for piece in data:
                if len(piece) > 1:
                    if piece[0] == NODE:
                        if len(piece) == 3 and type(piece[1]) == type('a') and type(piece[2]) == type({}):
                            self.nodes.append(Node(piece[1], piece[2]))
                        else:
                            raise ValueError("Node is malformed")
                    elif piece[0] == EDGE:
                        if len(piece) == 4 and type(piece[1]) == type(piece[2]) == type('a') and type(piece[3]) == type({}):
                            self.edges.append(Edge(piece[1], piece[2], piece[3]))
                        else:
                            raise ValueError("Edge is malformed")
                    elif piece[0] == ATTR:
                        if len(piece) == 3:
                            self.attrs.setdefault(piece[1], piece[2])
                        else:
                            raise ValueError("Attribute is malformed")
                    else:
                        raise ValueError("Unknown item")
                else:
                    raise TypeError("Graph item incomplete")
        elif data is not None:
            raise TypeError("Graph data malformed")
       