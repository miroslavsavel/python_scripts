import os

project_folder = os.path.join(os.getcwd())
working_folder = os.path.join(os.getcwd(), 'data_small_test')		#switch from test to DATA on production
old_folder = os.path.join(os.getcwd(), 'OLD_small_test')

# TODO remove old newDomains file
# open file 
try:
	f = open(project_folder + '/' +'small_output_file.txt', "r+") 
	# absolute file positioning
	f.seek(0) 
	# to erase all data 
	f.truncate()
	f.close()
except FileNotFoundError as e:
					print(f"Subor neexistuje v zlozke\n"f"{e}")
					# create empty file
					new_file = open(project_folder + '/' +'small_output_file.txt','w+')
					new_file.close()


for filename in os.listdir(working_folder):
	# loop through all filenames in the folder
	data_file = open(working_folder + '/' + filename, "r")
	# open the same file in the OLD folder
	try:
		old_file = open(old_folder + '/' + filename, "r")
	except FileNotFoundError as e:
					print(f"Subor neexistuje v OLD zlozke, vytvorim prazdny\n"f"{e}")
					# create empty file
					new_file = open(old_folder + '/' + filename,'w+')
					new_file.close()
					old_file = open(old_folder + '/' + filename, "r")
	# open output file where news domains will be appended
	new_domains = open(project_folder + '/' +'small_output_file.txt', "a+")

	# loop throug line of data file
	data_line = data_file.readline()
	
	# TODO ak je old_line hned prazdny

	# take each line and compare it with old_file
	while data_line != '':
		# Removing whitespaces
		data_line = data_line.rstrip()
		# loop through old file and check for data_line
		bExistOld = False
		old_file = open(old_folder + '/' + filename, "r")
		old_line = old_file.readline()
		while old_line != '':
			old_line = old_line.rstrip()
			# Compare the lines from both file
			if data_line == old_line:
				bExistOld = True
				break
			old_line = old_file.readline()
		if not bExistOld:
			# ak sa riadok nenachadzal v OLD
			new_domains.write("%s\n" %(data_line))
		old_file.close()
		# Read the next line from the file
		data_line = data_file.readline()
		
	


data_file.close()
old_file.close()


##https://realpython.com/working-with-files-in-python/

# file1 = open("C:\\Users\\Abinash\\Desktop\\Python Programs\\input1.txt", "r")
# file2 = open("C:\\Users\\Abinash\\Desktop\\Python Programs\\input2.txt", "r")

# i = 0

# for l1 in file1:
#     i += 1
#     for l2 in file2:
#         if l1 == l2:
#             print("Line ", i,": ")
#             print("Both the lines are same")
#         else:
#             print("Line ", i,": ")
#             print("File 1: ", l1)
#             print("File 2: ", l2)
#         break

# file1.close()
# file2.close()