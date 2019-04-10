import csv,sys,os

project_dir = "C:/Users/Admin/Desktop/MnoogleFinal1/mnoogle/mnoogle/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from jobs.models import Jobs


data2= csv.reader(open("C:/Users/Admin/Desktop/MnoogleFinal1/mnoogle/MnoogleData.csv",encoding='UTF8'),delimiter=",");

for row in data2:
	if row[0] != 'Job_Id':
		product = Jobs()
		product.Job_Id = row[0]
		product.Job= row[1]
		product.Company= row[2]
		# product.Address= row[3]
		# product.Deadline = row[4]
		product.URL = row[3]
		product.save()
		


		

		

		



