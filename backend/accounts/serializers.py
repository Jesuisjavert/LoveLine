from rest_framework import serializers
from accounts.models import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.validators import UniqueValidator
class UserSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(required=True,  validators=[UniqueValidator(queryset=User.objects.all())])
    # gender = serializers.CharField(max_length=2)
    age = serializers.IntegerField()
    # address = serializers.CharField(max_length=200)
    def get_cleaned_data(self):
        return {
            
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname' : self.validated_data.get('nickname',''),
            'gender' : self.validated_data.get('gender',''),
            'age' : self.validated_data.get('age','')
            
        }

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','nickname','age','gender')
        read_only_fields = ('email','nickname')
