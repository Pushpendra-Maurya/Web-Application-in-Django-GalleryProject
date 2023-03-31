from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User

from .models import ImageModel

from django import forms


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter Your First Password', widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Your First Password'}))
    
    password2 = forms.CharField(label='Enter Your Re-Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Re- Password '}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']

        labels = {
            'first_name':'Enter Your First Name ',
            'last_name':'Enter Your Last Name ',
            'username':'Enter Your  UserName ',
            'email':'Enter Your  Email '
            
        }
        widgets =  {
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name '}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name '}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your UserName '}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email '})

        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Your UserName ', widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter Your  Username'}))
    password = forms.CharField(label='Enter Your  Password', widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Your  Password'}))
    
    class Meta:
        model = User
        fields = User 
        fields = ['username','password']




class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title','cat','image','desc']

        labels = {
            'title':'Enter Your Title',
            'cat':'Enter Your Categories',
            'image':'Enter Your Image',
            'desc':'Enter Your Description'

        }

        widgets =  {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Title'}),
            'cat':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your description '})

        }