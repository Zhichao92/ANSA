import os
import ansa
import collections
from ansa import constants
from ansa import base
from ansa import utils
deck = constants.RADTHERM

def ph_pidname(phnames):
	ph_pid_dict =collections.OrderedDict()
	group_list = base.CollectEntities(deck, None, 'ANSAGROUP', recursive = True)	
	for group in group_list:
		if group._name in phnames and group._name.startswith('PH-'):
			search_types = ['MULTI_LAYER_PART','SHELL_PART']
			pid_list = base.CollectEntities(deck, group, search_types, recursive=True)
			ph_pid_dict[group._name] = [i._name for i in pid_list]
	return ph_pid_dict
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

if __name__ == '__main__':
	part_list = base.CollectEntities(constants.NASTRAN, None, "ANSAPART", recursive=True , filter_visible=True)
	phname_list = []	
	for part in part_list:
		emp = []
		di_hierarchy = Part_DI(emp, part)
		if di_hierarchy[-1] not in phname_list:
			phname_list.append(di_hierarchy[-1])	
	ph_dict = ph_pidname(sorted(phname_list))	
	m = utils.SelectSaveFile("*.txt")
	with open(m[0], 'w') as f:
		for i in ph_dict:
			f.write(i+'\n')
			print(i)
			for j in ph_dict[i]:
				f.write('\t'+j.strip()+'\n')
				print('\t'+j.strip())
