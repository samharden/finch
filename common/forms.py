from django import forms
from common.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}

        issue_detail = forms.CharField(widget=forms.Textarea)
        self.fields['website'].required = False

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'state',
            'county',
            'website',

        )

    def clean_name(self):
        name = self.cleaned_data['username']

        user = User.objects.filter(name__iexact=name).exclude(id=self.instance.id)
