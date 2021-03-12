from django.db import models
from django.conf import settings
import uuid
# Create your models here.

class Community(models.Model):
    # 게시판을 분리해주는 모델
    name = models.CharField(max_length=50)
    rank = models.IntegerField()

class Post(models.Model):
    # 게시글 모델
    title = models.CharField(max_length=150)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='post')
    community = models.ForeignKey(Community,on_delete=models.CASCADE,related_name='post')
    category = models.CharField(max_length=150)
    views_count = models.PositiveIntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def update_counter(self):
        self.views_count = self.views_count + 1
        self.save()

class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment')

class CategoryGroup(models.Model):
    name = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=50)
    categorygroup = models.ForeignKey(CategoryGroup,on_delete=models.CASCADE,related_name='categorygroup')

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=30,null=True)
    latitude = models.FloatField(max_length=10,null=True)
    longitude = models.FloatField(max_length=10,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='location')
    rank = models.FloatField(default=0)

class Review(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='review')
    profile = models.URLField(max_length=200)
    rate = models.IntegerField()
    content = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    created_at = models.DateField()

class CourseTotal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='coursetotal')
    distance = models.FloatField(default=0)
    rank = models.IntegerField(null=True,blank=True)
    taste = models.IntegerField(default=0)
    tour = models.IntegerField(default=0)
    visited = models.BooleanField(default=False)
    activity = models.IntegerField(default=0)
    traveldate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        name = 'Coursetotal : '+str(self.pk)
        return name

class CourseDetail(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='coursedetail')
    coursetotal = models.ForeignKey(CourseTotal,on_delete=models.CASCADE,related_name='coursedetail')
    order = models.IntegerField()

class CoursePost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='coursepost')
    views_count = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    coursetotal = models.ForeignKey(CourseTotal, on_delete=models.CASCADE, related_name="coursepost")

    @property
    def update_counter(self):
        self.views_count = self.views_count + 1
        self.save()

def user_image_path(instance,filename):
    uuidstr = str(uuid.uuid1())
    total = uuidstr+filename
    return 'api/coursepost/{0}'.format(total)

class Image(models.Model):
    image = models.ImageField(upload_to=user_image_path)
    coursepost = models.ForeignKey(CoursePost, on_delete=models.CASCADE, related_name='image')