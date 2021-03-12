from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from allauth.account.models import EmailAddress
from django.conf import settings
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True    
    
    def _create_user(self, email, password=None, **kwargs):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        EmailAddress.objects.create(user=user,email=user.email,verified=True,primary=True)     
        return user
    def create_user(self, email, password, **kwargs):
        """
        일반 유저 생성
        """
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)     
    def create_superuser(self, email, password, **kwargs):
        """
        관리자 유저 생성
        """
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_staff',True)
        return self._create_user(email, password, **kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    username = None
    objects = UserManager()
    email = models.EmailField(
        verbose_name = '이메일',
        max_length = 255,
        unique = True,
    )
    nickname = models.CharField(
        max_length = 15,
        null = False,
        unique = True,
    )
    gender = models.CharField(
        verbose_name = '성별',
        max_length = 2,
        null = True,
    )
    age = models.IntegerField(
        verbose_name= '나이',
        null= True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joind = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

def user_image_path(instance,filename):
    uuidstr = str(uuid.uuid1())
    total = uuidstr+filename
    return 'api/profile/{0}'.format(total)

class UserProfile(models.Model):
    image = models.ImageField(upload_to=user_image_path)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='userprofile')