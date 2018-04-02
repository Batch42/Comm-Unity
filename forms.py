from django.forms import ModelForm
from CommUnity.models import Proposal

class SystemForm(ModelForm):
    class Meta:
        model = Proposal
        fields= ('text',)
