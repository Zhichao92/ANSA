# export all files in ANSA group to STL format
# Aero Team@ZhichaoZHAO 2020-12-26


import ansa
from ansa import base
from ansa import constants
from ansa import utils

@ ansa.session.defbutton('Output', 'stl', 'output a stl file for each ANSAGROUP')

def output_stl():
	dir = utils.SelectSaveDir("C:/")
	groups_list = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")	
	for group in groups_list:	
		base.Or(group)
		filename= dir + group._name +".stl"
		base.OutputStereoLithography(filename, mode="visible")
