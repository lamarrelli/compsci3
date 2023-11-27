class Node():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return "internal_{}".format(id(self))

class Edge():
    def __init__(self, node1, node2):
        self.nodes = [node1, node2]

    def __str__(self):
        return "{}--{}".format(*self.nodes)

class Tree():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        return "tree_{} edges: {}".format(id(self), [str(x) for x in self.edges])

    def copy(self):
        conv = {node: Node(node.name) for node in self.nodes}
        new_nodes = list(conv.values())
        new_edges = [Edge(conv[edge.nodes[0]], conv[edge.nodes[1]]) for edge in self.edges]

        new_tree = Tree(new_nodes, new_edges)
        return new_tree


def enumerate_t(leaves):
    assert(len(leaves) > 1)
    
    if len(leaves) == 2:
        n1, n2 = leaves
        t = Tree()
        t.nodes = [Node(n1), Node(n2)]
        t.edges = [Edge(t.nodes[0], t.nodes[1])]
        return [t]
    elif len(leaves) > 2:
        old_t = enumerate_t(leaves[:-1])
        new_leaf_name = leaves[-1]
        trees = []
        for old_tree in old_t:
            for i in range(len(old_tree.edges)):
                new_t = old_tree.copy()
                edge_to_split = new_t.edges[i]
                old_n1, old_n2 = edge_to_split.nodes
                new_t.edges.remove(edge_to_split)
                internal = Node(None)
                new_t.nodes.append(internal)
                new_leaf = Node(new_leaf_name)
                new_t.nodes.append(new_leaf)
                new_t.edges.append(Edge(old_n1, internal))
                new_t.edges.append(Edge(old_n2, internal))
                new_t.edges.append(Edge(new_leaf, internal))
                trees.append(new_t) 

        return trees

def newick_format(tree_in):
    tree = tree_in.copy()

    if len(tree.nodes) == 1:
        return "{};".format(tree.nodes[0])
    elif len(tree.nodes) == 2:
        return "({},{});".format(*tree.nodes)
    elif len(tree.nodes) > 2:
        for candidate_node in tree.nodes:
            if candidate_node.name is not None:
                continue

            adjacent_edges = [edge for edge in tree.edges if candidate_node in edge.nodes]
            adjacent_nodes = [node for edge in adjacent_edges for node in edge.nodes if node in edge.nodes and node is not candidate_node]
            adjacent_leaves = [node for node in adjacent_nodes if node.name is not None]
            if len(adjacent_leaves) == 2 or len(adjacent_leaves) == 3:
                leaf1, leaf2 = adjacent_leaves[0: 2]
                edges_to_cut = [edge for edge in adjacent_edges if leaf1 in edge.nodes or leaf2 in edge.nodes]
                candidate_node.name = "({},{})".format(leaf1, leaf2)

                tree.nodes.remove(leaf1)
                tree.nodes.remove(leaf2)
                for edge in edges_to_cut: tree.edges.remove(edge)
                return newick_format(tree)

if __name__ == '__main__':
    leaves = open('rosalind_eubt.txt').read().split()
    trees = enumerate_t(leaves)

    print ('\n'.join([newick_format(tree) for tree in trees]))