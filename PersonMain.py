# ---------------------------------

# File          : PersonMain.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 02/11/2021
# Modified Date : 02/11/2021
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

from Sample1 import PERSON

if __name__ == '__main__':

    Joe = PERSON("Joe Bloggs")
    Joe.display_person_details()

    Jane = PERSON("Jane Doe")
    Jane.name = "Jane Doe"
    Jane.display_person_details()
