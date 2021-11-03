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
    #print('\nCalling STUDENT class')
    StudName = STUDENT('Anup Jacob', 'L0013455')
    callable(StudName.display_person_details)

    print("")

    ModName1 = MODULE(1, 'DevOps Server Admin')
    RoomNum2 = ROOM(3569)
    RoomNum1 = ROOM(4209)
    ModName2 = MODULE(2, 'DevOps Software Engineering')

    # Details of Module 1 and class
    callable(ModName1.display_mod_details)
    callable(RoomNum1.display_class_details)

    print("")

    # Details of Module 2 and class
    callable(ModName2.display_mod_details)
    callable(RoomNum2.display_class_details)

    print("\nThank you for using my application")


