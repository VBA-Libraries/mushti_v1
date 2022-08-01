from dataclasses import fields
from django import forms
from .models import Project, ProjectContribution

class ProjectCreateForm(forms.ModelForm):
    
    
    class Meta:
        model = Project
        fields = ['name','description','budget']
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

class ProjectContributionCreateForm(forms.ModelForm):

    class Meta:
        model = ProjectContribution
        fields = ['contributor','amount','comments']
        widgets={
                'comments':forms.Textarea(
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
    


            

    
    
