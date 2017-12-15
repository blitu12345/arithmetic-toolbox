def binary_tree(r):
	return [r, [], []]

def insert_left(root, new_branch):
	print "insertL"
	print "root",root
	t = root.pop(1)
	print "t",t
	if len(t) > 1:
		print "root",root
		root.insert(1, [new_branch, t, []])
		print "root",root
	else:
		root.insert(1, [new_branch, [], []])
	return root

def insert_right(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
			root.insert(2, [new_branch, [], t])
	else:
		root.insert(2, [new_branch, [], []])
	return root

def get_root_val(root):
	return root[0]

def set_root_val(root, new_val):
	root[0] = new_val

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

'''r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print l
insert_right(l, 7)
print l
print "root-value"
print get_root_val(l)
print r
print(get_right_child(get_right_child(r)))'''
r=binary_tree(1)
insert_left(r,3)
insert_right(r,4)
l=get_right_child(r)
print "l",l
insert_left(l,0)
print "l",l
insert_right(l,2)
print "l",l
insert_left(l,5)
print "l",l
print r