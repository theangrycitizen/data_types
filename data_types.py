# Datatypes function to compares arguments and return 
# results based on the argument provided.
def data_type(A):

	if type(A) == str:
		return len(A)

# Return ''No Value'If no String data type is available

	if A == None:
		return 'no value'

	if type(A) == bool:
		return A

# Comparing Integers

	if type(A) == int:
		if A < 100:
			return 'less than 100'
		elif A == 100:
			print 'equal to 100'
			return None
		else:
			return 'more than 100'

# For Lists return the 3rd Item or No item if not there

	if type(A) == list:
		mylist = A[2:3]
		if mylist:
			return mylist[0]
		else:
			return None
