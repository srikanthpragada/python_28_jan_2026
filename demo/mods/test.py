import strfuns as sf
from strfuns import count_spaces

print(count_spaces.__doc__)
print(help(count_spaces))

import sys
sys.path.append(r"c:\classroom\jan28\demo\lib")
print(sys.path)

print(count_spaces('How are you'))
print(sf.find_first_space_pos('How are you'))
print(sf.NEWLINE)

import numfuns as nf
print(nf.iseven(10))
