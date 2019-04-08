from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User

class Jobs(models.Model):
	#Id = models.IntegerField()
	Job = models.CharField(max_length=250) 
	Company = models.TextField(max_length = 250, default="Not Available")
	Address = models.TextField(max_length = 250, default="Not available")
	Deadline = models.DateField(default=timezone.now)   
	flag = models.BooleanField(default=0)
	URL = models.URLField(
		max_length=128,
		db_index=True, 
		unique=False, 
		blank=True
	)  
	   
	class Meta:      
		ordering = ('-Deadline',)

	def __str__(self):     
		return self.Job
