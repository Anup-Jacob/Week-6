# ---------------------------------

# File          : Sample2.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

from random import randint

Lecturers = ["Pat", "Evelyn", "Priyank"]

class LECTURER:
 def __init__(self, name):
    self._lect_name = name

 @property
 def lnumber(self):
    """This is a getter function for lnumber"""
    return self._lnumber

 @property
 def lect_name(self):
    """The property (getter) must be created before a setter can be made"""
    return self._lect_name

 @lect_name.setter
 def lect_name(self, val):
    """restricting values to a predefined set"""
    if val not in Lecturers:
        raise ValueError("Invalid lecturer")
        self._lect_name = val

 @lect_name.deleter
 def lect_name(self):
    """The deleter is called when del is called"""
    print("del called")
    del self._lect_name

 @staticmethod
 def random_lecturer():
    return Lecturers[randint(0, 2)]


