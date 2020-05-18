class BST(object):
    class Node(object):
        def __init__(self, val):
            self.key = val
            self.parent = None
            self.right = None
            self.left = None

        def set_parent(self, val):
            self.parent = val

        def set_left(self, val):
            self.left = val

        def set_right(self, val):
            self.right = val

        def change_key(self, val):
            self.key = val

        def get_children(self):
            return [self.left, self.right]

        def __lt__(self, other):
            return self.key < other.key

        def __le__(self, other):
            return self.key <= other.key

        def __gt__(self, other):
            return self.key > other.key

        def __ge__(self, other):
            return self.key >= other.key

        def __str__(self):
            """
            :return: node values - [key, left_child, right_child]
            """
            # return 'key: '+str(self.key)+'\n'+'left_child: '+str(self.left)+'\n'+'right_child: '+str(self.right)
            return 'key:' + str(self.key)

    def __init__(self):
        self.root = None
        self.num = 0
        self.in_order_list = []
        self.pre_order_list = []
        self.post_order_list = []

    def clear_order_lists(self):
        del self.in_order_list[:], self.in_order_list
        del self.pre_order_list[:], self.pre_order_list
        del self.post_order_list[:], self.post_order_list
        self.in_order_list = []
        self.pre_order_list = []
        self.post_order_list = []

    def find(self, key, root):
        node = self.Node(key)
        while root != node and root != None:
            if root < node:
                root = root.right
            else:
                root = root.left
        return root

    def get_min(self, root):
        while root.left != None:
            root = root.left
        return root

    def get_max(self, root):
        while root.right != None:
            root = root.right
        return root

    def next(self, root):
        if root.right != None:
            return self.get_min(root.right)
        parent = root.parent
        while parent != None and parent.right == root:
            root = parent
            parent = parent.parent
        return parent

    def previous(self, root):
        if root.left != None:
            return self.get_max(root.left)
        parent = root.parent
        while parent != None and parent.left == root:
            root = parent
            parent = parent.parent
        return parent

    def insert(self, key):
        n = self.Node(key)
        y = None
        x = self.root
        while x != None:
            y = x
            if n < x:
                x = x.left
            else:
                x = x.right
        n.parent = y
        if y == None:
            self.root = n  # in case if tree was empty
        elif n < y:
            y.left = n
        else:
            y.right = n
        self.num += 1

    def transplant(self, u, v):
        """
        :param u: old subtree root Node
        :param v: new subtree root Node
        """
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def delete(self, key):
        z = self.find(key, self.root)
        if z != None:
            self.num -= 1
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.get_min(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(y, y.left)
            y.left = z.left
            y.left.parent = y
        if z != None:
            del z

    def range_search(self, x, y, root):
        l = []
        n = self.find(x, root)
        while n.key <= y:
            if n.key >= x:
                l.append(n.key)
            n = self.find(n.key, root)
        return l

    def in_order_walk(self, root):
        if root == 'default':
            self.in_order_walk(self.root.left)
            self.in_order_list.append(self.root.key)
            self.in_order_walk(self.root.right)
        else:
            if root != None:
                self.in_order_walk(root.left)
                self.in_order_list.append(root.key)
                self.in_order_walk(root.right)
        if self.num == len(self.in_order_list):
            return self.in_order_list

    def pre_order_walk(self, root='default'):
        if root == 'default':
            self.pre_order_list.append(self.root.key)
            self.pre_order_walk(self.root.left)
            self.pre_order_walk(self.root.right)
        else:
            if root != None:
                self.pre_order_list.append(root.key)
                self.pre_order_walk(root.left)
                self.pre_order_walk(root.right)
        if self.num == len(self.pre_order_list):
            return self.pre_order_list

    def post_order_walk(self, root='default'):
        if root == 'default':
            self.post_order_walk(self.root.left)
            self.post_order_walk(self.root.right)
            self.post_order_list.append(self.root.key)
        else:
            if root != None:
                self.post_order_walk(root.left)
                self.post_order_walk(root.right)
                self.post_order_list.append(root.key)
        if self.num == len(self.post_order_list):
            return self.post_order_list

    def read(self):
        self.num = int(input())
        self.keys = [0 for i in range(self.num)]
        self.lefts = [0 for i in range(self.num)]
        self.rights = [0 for i in range(self.num)]
        for i in range(self.num):
            key, left, right = map(int, input().split(' '))
            self.keys[i] = key
            self.lefts[i] = left
            self.rights[i] = right

    def build_from_data(self):
        self.nodes = [self.Node(i) for i in self.keys]
        for i in range(self.num):
            left, right = self.lefts[i], self.rights[i]
            if left != -1:
                self.nodes[i].left = self.nodes[left]
                self.nodes[i].left.parent = self.nodes[i]
            if right != -1:
                self.nodes[i].right = self.nodes[right]
                self.nodes[i].right.parent = self.nodes[i]

    def check_bst(self, root):
        if root.left == None and root.right == None:
            if root == root.parent.left:
                return root < root.parent
            else:
                return root >= root.parent

        elif root.left == None:
            if root > root.right:
                return False
            else:
                return self.get_min(root.right) < root
        elif root.right == None:
            if root.key <= root.left.key:
                return False
            else:
                return self.get_max(root.left) >= root
        else:
            x = self.check_bst(root.left)
            y = self.check_bst(root.right)
            return x and y

    def __len__(self):
        return self.num