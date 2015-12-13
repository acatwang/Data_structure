import unittest, inspect
from Tree import Node,BSTree

class TreeTestCase(unittest.TestCase):
	"""Test the tree structure and the untility functions in Tree.py
	The example tree 
	 			5
			   / \
			  3   10
			 / \   \
			1   4   11
	"""
	inorders = [1,3,4,5,10,11]
	levels = [5,3,10,1,4,11]
	childs = [3,10,1,4,11]

	def makeTree(self):
		tree = BSTree(5)
		for kid in self.childs:
			tree.insert(kid)
		return tree

	
	def test_root(self):
		tree = BSTree(5)
		self.assertIsInstance(tree.root,Node)
		self.assertEqual(tree.root.data,5)
		self.assertIsNone(tree.root.left)

	def test_insert_left_child(self):
		tree = BSTree(5)
		tree.insert(3)
		self.assertIsInstance(tree.root.left, Node)
		self.assertEqual(tree.root.left.data,3)
		self.assertIsNone(tree.root.left.left)

	def test_insert_left_grandchild(self):
		tree = BSTree(5)
		tree.insert(3)
		tree.insert(1)				
		self.assertEqual(tree.root.left.left.data,1)
		self.assertIsNone(tree.root.left.right)	
		
	def test_search(self):
		tree = BSTree(5)
		for kid in self.childs:
			tree.insert(kid)
		for kid in self.childs:
			self.assertTrue(tree.search(tree.root,kid))

		self.assertFalse(tree.search(tree.root,500))
		self.assertFalse(tree.search(tree.root,-1))
		self.assertFalse(tree.search(tree.root,'abc'))
		self.assertFalse(tree.search(tree.root,None))

	def test_structure(self):
		tree = self.makeTree()
		
		# root
		self.assertEqual(tree.root.left.data,3)
		self.assertNotEqual(tree.root.left.data,1)
		self.assertEqual(tree.root.right.data,10)
		
		# Node 10
		kid_ten = tree.root.right
		self.assertIsNone(kid_ten.left)
		self.assertEqual(kid_ten.right.data,11)

		# Node 3
		kid_three = tree.root.left
		self.assertEqual(kid_three.left.data,1)
		self.assertEqual(kid_three.right.data,4)

		# Grand kid 1
		grand_one = kid_three.left
		self.assertIsNone(grand_one.left)
		self.assertIsNone(grand_one.right)

	def test_bfs(self):
		tree = self.makeTree()

		self.assertEqual(tree.bfsTraverse(),self.levels)

	def test_dfs_inorder(self):
		tree = self.makeTree()
		self.assertEqual(tree.dfsTraverse(tree.root),self.inorders)

	def test_find_min(self):
		emptyTree = BSTree()
		self.assertEqual(emptyTree.findMin(emptyTree.root), -1)
		tree = self.makeTree()
		self.assertEqual(tree.findMin(tree.root).data,10)
		three = tree.root.left
		self.assertEqual(tree.findMin(three).data,4)

	def test_delete_node_with_one_child(self):
		tree = self.makeTree()
		tree.delete(tree.root,10)
		self.assertFalse(tree.search(tree.root,10))
		self.assertEqual(tree.root.right.data,11)
	
	def test_delete_node_with_two_childs(self):
		tree = self.makeTree()
		tree.delete(tree.root,3)
		self.assertFalse(tree.search(tree.root,3))
		self.assertEqual(tree.root.left.data,4)

	def test_getSuccessor(self):
		tree = self.makeTree()
		self.assertEqual(tree.getSuccessor(1),3)
		self.assertEqual(tree.getSuccessor(3),4)
		self.assertEqual(tree.getSuccessor(5),10)
		self.assertEqual(tree.getSuccessor(4),5)
		self.assertEqual(tree.getSuccessor(42),"Not in the tree")

if __name__ == '__main__':
	unittest.main()