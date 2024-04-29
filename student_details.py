# Write a program to create a class with name 'Box' which should contain 7 data members. 1. name 2. rollNo 3. dbmsMarks 4. pythonMarks 5. cMarks 6. osMarks 7. cnMarks
# Then create 3 objects with below data, and print them in same line in space seperated manner.
# Student1: name: "Harika" rollNo: "5A1" dbmsMarks: 78 pythonMarks: 67 cMarks: 77 osMarks: 89 cnMarks:46
# Student2: name: "Swapna" rollNo: "5A2" dbmsMarks: 38 pythonMarks: 65 cMarks: 97 osMarks: 59 cnMarks:41
# Student3: name: "Sushma" rollNo: "5A3" dbmsMarks: 88 pythonMarks: 95 cMarks: 47 osMarks: 89 cnMarks:31

# Sample Output 
# Harika 5A1 78 67 77 89 46
# Swapna 5A2 38 65 97 59 41
# Sushma 5A3 88 95 47 89 31

class Box:
  def __init__(self, name, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
    self.name = name
    self.rollNo = rollNo
    self.dbmsMarks = dbmsMarks
    self.pythonMarks = pythonMarks
    self.cMarks = cMarks        
    self.osMarks = osMarks
    self.cnMarks = cnMarks

# Object creation with provided data
student1 = Box("Harika", "5A1", 78, 67, 77, 89, 46)
student2 = Box("Swapna", "5A2", 38, 65, 97, 59, 41)
student3 = Box("Sushma", "5A3", 88, 95, 47, 89, 31)

# Printing the data in the required format
print(student1.name, student1.rollNo, student1.dbmsMarks, student1.pythonMarks, student1.cMarks, student1.osMarks, student1.cnMarks)
print(student2.name, student2.rollNo, student2.dbmsMarks, student2.pythonMarks, student2.cMarks, student2.osMarks, student2.cnMarks)
print(student3.name, student3.rollNo, student3.dbmsMarks, student3.pythonMarks, student3.cMarks, student3.osMarks, student3.cnMarks)

