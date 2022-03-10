import os

project_folder = os.path.join(os.getcwd())
working_folder = os.path.join(os.getcwd(), 'data_test')		#switch from test to DATA on production
old_folder = os.path.join(os.getcwd(), 'OLD_test')

# TODO remove old newDomains file
# open file 
f = open(project_folder + '\\' +'output_file.txt', "r+") 
# absolute file positioning
f.seek(0) 
# to erase all data 
f.truncate()
f.close()

for filename in os.listdir(working_folder):
	# loop through all filenames in the folder
	data_file = open(working_folder + '\\' + filename, "r")
	# open the same file in the OLD folder
	old_file = open(old_folder + '\\' + filename, "r")
	# open output file where news domains will be appended
	new_domains = open(project_folder + '\\' +'output_file.txt', "a+")

	# TODO
	# IF OLD file doesnt exists -> raise exception

	# Loop through data_file line by line and compare it with OLD
	# for data_line in data_file:
	# 	for old_line in old_file:
	# 		if data_line == old_line:
	# 			new_domains.write("%s\n" %(data_line))

	# common lines in both files
	# with open(working_folder + '\\' + filename, "r") as file1:
	# 	with open(old_folder + '\\' + filename, "r") as file2:
	# 		same = set(file1).intersection(file2)

	# ###############################################
	# Difference Lines in Both Files
	# data_line = data_file.readline()
	# old_line = old_file.readline()
	# # Use as a COunter
	# line_no = 1

	# while data_line != '' or old_line != '':
	# 	 # Removing whitespaces
	# 	data_line = data_line.rstrip()
	# 	old_line = old_line.rstrip()
	
	# 	# Compare the lines from both file
	# 	if data_line != old_line:
	# 		new_domains.write("%s\n" %(data_line))
	# 	# Read the next line from the file
	# 	data_line = data_file.readline()
	# 	old_line = old_file.readline()
	# 	line_no += 1

	# different lines in both files
	with open(working_folder + '\\' + filename, "r") as file1:
		with open(old_folder + '\\' + filename, "r") as file2:
			difference = set(file1).difference(file2)
	
	for diff_line in difference:
		new_domains.write( diff_line)


# # common lines 
# print("Common Lines in Both Files")  
# for line in same:
#     print(line, end='')

# # differentlines 
# print("Different Lines in Both Files")  
# for line in difference:
#     print(line, end='')

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