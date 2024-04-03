#coding problem 3
class Node():

    def __init__(self, val: str, left = None, right = None) -> None:
        self.val = val 
        self.left = left
        self.right = right

node = Node('root', Node('Left', Node('left.left')), Node('right'))

def serialize(root: Node):
    values: list = []

    def serializer(node):
        if not node:
            values.append('?')
        else:
            values.append(str(node.val))
            serializer(node.left)
            serializer(node.right)
    serializer(root)
    return ','.join(values)

def deserialize(s: str):
    serialized = iter(s.split(','))

    def deserializer() -> Node | None:
        val = next(serialized)
        if val == '?':
            return None
        else:
            node: Node = Node(val)
            node.left = deserializer()
            node.right = deserializer()
        return node
    return deserializer()

assert deserialize(serialize(node)).left.left.val == 'left.left'