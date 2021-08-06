# Write a program to display all Pythagoras triples less than 100.
# A Pythagoras triple is a set of three numbers a, b, and c, such that a2 + b2 = c2.
# Each triple should be printed only once, i.e. it should display either 3 4 5, or 4 3 5, not both

# AP: There are three parts to this problem
# - Generate pairs of numbers in given range that we want to check
# - Given a pair of numbers, determine if a Pythagoras triple exists
# - Apply this condition of all the pairs and print the ones that satisfy the condition

# In your approach you have given more importance to the removal of duplicates...
# You should approach the problem in a way to avoid duplicates in the first place,

# PART 1: Your way - I have made changes to make removing duplicates better
# ---------------------------------------------------------------------------
def remove_dup(list_b):  # AP: You should set() to remove duplicates. 
	for i in list_b:                                 # AP: You are looping over the list...
		if list_b.count(i) > 1:
			#print(list_b.count(i))
			list_b.remove(i)                         # ... while you are modifying the list.
	return list_b                                    # That is very bad practice!!!!!!!!

def pythagorus_tiplets():   # AP: pythagorAs_tRiplets (typos will cost your users a lot of pain). Please refactor
	list_of_nos_sq, final_list = [],[]
	list_of_nos = list(range(1, 100))

	for i in list_of_nos:
		list_of_nos_sq.append(i**2)

	for item in list_of_nos:
		for i in list_of_nos:
			#print(item, i)
			if item**2 + i**2 in list_of_nos_sq:  # AP: List search is too expensive. Do this arithmetically.
				# temp_list = []                               # AP: Why are you doing it this way?
				# temp_list.append(item)                       # Too long.
				# temp_list.append(i)                          # You want to use append() method primarily in a loop.
				# temp_list.append((item**2 + i**2)**(1/2))
				temp_list = [item, i, int((item**2 + i**2)**(1/2))]  # AP: It is one line list definition
				                                                     # Must convert result to int
																	 # Expr item**2+i**2 evaluated twice in a loop, why? 
				temp_list.sort()  # This becomes necessary to remove duplicates...
				final_list.append(tuple(temp_list))  # AP: Why do we need to convert to a tuple? Why not a list?
	# final_list = remove_dup(final_list)  # Not using your complex remove function
	final_list = set(final_list)  # This also removes duplicates.
	return final_list

print(sorted(pythagorus_tiplets()))  # AP: Just printing lists as output makes the eyes bleed!!

# CRITICISMS:
# - Typos in file name and function name (-1)
# - Using list append three times on empty list, instead of just assigning a list (-2)
# - Evaluating same exression twice (-1)
# - Not well formatted output, lazy (-2)
# - Too complex thought process (-1) 
# - but does the work (+1)
# ----------------
# Score : 4 / 10
# - Need to improve algorithm development


# --------------------------------------------------------------------------------
# PART 2: Optimal solution - follow this algorithm line by line

def calc_hypot(a: int, b: int) -> float:  # AP: takes two integers and returns a float
	"""Apply pythagoras theorem and calculate hypotenuse."""
	return (a ** 2 + b ** 2) ** 0.5

trip_list = []  # Collect the triples here
for x in range(1, 100):
	for y in range(x, 100):  # Starting from x prevents duplicate pair generation
		z = calc_hypot(x, y)
		
		# if round(z) == z:  # Check if the float z represtents an integer
		# if int(z) == z:  
		# if z // 1 == z:  # Check if integer part is equal to number
		if z % 1 == 0 and z <= 100:  # Check if fractional part is .00000
		
			trip_list.append([x, y, int(z)])  # appending a list containing integers only.

			
# ---------------------------
# Have well formatted output
print('\nx\t\ty\t\tz\n----------------------------')  # Table header
#                             Display in z column sorted order. BONUS!
for x, y, z in sorted(                   
				trip_list, 
				key=lambda x: x[2]  # An anonymous function that returns the 3rd item in the argument x
				):
	print(f'{x}\t\t{y}\t\t{z}')  # An f-string to format the line output

# --------------------------------------------------------------------------------
# PART 3: Extending the problem

# - Generalize the problem to finding pythagoras triples of a, b lying in the range [n:n+m]
# - Find all the numbers between 1-100 that are not hypotenuse of a right triangle
# - Find all the numbers between 1-100 that are not part of any pythagoras triple.

		