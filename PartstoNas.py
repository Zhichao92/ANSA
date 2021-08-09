import ansa
from ansa import utils
from ansa import base
from ansa import constants

def PartToNas():
	print("Please select the output directory...")
	dir = utils.SelectOpenDir('')
	parts = base.CollectEntities(constants.NASTRAN, None, "ANSAPART")
	#to save files based on pids comment the above line and comment out below line
	#parts = base.CollectEntities(constants.NASTRAN, None, "PSHELL")
	base.All()
	for part in parts:
		base.Or(part)
		file_name = (part._name).replace("/", "_").replace(" ", "_")
		#print(file_name)
		base.OutputNastran(dir+file_name+".nas")
		#base.OutputStereoLithography(filename=dir+file_name+".stl", mode="visible", format = "ascii", output_exponent = "on")
		base.All()

PartToNas()
