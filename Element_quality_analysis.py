# PYTHON script
import os
import ansa
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import operator
import csv
import pandas as pd
from ansa import base
from ansa import constants
deck = constants.NASTRAN

def main():
	qual_dict = {}
	qual_n = ("SKEW","MINANGLE","MAXANGLE")
	ele = base.CollectEntities(deck, None, "SHELL", filter_visible=True)	
	for i in ele:
		qual_dict[i._id] = base.ElementQuality(i, qual_n)
	sorted_qual = sorted(qual_dict.items(), key = operator.itemgetter(1))
	qual_pd = pd.DataFrame(sorted_qual)
	qual_pd.to_csv('U:/TMP/4MARIES/Element/Angle_skewness.csv', index = False, header = False)
	#with open('U:/TMP/4MARIES/Element/Angle_skewness.csv', 'w') as csv_file:
		#writer = csv.writer(csv_file)	
		#writer.writerows(sorted_qual)
		#for key, value in qual_dict.items():
			#writer.writerow([key, value])
	print(sorted_qual[len(sorted_qual)-1])
	
	

if __name__ == '__main__':
	main()
