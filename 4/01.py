# Болібрук Влад

9.1
# (The Rectangle class) Following the example of the Circle class in Section 9.2,
# design a class named Rectangle to represent a rectangle. The class contains:
# ■ Two double data fields named width and height that specify the width and
# height of the rectangle. The default values are 1 for both width and height.
# ■ A no-arg constructor that creates a default rectangle.
# ■ A constructor that creates a rectangle with the specified width and height.
# ■ A method named getArea() that returns the area of this rectangle.
# ■ A method named getPerimeter() that returns the perimeter.

# Draw the UML diagram for the class then implement the class. Write a test pro-
# gram that creates two Rectangle objects—one with width 4 and height 40, and

# three objectives

# M09_LIAN2079_12_GE_C09.indd 384 09/06/2021 13:38

# Programming Exercises 385

# the other with width 3.5 and height 35.9. Display the width, height, area, and
# perimeter of each rectangle in this order.


9.7

# (The Account class) Design a class named Account that contains:
# ■ A private int data field named id for the account (default 0).
# ■ A private double data field named balance for the account (default 0).

# M09_LIAN2079_12_GE_C09.indd 385 09/06/2021 13:38

# 386 Chapter 9 Objects and Classes

# ■ A private double data field named annualInterestRate that stores the current
# interest rate (default 0). Assume that all accounts have the same interest rate.
# ■ A private Date data field named dateCreated that stores the date when the
# account was created.
# ■ A no-arg constructor that creates a default account.
# ■ A constructor that creates an account with the specified id and initial balance.
# ■ The accessor and mutator methods for id, balance, and annualInterestRate.
# ■ The accessor method for dateCreated.
# ■ A method named getMonthlyInterestRate() that returns the monthly
# interest rate.
# ■ A method named getMonthlyInterest() that returns the monthly interest.
# ■ A method named withdraw that withdraws a specified amount from the
# account.
# ■ A method named deposit that deposits a specified amount to the account.
# Draw the UML diagram for the class then implement the class. (Hint: The method
# getMonthlyInterest() is to return monthly interest, not the interest rate.

# Monthly interest is balance * monthlyInterestRate. monthlyIntere-
# stRate is annualInterestRate / 12. Note annualInterestRate is a per-
# centage, for example 4.5%. You need to divide it by 100.)

# Write a test program that creates an Account object with an account ID of 1122,
# a balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw
# method to withdraw $2,500, use the deposit method to deposit $3,000, and print
# the balance, the monthly interest, and the date when this account was created.

9.8

# (The Fan class) Design a class named Fan to represent a fan. The class contains:
# ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3
# to denote the fan speed.
# ■ A private int data field named speed that specifies the speed of the fan (the
# default is SLOW).
# ■ A private boolean data field named on that specifies whether the fan is on (the
# default is false).
# ■ A private double data field named radius that specifies the radius of the fan
# (the default is 5).
# ■ A string data field named color that specifies the color of the fan (the default
# is blue).
# ■ The accessor and mutator methods for all four data fields.
# ■ A no-arg constructor that creates a default fan.
# ■ A method named toString() that returns a string description for the fan. If

# the fan is on, the method returns the fan speed, color, and radius in one com-
# bined string. If the fan is not on, the method returns the fan color and radius

# along with the string “fan is off” in one combined string.

# Draw the UML diagram for the class then implement the class. Write a test program
# that creates two Fan objects. Assign maximum speed, radius 10, color yellow,
# and turn it on to the first object. Assign medium speed, radius 5, color blue, and
# turn it off to the second object. Display the objects by invoking their toString
# method.


9.10

# (Algebra: quadratic equations) Design a class named QuadraticEquation for
# a quadratic equation ax2 + bx + c = 0. The class contains:
# ■ Private data fields a, b, and c that represent three coefficients.
# ■ A constructor with the arguments for a, b, and c.
# ■ Three getter methods for a, b, and c.
# ■ A method named getDiscriminant() that returns the discriminant, which
# is b2 - 4ac.
# ■ The methods named getRoot1() and getRoot2() for returning two roots
# of the equation
# r1 = -b + 2b2 - 4ac
# 2a

# and r2 = -b - 2b2 - 4ac
# 2a

# These methods are useful only if the discriminant is nonnegative. Let these methods
# return 0 if the discriminant is negative.

# Draw the UML diagram for the class then implement the class. Write a test pro-
# gram that prompts the user to enter values for a, b, and c and displays the result

# based on the discriminant. If the discriminant is positive, display the two roots. If
# the discriminant is 0, display the one root. Otherwise, display “The equation has
# no roots.” See Programming Exercise 3.1 for sample runs.