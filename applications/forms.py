from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        # fields = ('course', 'name', 'mid_name', 'surname', 'birth_date', 'equity', 'disability', 'yes_specify', 'street_address', 'street_address2', 'city', 'zip_code', 'email', 'phone_number', 'whatsapp', 'work_phone', 'south_african_citizen', 'non_citizen_docs', 'highest_qualification', 'nk_name', 'nk_surname', 'nk_cellphone', 'nk_email', 'nk_home_tel', 'name_of_employer', 'comments', 'agreement' )
        fields = '__all__'
