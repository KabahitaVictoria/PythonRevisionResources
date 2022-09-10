class Student:
    def __init__(self, name, age, school): # blue print for student class with attributes of name, age and school
        self.name = name
        self.age = age
        self.school = school
        # student_keys = ['name', 'age', 'school']
        # student_values = [self.name, self.age, self.school]
        # student = dict(zip(student_keys, student_values))
        # print(student)
            

class Classroom(Student):  #classroom class inherits from parent class student
    ClassList = list()     # class attribute, list to which every instance will be appended
    def __init__(self, name, age, school, classroom_number, teacher):
        super().__init__(name, age, school)  # super function allows us to inherit rhe parent class attribute
        self.classroom_number = classroom_number
        self.teacher = teacher
        Classroom.ClassList.append(self) # adding a new student to the class; ADD 
    
    def __repr__(self):  # using the __repr__ magic method to customize how the instances will appear
        keys_list = ['room number', 'name', 'age', 'teacher']
        values_list = [self.classroom_number, self.name, self.age, self.teacher]
        student = dict(zip(keys_list, values_list))
        
        return f'{student}'
    
    @classmethod
    def delete_student(cls):   # class method to DELETE a student by name
        student_name = input("Enter name of student to be deleted: ")
        for x in Classroom.ClassList:
            if getattr(x, 'name') == student_name: # using the getattr() function to access the instance attribute
                Classroom.ClassList.remove(x)
        print(Classroom.ClassList)
    
    @classmethod
    def filter_by_age(cls):  # class method to FILTER out students of a specified age
        filter_list = list() # list to which the filtered students will be appended
        filter_age = int(input('Enter the filter age here: ')) # input function that accepts user input as an integer
        
        # for loop to iterate through each instance
        for x in Classroom.ClassList:
            if getattr(x, 'age') == filter_age:
                filter_list.append(getattr(x, 'name'))
        print(filter_list)
    
    @classmethod
    def class_list(cls):  # class method to PRINT the class list
        print(Classroom.ClassList)

# creating instances of the Classroom class   
student1 = Classroom('Victoria', 19, 'WITU', 1, 'Miriam')        
student2 = Classroom('Mary', 20, 'WITU', 1 , 'Miriam')  
student3 = Classroom('Sera', 19, 'WITU', 2, 'Effie')

# Classroom.delete_student()
# Classroom.filter_by_age()
Classroom.class_list()

  
    