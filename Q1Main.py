# ---------------------------------

# File          : Q1Main.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   : A main program to check the functionality of annotation and call classes STUDENT, ROOM and MODULE
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

from STUDENT import STUDENT
from ROOM import ROOM
from MODULE import MODULE

if __name__ == '__main__':
    print('\nFirst Step')
    StudName = STUDENT('Anup Jacob', 'L0013455')
    #StudName.name = 'Anup Jacob'
    #StudName.roll = 'L0013455'
    #StudName.stud_details()
    print(callable(StudName.display_person_details()))

    print('\nSecond')
    ModName = MODULE(1, 'DevOps Server Admin')
    print(ModName.display_mod_details())

    print('\nThird')
    RoomDet = ROOM(4209)
    print(RoomDet.display_class_details())

    print("Thank you for using my application")


