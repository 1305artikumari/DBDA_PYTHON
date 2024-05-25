#Multiple inheritances are when a child’s class is derived from two or more parent classes.
#For example, you are inheriting some of the features from your father and some from your mother.
# creating class for father
class Dad():
	# writing a method for parent class 1
	def singing(self):
		print("Dad sings well")
		
# creating a class for mother
class Mom():
	# method for parent class 2
	def coding(self):
		print("Mom codes well")

# creating derived class
class Child(Dad, Mom):
	def play(self):
		print("Kid loves to play")

# creating object of the new derived class
child = Child()
# calling methods of parent classes and derived class
child.singing()
child.coding()
child.playing()		
