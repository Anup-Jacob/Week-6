# ---------------------------------

# File          : MODULE.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   : A Class named MODULE to be called from main program with module details
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

class MODULE:

    def __init__(self, mod_num, mod_name):
        self._mod_name = mod_name
        self._mod_num = mod_num

    @property
    def mod_details(self):
        return self._mod_name, self._mod_num

    @mod_details.setter
    def mod_details(self, value):
        print('Inside mod_details')
        self._mod_name = value

    @property
    def display_mod_details(self):
        print("Module name: {}".format(self._mod_name))
        print("Module number: {}".format(self._mod_num))
