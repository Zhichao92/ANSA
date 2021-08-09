import os
import ansa
import collections
import pprint
import time
import os
from ansa import base
from ansa import constants
from ansa import utils
deck = constants.NASTRAN
lock_names = []
base.SetViewButton({"SHADOW":"on", "VIEWMODE":"PID", "GRIDs":"off", "PERIMS":"off"})
file_path = base.DataBaseName()	
file_dir = file_path[0:file_path.rfind("/")+1]

def powerflow_export():	
	start = time.time()
	aero_group = collections.defaultdict(list)	
	pid_list = base.CollectEntities(deck, None, "PSHELL")
	global file_dir
	for i in pid_list:
		val_field = ('User/Aero/Aero_Group',)
		#vals = i.get_entity_values(deck, ('User/Aero/Aero_Group',))
		vals = base.GetEntityCardValues(deck, i, val_field)
		aero_group[vals['User/Aero/Aero_Group']].append(i)
	#pprint.pprint(aero_group)
	file_dir += "nas/"
	os.mkdir(file_dir)
	for k, v in aero_group.items():
		base.Or(v)
		base.SetViewAngles(f_key="F10")
		base.OutputNastran(file_dir+k+".nas", mode = "visible")
		#utils.PrintToFile(filename=file_dir+k+".png", image_format="PNG", red=255, green=255, blue=255, text_axes=False, transparent=False)
	end = time.time()
	print("Time taken to run: {} sec".format(end - start))
	

if __name__ == '__main__':	
	powerflow_export()
