import csv,sys,os

project_dir = "C:/Users/Admin/Desktop/MnoogleFinal1/mnoogle/mnoogle/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from jobs.models import Jobs


data2= csv.reader(open("C:/Users/Admin/Desktop/MnoogleFinal1/mnoogle/MnoogleData.csv",encoding='UTF8'),delimiter=",");


for row in data2:
	if row[0] != 'Job':
		product = Jobs()
		product.Job= row[0]
		product.Company= row[1]
		product.Address= row[2]
		product.Deadline = row[3]
		product.URL = row[4]
		product.save()
		


		

		

		



