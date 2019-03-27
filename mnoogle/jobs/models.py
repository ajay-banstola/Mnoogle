from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User

class Jobs(models.Model): 
	Title = models.CharField(max_length=250)   
	slug = models.SlugField(max_length=250,unique_for_date='Deadline')  
	Link = models.URLField(
		max_length=128, 
		db_index=True, 
		unique=True, 
		blank=True
	)  
	Description = models.TextField()
	Deadline = models.DateTimeField(default=timezone.now)   
	class Meta:      
		ordering = ('-Deadline',)
		index_together = (('id', 'slug'),)

	def __str__(self):     
		return self.Title
