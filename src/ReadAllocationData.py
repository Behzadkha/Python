## @file ReadAllocationData.py
#  @author Behzad Khamneli 
#  @brief This code reads student information and returns the necessary files for allocation of students.
#  @date 1/18/2019

## @brief This function returns a list of dictionaries of student information.
#  @details ReadStdnts accepts a string corresponding to a file name. If there is something wrong with the file name, it returns an error message.
#  @param s Is a filename with the following format : macid firstname lastname gender gpa choice choice choice for every student (every line for a single students).
#  @return A dictionary with format : {'macid': string, 'fname': string, 'lname': string, 'gender': string, 'gpa': float, 'choices': [string, string, string]}.
def readStdnts(s):
	try:
		contents = []
		choices = []
		stdnList = []
		dicty = {}
		file = open(s, "r")
		for line in file.readlines():
			contents = (line.split()) 
			dicty["macid"] = str(contents[0])
			dicty["fname"] = str(contents[1])
			dicty["lname"] = str(contents[2])
			dicty["gender"] = str(contents[3])
			dicty["gpa"] = float(contents[4])
			choices.append(str(contents[5]))
			choices.append(str(contents[6]))
			choices.append(str(contents[7]))
			dicty["choices"] = choices
			choices = []
			stdnList.append(dicty)
			dicty = {}
		file.close()
		return stdnList
	except:
		return "File Error"
##  @brief This function filters students with freechoice.
#   @param s Is a filename with the following format: macid FreeChoice if a student has a free choice and format : macid no for student without a freechoice (on every line).
#   @details If there is an error in the file name, function readFreeChoice returns an error.
#   @return A list of string, where each entry in the list corresponds to the macid of a student with free choice.
def readFreeChoice(s):
	try:
		contents = []
		FreeChoiceStdn = []
		numberofStdn = 0
		file = open(s, "r")
		for line in file.readlines():
			contents.append(line.split())
			numberofStdn += 1

		for i in range (numberofStdn):
			if 'FreeChoice' in contents[i]:
				FreeChoiceStdn.extend(contents[i])
				FreeChoiceStdn.remove("FreeChoice")
		file.close()
		return FreeChoiceStdn
	except:
		return "File Error"
## @brief Takes a string and returns a dictionary.
#  @details This function separates department name and its capacity. department name goes to dept(list) and its capacity goes to capacity(list). 
#  @param s Is a filename with the following format : departmentName capacity on each line.
#  @return A dictionary with the following format : {'dept': integer}.
def readDeptCapacity(s):
	try:
		dept = []
		capacity = []
		dicty = {}
		file = open(s, "r")
		for line in file.readlines():
			dept, capacity = line.split()
			dicty[dept] = int(capacity)
		file.close()
		return dicty
	except:
		return "File Error"
