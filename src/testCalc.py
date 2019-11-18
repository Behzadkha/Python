## @file testCalc.py
#  @Behzad Khamneli
#  @brief testCalc.py tests the functions in CalcModule.py
#  @date 1/17/2019
import ReadAllocationData
import CalcModule

## @brief Checks if the output is the same as the expected output.
#  @details This function passes data from ReadAllocationData to function sort in CalcModule as a parameter.
def test_sort():
	answer = CalcModule.sort(ReadAllocationData.readStdnts("src/test.txt")) 
	assert answer == [{'macid': 'mithj', 'fname': 'mith', 'lname': 'jones', 'gender': 'male', 'gpa': 12.0, 'choices': ['civil', 'software', 'material']},
	{'macid': 'khamnelb', 'fname': 'behzad', 'lname': 'khamneli', 'gender': 'male', 'gpa': 9.0, 'choices': ['software', 'mechanical', 'chemical']},
	{'macid': 'jackm', 'fname': 'Jack', 'lname': 'mate', 'gender': 'male', 'gpa': 6.0, 'choices': ['mechanical', 'materials', 'electrical']},
	{'macid': 'loganh', 'fname': 'logan', 'lname': 'hall', 'gender': 'male', 'gpa': 6.0, 'choices': ['mechanical', 'software', 'civil']}, 
	{'macid': 'sophias', 'fname': 'sophia', 'lname': 'smith', 'gender': 'female', 'gpa': 4.0, 'choices': ['software', 'electrical', 'engphys']}]
	
	answer2 = CalcModule.sort(ReadAllocationData.readStdnts(" "))
	assert answer2 == "File Error"
## @brief Checks if the output is the same as the expected output.
#  @details This function passes data from ReadAllocationData to function average in CalcModule as a parameter.
def test_average():
	answer = CalcModule.average(ReadAllocationData.readStdnts("src/test.txt"), "male")
	assert answer == 8.25

	answer1 = CalcModule.average(ReadAllocationData.readStdnts("src/test.txt"), "female") 
	assert answer1 == 4.0

	answer2 = CalcModule.average(ReadAllocationData.readStdnts(" "), "male")
	assert answer2 == "File Error"
	
	answer3 = CalcModule.average(ReadAllocationData.readStdnts("src/test.txt"), "Jack")
	assert answer3 == "g can be either male or female"
## @brief Checks if the output is the same as the expected output.
#  @details This function passes data from ReadAllocationData to function allocate in CalcModule as a parameter.
def test_allocate():
	answer = CalcModule.allocate(ReadAllocationData.readStdnts("src/test.txt"), ReadAllocationData.readFreeChoice("src/free.txt"), ReadAllocationData.readDeptCapacity("src/capa.txt"))
	assert answer == {'civil': [{'macid': 'mithj', 'fname': 'mith', 'lname': 'jones', 'gender': 'male', 'gpa': 12.0, 'choices': ['civil', 'software', 'material']}], 
	'chemical': [], 'electrical': [], 
	'mechanical': [{'macid': 'jackm', 'fname': 'Jack', 'lname': 'mate', 'gender': 'male', 'gpa': 6.0, 'choices': ['mechanical', 'materials', 'electrical']}, 
	{'macid': 'loganh', 'fname': 'logan', 'lname': 'hall', 'gender': 'male', 'gpa': 6.0, 'choices': ['mechanical', 'software', 'civil']}], 
	'software': [{'macid': 'khamnelb', 'fname': 'behzad', 'lname': 'khamneli', 'gender': 'male', 'gpa': 9.0, 'choices': ['software', 'mechanical', 'chemical']},
	{'macid': 'sophias', 'fname': 'sophia', 'lname': 'smith', 'gender': 'female', 'gpa': 4.0, 'choices': ['software', 'electrical', 'engphys']}], 'materials': [], 
	'engphys': []}

	answer2 = CalcModule.allocate(ReadAllocationData.readStdnts(" "), ReadAllocationData.readFreeChoice(" "), ReadAllocationData.readDeptCapacity(" "))
	assert answer2 == "File Error"
