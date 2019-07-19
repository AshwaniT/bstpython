import queue


class PoliceTree:
    def __init__(self, comparer):
        self.root = None
        self.comparer = comparer
        self.inorderlist = []
        self.bsfList = []

    def empty(self):
        return self.root is None

    def insert(self, current, newNode):
        if current is None:
            current = newNode
            if self.empty():
                self.root = current
        elif self.comparer.compare(current, newNode) == 1:
            current.left = self.insert(current.left, newNode)
        elif self.comparer.compare(current, newNode) == -1:
            current.right = self.insert(current.right, newNode)
        else:
            current.fineAmt = float(current.fineAmt) + float(newNode.fineAmt)
        return current

    def search(self, curent, nodetosearch):
        if curent is None:
            return None
        if self.comparer.compare(curent, nodetosearch) == 0:
            return curent
        elif self.comparer.compare(curent, nodetosearch) == 1:
            return self.search(curent.left, nodetosearch)
        elif self.comparer.compare(curent, nodetosearch) == -1:
            return self.search(curent.right, nodetosearch)

    def getParent(self, current, childNode):
        parent = None
        while current is not None and self.comparer.compare(current, childNode):
            parent = current
            if self.comparer.compare(current, childNode) == -1:
                current = current.left
            else:
                current = current.right
        return parent

    def findMax(self, current):
        if current is None:
            return current
        elif current.right is None:
            return current
        return self.findMax(current.right)

    def inOrder(self, current):
        if current is None:
            return None
        self.inOrder(current.left)
        self.inorderlist.append(current)
        self.inOrder(current.right)
        return self.inorderlist

    def min(self, current):
        if current is None:
            return None
        elif current.left is None:
            return current
        else:
            return self.min(current.left)

    def max(self, current):
        if current is None:
            return None
        elif current.right is None:
            return current
        else:
            return self.max(current.right)

    def delete(self, current, nodetodelete):
        if current is None:
            return current
        comres = self.comparer.compare(current, nodetodelete)
        if comres == 1:
            current.left = self.delete(current.left, nodetodelete)
        elif comres == -1:
            current.right = self.delete(current.right, nodetodelete)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            temp = self.min(current.right)
            current.policeId = temp.policeId
            current.fineAmt = temp.fineAmt
            current.right = self.delete(current.right, temp)
        return current

    def height(self, current):
        if current is None:
            return -1
        lh = self.height(current.left)
        rh = self.height(current.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1

    def bsf(self):
        if self.empty():
            return None
        h = self.height(self.root)
        q = queue.Queue(maxsize=2 * h + 1)
        q.put(self.root)
        while not q.empty():
            c = q.get()
            self.bsfList.append(c)
            if c.left:
                q.put(c.left)
            if c.right:
                q.put(c.right)
        return self.bsfList
