from dataclasses import fields
from django import forms
from .models import Project, ProjectContribution

class ProjectContributionCreateForm(forms.ModelForm):
    
    class Meta:
        model = ProjectContribution
        fields =['amount','comments']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }  
        )
          

class ProjectCreateForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name','description','budget', 'category', 'project_image']
        widgets={
            'description':forms.Textarea(
                attrs={'rows':2,
                'placeholder':'description'
                
                }
            )
        }
        
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(
                {
            'placeholder': f'{str(field)}',
            'class': 'form-control'
            }
                
        )
        



            

    
    
