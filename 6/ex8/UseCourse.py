# a lab course and to display all the data. Write an application named UseCourse
# that prompts the user for course information. If the user enters a class in any of
# the following departments, create a LabCourse: BIO, CHM, CIS, or PHY. If the
# user enters any other department, create a CollegeCourse that does not include
# the lab fee. Then display the course data. Save the files as CollegeCourse.java,
# LabCourse.java, and UseCourse.java.

from CollegeCourse import CollegeCourse
from LabCourse import LabCourse
import re

def isCollegeCourse(department):
  find = re.search("BIO|CHM|CIS|PHY", department)
  return find


department = input("Enter your class BIO or CHM or CIS or PHY : ")
if (isCollegeCourse(department) == None):
  collegeCourse = CollegeCourse(department, 102, 10)
  collegeCourse.display()
else:
  collegeCourse = LabCourse(department, 103, 20)
  collegeCourse.display()

