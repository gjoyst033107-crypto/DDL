
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BSTModule:
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.val:
            root.left = self.insert(root.left, key)

        elif key > root.val:
            root.right = self.insert(root.right, key)

        return root

    def add(self, key):
        self.root = self.insert(self.root, key)

    # Preorder: Root, Left, Right
    def preorder(self, root):
        result = []

        if root:
            result.append(root.val)
            result += self.preorder(root.left)
            result += self.preorder(root.right)

        return result

    # Inorder: Left, Root, Right
    def inorder(self, root):
        result = []

        if root:
            result += self.inorder(root.left)
            result.append(root.val)
            result += self.inorder(root.right)

        return result

    # Postorder: Left, Right, Root
    def postorder(self, root):
        result = []

        if root:
            result += self.postorder(root.left)
            result += self.postorder(root.right)
            result.append(root.val)

        return result

    # DFS: Depth-First Search
    def dfs(self):
        return self.preorder(self.root)

    # BFS: Breadth-First Search
    def bfs(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            result.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return result


# Example usage
tree = BSTModule()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.add(value)

print("DFS:", tree.dfs())
print("Preorder:", tree.preorder(tree.root))
print("Inorder:", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))
print("BFS:", tree.bfs())
