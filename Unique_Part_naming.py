# PYTHON script
import os
import ansa
import sys
import re
import collections
from ansa import base
from ansa import constants
from ansa import utils
from ansa import session
current_dir = os.path.dirname(os.path.realpath(__file__))
if current_dir not in sys.path:
	sys.path.append(current_dir)
import xlrd


@session.defbutton('TSE', 'Pid_Check_Correction', 'Check the PIDs with unique_name_list and print the list of incorrect PID names in ansa info window. This script automatically correct the PID character case according to naming procedure.')

def Pid_Check_Correction():
	wrong_pids = {}	
	pid_list = base.CollectEntities(constants.FLUENT, None, "SHELL_PROPERTY")
	m = utils.SelectOpenFile(0, 'Excel files (*.xlsx)')
	excel_names = _excel_name_extract(m[0])
	unique_name_list = _remove_no_name(excel_names)
	unique_name_lower = list(map(lambda x:x.lower(), unique_name_list))

			
	for pid in pid_list:	
		if _remove_no_name([pid._name])[0] not in unique_name_list and _remove_no_name([pid._name])[0].lower() not in unique_name_lower:
			wrong_pids[pid._id] = pid._name
		elif _remove_no_name([pid._name])[0].lower() in unique_name_lower:
			_character_case(pid, excel_names)	
	if len(wrong_pids) == 0:
		print("\nAll PIDs are named as per convention\n")
	else:
		print("\nBelow pids are not named as per convention")
		print("------------------------------------------------------")
		for key, values in wrong_pids.items():
			print(key, values)
		print("------------------------------------------------------")


def _excel_name_extract(xl_file):
	#This function extract the unique names from the excel file and return the list of unique names
	unique_names = []
	xl_workbook = xlrd.open_workbook(xl_file)
	sheet_names = xl_workbook.sheet_names()	
	xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
	total_rows = xl_sheet.nrows
	#print(total_rows)
	for i in range(4, total_rows):
		cell = xl_sheet.cell(i, 2)
		if cell.value != '':
			unique_names.append(cell.value.strip())
	#print(type(unique_names[1]))
	return unique_names

def _remove_no_name(names_list):
	"""
	This function remove the number and preceding '_' from names. Example test_1 will return test
	Take a name list as input and return corrected name list as output.
	This function returns list of removed names
	"""
	name_wo_number = []
	for j in names_list:
		pattern = re.compile(".\d+")
		num = pattern.search(j)				
		name_wo_number.append(pattern.sub('',j.strip()))
	return name_wo_number

def _character_case(pid, unique_name_list):
	#This function corrects the character case of pid according to unique name list
	for i in unique_name_list:
		if _remove_no_name([pid._name])[0].lower() == _remove_no_name([i])[0].lower():
			check_number = map(lambda x:x.isnumeric(), pid._name)			
			if any(list(check_number)):
				pattern = re.compile("\d+")
				no_pid = re.search("\d+", pid._name)
				corrected_pid = pattern.sub(no_pid.group(), i)
				base.SetEntityCardValues(constants.FLUENT, pid, {'Name':corrected_pid})
			else:
				values = {'Name':i}
				base.SetEntityCardValues(constants.FLUENT, pid, values)

Pid_Check_Correction()
