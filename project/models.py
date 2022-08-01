
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

class ProjectManager(models.Manager):
    def get_all_active_projects(self):
        return Project.objects.filter(is_active = True)
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_project_user")
    is_active = models.BooleanField(default=True)
    objects=ProjectManager()

    def get_active_contributions(self):
        rs = self.projectcontribution_set.filter(is_active = True)
        return rs

    def get_funded_amount(self):
        amount =self.get_active_contributions().aggregate(total=models.Sum('amount'))
        return amount.get('total',0)

    def get_funded_percentage(self):
        amount = self.get_funded_amount()
        
        if amount == None:
            amount = 0
        return round( amount/self.budget * 100,0)
    # Urls
    def get_detail_url(self,**kwargs):
        return reverse ('project:detail_view', kwargs={'id' :self.id})

class ProjectContribution(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    contributor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank = True)
    comments = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_user")
    is_active = models.BooleanField(default=True)



    