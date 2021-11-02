# ---------------------------------

# File          : Sample1.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

class PERSON:
    def __init__(self, name):
        self._name = name # cannot be accessed outside of class
        print("Init ran successfully")

    @property
    def name(self):
        print('In property')
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        print('In Setter')

    @property
    def display_person_details(self):
        print("Name: ".format(self._name))


