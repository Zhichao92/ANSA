""" This script is used to calculate the thickness of each part in jt files which is available in current working folder. Output will be .csv files containing part name and corresponding thickness. Function _CheckandFixGeometry is taken from ansa user scripts
"""
import os
import ansa
import glob
from ansa import utils
from ansa import base
from ansa import constants

deck = constants.NASTRAN

def _CheckAndFixGeometry():	
	all_faces = base.CollectEntities(deck, None, "FACE")	
	length_of_faces_list= len(all_faces)
	if length_of_faces_list>0:
		print("\nChecking and fixing possible geometry errors...\n")
		options = ["CRACKS", "TRIPLE CONS", "OVERLAPS", "NEEDLE FACES", "COLLAPSED CONS"]
		fix = [1, 1, 1, 1, 1]
		ret = base.CheckAndFixGeometry(all_faces, options, fix)
		if ret == None:
			print("Fixing geometry completed successfully.\n")
		else:
			print("Total remaining errors:", len(ret['failed']),"\n")
	base.All()
	base.Topo()

def thickness_cad(filename):
	pids = base.CollectEntities(deck, None, "PSHELL")
	with open(filename, 'w') as thick:
		for pid in pids:
			faces = base.CollectEntities(deck, pid, "FACE")
			base.CollectEntities(deck, None, "FACE", filter_visible=True)
			is_solid_description = base.DetectSolidDescription(faces, estimate_thickness=True)
			print(pid._name, max(is_solid_description[0], key=is_solid_description[0].get))			
			thick.write(pid._name+', '+str(max(is_solid_description[0], key=is_solid_description[0].get))+'\n')
			
if __name__ == '__main__':
	jt_files = glob.glob('./*.jt')
	for root, dir, files in os.walk('.'):
		#print(root, dir, files)
		for file in files:			
			if file.endswith('.jt'):
				base.Open(os.path.join(root,file))
				_CheckAndFixGeometry()
				ansa_filename = base.DataBaseName()
				print(ansa_filename)
				csv_filename = ansa_filename+'.csv'
				print(csv_filename)
				thickness_cad(csv_filename)
