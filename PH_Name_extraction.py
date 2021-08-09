# PYTHON script
# Script to collect the PH names from ansa file.
# Type the file name to be stored with extension .csv.
# If PH name is not in ansa group. It will simply write the topgroup.

import os
import ansa
from ansa import constants
from ansa import base
from ansa import utils

def Part_DI(heirarchy, partname):
	ret = base.GetPartDepth(partname)
	if ret["parent_part"] == None:
		heirarchy.append(partname._name)
		return heirarchy
	else:
		parent_name = base.GetEntityCardValues(constants.NASTRAN, ret["parent_part"], ('Name',))
	#heirarchy = []
	#print(parent_name['Name'])
	if parent_name['Name'].startswith('PH-'):
		heirarchy.append(parent_name['Name'])
		return heirarchy
	else:
		heirarchy.append(parent_name['Name'])
		return Part_DI(heirarchy, ret['parent_part'])

part_list = base.CollectEntities(constants.NASTRAN, None, "ANSAPART", recursive=True , filter_visible=True)
partname_list = []
m = utils.SelectSaveFile("*.csv")
file = open(m[0],'w')
for part in part_list:
	emp = []
	di_hierarchy = Part_DI(emp, part)
	if di_hierarchy[-1] not in partname_list:
		partname_list.append(di_hierarchy[-1])

partname_list.sort()
for i in partname_list:
	#print(i)
	file.write(i+'\n')
file.close()
