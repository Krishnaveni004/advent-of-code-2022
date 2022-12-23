class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None
        self.is_leaf = False
        self.size = 0
        self.result = 0

    def add_child(self, node):
        self.children.append(node)

    def set_size(self, size):
        self.size = size

    def __repr__(self):
        return self.value


class Tree:

    def get_indent(self, indent):
        string = '\t'
        for i in range(indent):
            string += '\t'
        return string

    def print_tree(self, _node, indent=0):
        print(f'{self.get_indent(indent)}{_node.value}: {_node.size}, {_node.size <= 100000}')
        if _node.is_leaf:
            return

        for child in _node.children:
            self.print_tree(child, indent + 1)

    def print_result_tree(self, _node, indent=0):
        print(f'{self.get_indent(indent)}{_node.value}: {_node.result}/{_node.size}')
        if _node.is_leaf:
            return

        for child in _node.children:
            self.print_result_tree(child, indent + 1)

    def update_size(self, _node: TreeNode):
        if _node.is_leaf:
            return _node.size

        for child in _node.children:
            _node.size += self.update_size(child)

        return _node.size

    def update_result(self, _node: TreeNode):
        if _node.is_leaf:
            _node.result = 0
        elif _node.size > 100000:
            _node.result = 0
        else:
            _node.result = _node.size

        for child in _node.children:
            _node.result += self.update_result(child)

        return _node.result

    def big_directories(self, _node: TreeNode, required, ans):
        if _node.is_leaf:
            return

        if required <= _node.size < ans[-1]:
            ans.append(_node.size)

        for child in _node.children:
            self.big_directories(child, required, ans)


def main():
    current_node = TreeNode('/')
    tree = current_node

    with open('input.txt', 'r') as puzzle_input:
        readable = puzzle_input.readlines()

        for line in readable:
            line = line.replace('\n', '')
            if line.startswith('$'):
                if line.startswith('$ cd ..'):
                    current_node = current_node.parent

                elif line.startswith('$ cd'):
                    directory_name = line.split(' ')[2].strip()
                    if directory_name == '/':
                        continue

                    for child in current_node.children:
                        if child.value == directory_name:
                            node = child
                            break

                    node.parent = current_node
                    current_node = node

                elif line.startswith('$ ls'):
                    pass
                else:
                    raise NotImplementedError
            else:
                if line.startswith('dir'):
                    directory_name = line.split('dir')[-1].strip()
                    node = TreeNode(directory_name)
                else:
                    size, file_name = line.split(' ')
                    node = TreeNode(file_name)
                    node.size = int(size)
                    node.is_leaf = True
                node.parent = current_node
                current_node.add_child(node)

    tree_object = Tree()
    tree_object.update_size(tree)
    tree_object.update_result(tree)

    required = tree.size - 40000000
    print(f'Required is {required}')
    result = [tree.size]
    tree_object.big_directories(tree, required, result)

    print(result)


if __name__ == '__main__':
    main()
