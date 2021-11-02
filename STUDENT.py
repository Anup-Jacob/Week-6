# ---------------------------------

# File          : STUDENT.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 01/11/2021
# Modified Date : 01/11/2021
# Description   : A Class named STUDENT to be called from main program with person details
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

class STUDENT:

    def __init__(self, name, roll):
        print("Inside Init")
        self._name = name
        self._roll = roll
        print(self._name,self._roll)

    @property
    def stud_details(self):
        print('Inside property')
        print(self._name,self._roll)
        return self._name, self._roll

    @stud_details.setter
    def stud_details(self, name, roll):
        print("Inside stud_details")
        self._name = name
        self._roll = roll

    @property
    def display_person_details(self):
        print("Name: ".format(self._name))
        print("Roll Number: ".format(self._roll))







