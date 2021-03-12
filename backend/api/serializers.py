from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from accounts.models import UserProfile
import datetime
User = get_user_model()
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name',read_only=True)
    categorygroup = serializers.CharField(source='category.categorygroup.name')
    class Meta:
        model = Location
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.nickname',required=False)
    comment_count = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)
    community_id = serializers.IntegerField(source='community.id',required=False)

    def get_comment_count(self,post):
        return post.comment.count()

    def get_like_count(self,post):
        return post.like_users.count()

    class Meta:
        model = Post
        exclude = ('user','community','like_users')

class CourseDetailShowSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False)
    class Meta:
        model = CourseDetail
        exclude =('coursetotal',)


class CourseSerializer(serializers.ModelSerializer):
    ispastday = serializers.SerializerMethodField(read_only=True)
    coursedetail = CourseDetailShowSerializer(required=False,many=True)
    def get_ispastday(self,CourseTotal):
        origin = datetime.datetime.strptime(str(CourseTotal.traveldate),'%Y-%m-%d')
        temp = origin> datetime.datetime.today()
        return temp
    class Meta:
        model = CourseTotal
        exclude = ('user',)

class CourseDetailSerializer(serializers.ModelSerializer):
    coursetotal = serializers.CharField(required=False)
    Location = LocationSerializer(source='location')
    class Meta:
        model = CourseDetail
        fields = '__all__'

class CourseTotalSerializer(serializers.ModelSerializer):
    coursedetail = CourseDetailSerializer(many=True, read_only=True)
    class Meta:
        model = CourseTotal
        fields = '__all__'

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('nickname','email','age','gender')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    post = PostSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    image_url =  serializers.SerializerMethodField(read_only=True)
    def get_image_url(self,userprofile):

        userimage = str(userprofile.image)

        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+userimage
    class Meta:
        model = UserProfile
        exclude = ('user',)



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

class CoursePostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.nickname', read_only=True, required =False)
    courseTotal = CourseTotalSerializer(source='coursetotal', read_only=True, required =False)
    image = ImageSerializer(many=True, read_only=True, required =False)
    class Meta:
        model = CoursePost
        exclude = ('user',)

class MypageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'