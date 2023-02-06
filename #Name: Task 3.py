#Name:                  Task 3.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    06-02-2023
#
#Purpose:
#
#The purpose of this program is to ask for a username that is more than 3 characters, but less than 20 characters.
#The username should also have a number in it, and should be able to loop if the username entered is invalid.

def greeting(userName):
    if len(userName) < 2:
        print("Username cannot be less than 2 characters.")
        return False
    if len(userName) > 20:
        print("Username cannot be longer than 20 characters.")
        return False
    
userNameInput = input("Please enter a username. Username should have at least 1 capital letter and 1 number: ")
