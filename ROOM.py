# ---------------------------------

# File          : ROOM.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   : A Class named ROOM to be called from main program with class details
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

class ROOM:

    def __init__(self, class_num):
        self._class_num = class_num

    @property
    def class_details(self):
        return self._class_num

    @class_details.setter
    def class_details(self, class_num):
        print('Inside class details')
        self._class_num = class_num
        # class_no: int = 4209

    @property
    def display_class_details(self):
        print("Class number: {}".format(self._class_num))
