class Node(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return "The node has data {0}, left child {1} and right child {2}.".format(self.data,self.left.data,self.right.data)

class BSTree(object):
	def __init__(self,rootData=None):
		if rootData:
			self.root = Node(rootData)
		else:
			self.root = None

	def insert(self,data):
		"""Create a chlid node and maintain the BST structure. """
		node = Node(data)
		cur = self.root
		while cur:
			if data < cur.data:
				if not cur.left: # found the position to insert
					cur.left = node
					return self.root
				cur = cur.left
			else:
				if not cur.right:
					cur.right = node
					return self.root
				cur = cur.right
		
		return self.root

	def search(self,root,value):
		""" Find whether a value is in the tree and return True/False """
		if not root:
			return False
		if value == root.data:
			return True
		elif value < root.data:
			return self.search(root.left,value)
		else:
			return self.search(root.right,value)
		

	def bfsTraverse(self):
		""" Return a list of data in the tree in level-order """
		queue = [self.root]
		bfs = []
		while queue:
			curr = queue.pop(0)
			bfs.append(curr.data)
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)
		return bfs

	def dfsTraverse(self,root,dfs=[]):
		""" Apply depth-first inorder search to print all the data in the tree """
		if not root :
			return None
		self.dfsTraverse(root.left)
		dfs.append(root.data)
		self.dfsTraverse(root.right)
		return dfs

""" TODO: Test Case"""

tree = BSTree(3)
tree.insert(5)
tree.insert(1)
tree.insert(10)
tree.insert(9)
tree.insert(2)
print tree.root

print tree.bfsTraverse()
print tree.dfsTraverse(tree.root)

print tree.search(tree.root,5)
print tree.search(tree.root,15)