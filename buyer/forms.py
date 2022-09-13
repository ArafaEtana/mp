from django.forms import ModelForm
from .models import postJob

class postJobForm(ModelForm):
    class Meta:
        model=postJob
        fields=('project_name','about_project')


