class student:
  def _init_(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
  def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda       student:student.cgpa,reverse=True)
    return sorted_students
  students=[student("Gayathri \t","fg24 \t",8.9),student("Ramya \t","aa24\t",9.9),student("Ramya  \t","po15\t",7.9)]
  sorted_students=sort_students(students)
  for student in sorted_students:
    print("Name:",student.name,"Roll_No:",student.roll_number,"CGPA:",students.cgpa)