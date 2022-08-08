
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
        funded_amount =amount.get('total',0)
        if funded_amount==None:
            funded_amount=0
        return round(funded_amount,2)

    def get_funded_percentage(self):
        amount = self.get_funded_amount()
        return round( amount/self.budget * 100,0)
    # Urls
    def get_detail_url(self,**kwargs):
        return reverse ('project:detail_view', kwargs={'id' :self.id})
    def get_update_url(self,**kwargs):
        return reverse ('project:update_view', kwargs={'id' :self.id})
    def get_deactivate_url(self,**kwargs):
        return reverse ('project:deactivate_view')
    def get_contrib_url(self):
        return reverse('project:contrib_create_view')
    

class ProjectContribution(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    contributor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank = True)
    comments = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank = True, related_name="modified_user")
    is_active = models.BooleanField(default=True)



    