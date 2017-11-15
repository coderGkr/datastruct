class bst:
	def __init__(self,val=0,left=None,right=None):
		self.left=left
		self.right=right
		self.val=val
	def addval(self,val):
		if self.val is 0:
			self.val=val
		elif self.val > val:
			if self.left is None:
				self.left=bst(val)
			else:
				self.left.addval(val)
		else:
			if self.right is None:
				self.right=bst(val)
			else:
				self.right.addval(val)
	def disptree(self,val=0):
		for i in range(0,val):
			print "-",
		print self.val
		if self.left is not None:
			print "l",
			self.left.disptree(val+1)
		if self.right is not None:
			print "r",
			self.right.disptree(val+1)
	def search(self,val):
		if self.val==val:
			return 1
		elif val <= self.val:
			if self.left is None:
				return 0
			else:
				self.left.search(val)
		else:
			if self.right is None:
				return 0
			else:
				self.right.search(val)

#Inorder successor
#inorder predecessor

#delete a node

a=[87, 50, 41, 53, 6, 4, 94, 72, 40, 17]
# import random
# for i in range(0,10):
# 	a.append(random.randint(1,45))

k=bst()
for i in a:
	k.addval(i)

# k.disptree()
print k.search(65)

print k.search(53)



# a=raw_input("enter the numbr")
# print str(a)
