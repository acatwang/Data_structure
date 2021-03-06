class Node(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return "The node has data {0}, left child {1} and right child {2}.".format(self.data,self.left.data,self.right.data)

class BSTree(object):
	def __init__(self,rootData=None):
		self.root = None
		if rootData:
			self.root = Node(rootData)
		
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

	def findMin(self,root): # find inorder sucessor
		""" Find the node with minimum val in right subtree """
		if not root :
			#print 'Empty Tree'
			return -1
		elif not root.left :
			return root

		return self.findMin(root.right)

	def delete(self,root,val):
		""" Remove the link to the given data without affecting BS tree """

		if not root:
			print "No such data"
			return None

		if val < root.data:
			root.left = self.delete(root.left,val)
		elif val > root.data:
			root.right = self.delete(root.right,val)
		else:  # found the to-be-deleted data
				# no child
				if not root.left and not root.right:
					return None
				
				# one child
				elif root.left and not root.right:
					return root.left
				elif root.right and not root.left:
					return root.right
				
				# two childs
				small = self.findMin(root)
				root.data = small.data
				root.right = self.delete(root.right,small.data)
		return root

	def getSuccessor(self,val):
		""" return the val of inorder successor node """
		root = self.root
		if not root:
			return "Empty Tree"
		
		visited = []
		cur = root
		while cur:
			
			if val > cur.data:
				visited.append(cur.data)	
				cur = cur.right
			elif val < cur.data:
				visited.append(cur.data)
				cur = cur.left
			else: # found the val
				if cur.right:
					return self.findMin(cur.right).data
				else :
					for x in visited[::-1]:
						if x >=cur.data:
							return x
		
		return "Not in the tree"


