# Create a class named CollegeCourse that includes data fields that hold the
# department (for example, ENG), the course number (for example, 101), the
# credits (for example, 3), and the fee for the course (for example, $360). All of the
# fields are required as arguments to the constructor, except for the fee, which is
# calculated at $120 per credit hour. Include a display() method that displays
# the course data. Create a subclass named LabCourse that adds $50 to the course
# fee. Override the parent class display() method to indicate that the course is
# a lab course and to display all the data. Write an application named UseCourse
# that prompts the user for course information. If the user enters a class in any of
# the following departments, create a LabCourse: BIO, CHM, CIS, or PHY. If the
# user enters any other department, create a CollegeCourse that does not include
# the lab fee. Then display the course data. Save the files as CollegeCourse.java,
# LabCourse.java, and UseCourse.java.

from CollegeCourse import CollegeCourse


class LabCourse(CollegeCourse):

    def __init__(self, department, courseNumber  , credits):
        super().__init__(department, courseNumber  , credits)
        self._courseFee += 50

    def display(self):
        print(f"LabCourse = description: {self._department} ,  course Number  {self._courseNumber}, credits :  {self._credits} , course Fee : {self._courseFee} ")