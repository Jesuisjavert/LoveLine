from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, SAFE_METHODS,IsAuthenticated
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
from django.db.models import F
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
import datetime
import time

# 페이지네이션
class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page_size"
    max_page_size = 1

class IsLogined(BasePermission):
    # get일때에는 전체 유저,
    # post일때에는 로그인 유저
     def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False

class CommunityView(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsLogined]

class CommunityPostView(generics.ListCreateAPIView):
    queryset = Community
    serializer_class = PostSerializer
    permission_classes = [IsLogined]
    pagination_class = ResultsSetPagination

    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk).post.all()
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer_class = PostSerializer(queryset,many=True)
        for k in serializer_class.data:
            check = Post.objects.get(pk=k['id']).like_users.filter(id=request.user.id).exists()
            k['likeusercheck'] = check
        return Response(serializer_class.data)

    def post(self, request, pk, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(community_id=pk,user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostView(generics.ListCreateAPIView):
    queryset = Community
    serializer_class = PostSerializer
    permission_classes = [IsLogined]

    def get_object(self, community_pk, post_pk):
        try:
            return Community.objects.get(pk=community_pk).post.get(pk=post_pk)
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, community_pk, post_pk):
        queryset = self.get_object(community_pk, post_pk)
        queryset.update_counter
        serializer_class = PostSerializer(queryset)
        return Response(serializer_class.data)

    def put(self, request, community_pk, post_pk):
        queryset = self.get_object(community_pk, post_pk)
        serializer_class = PostSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, community_pk, post_pk):
        queryset = self.get_object(community_pk, post_pk)
        try:
            queryset.delete()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CommentView(generics.ListCreateAPIView):
    queryset = Comment
    serializer_class = CommentSerializer
    # permission_classes = [IsLogined]

    def get_object(self, post_pk):
        try:
            return Post.objects.get(pk=post_pk).comment.all()
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, post_pk):
        queryset = self.get_object(post_pk)
        serializer_class = CommentSerializer(queryset, many=True)
        return Response(serializer_class.data)
   
    def post(self, request, post_pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post_id=post_pk,user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    permission_classes = [IsLogined]
    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def delete(self, request, post_pk, comment_pk):
        comment = self.get_object(comment_pk)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

class courseView(generics.ListCreateAPIView):
    queryset = CourseTotal.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsLogined]
    def get(self,request):
        coursetotal = request.user.coursetotal.all()
        serializer = CourseSerializer(coursetotal,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            courseTotal = serializer.save(user_id=request.user.id)
        for order,course in enumerate(request.data['courselist']):
            CourseDetail.objects.create(location_id=course['id'],order=order+1,coursetotal_id=courseTotal.id)
        coursetotal = CourseTotal.objects.get(id=courseTotal.id)
        returndata = CourseTotalSerializer(coursetotal)
        return Response(returndata.data)

class courseDetailView(generics.RetrieveUpdateAPIView):
    queryset = CourseTotalSerializer
    serializer_class = CourseTotalSerializer
    permission_classes = [IsLogined]

    def get_object(self, pk):
        try:
            return CourseTotal.objects.get(pk=pk)
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer_class = CourseTotalSerializer(queryset)
        return Response(serializer_class.data)
   
    def post(self, request, pk, format=None):
        serializer = CourseDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(coursetotal_id=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 
    def put(self, request, pk):
        queryset = self.get_object(pk)
        if queryset.user == request.user:
            origin = datetime.datetime.strptime(str(queryset.traveldate),'%Y-%m-%d')
            temp = origin < datetime.datetime.today()
            if temp:
                queryset.visited = True
                queryset.save()
                serializer = CourseTotalSerializer(queryset)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class accountView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        User = get_user_model()
        loginuser = User.objects.get(id=request.user.id)
        serializers = UserSerializer(loginuser)
        return Response(serializers.data)

class location(APIView):
    def get(self,request):
        start_time = time.time()
        _lat = float(request.query_params.get('latitude',35.1874726))
        _lon = float(request.query_params.get('longitude',126.900115))
        inputcate = request.query_params.get('category','한식')
        catelist = list(inputcate.split(','))
        for ind,k in enumerate(catelist):
            if catelist[ind] == '음식점':
                catelist.pop(ind)
                catelist.extend(['중식','술집','한식','카페','분식','세계음식','양식','뷔페','일식'])
        zoom = int(request.query_params.get('zoomlevel',14))
        searchrange = (15.9 *(2**(19-zoom))*2)/1000
        dlat = Radians(F('latitude') - _lat)
        dlong = Radians(F('longitude') - _lon)
        a = (Power(Sin(dlat/2), 2) + Cos(Radians(_lat)) 
            * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
        )

        c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
        d = 6371 * c
        te = Location.objects.select_related('category').annotate(distance=d).filter(distance__lt=searchrange).filter(category__name__in=catelist).order_by('rank')
        if (te.count()>50):
            te = te[:50]
        serializer = LocationSerializer(te,many=True)
        return Response(serializer.data)

class Profile(APIView):
    def get(self,request):
        users = User.objects.get(id=request.user.id)
        if users.userprofile.all().exists():
            userspro = users.userprofile.all().first()
            serializers = UserProfileSerializer(userspro)
            return Response(serializers.data)
        else:
            return Response({'data':False})
    def post(self,request):
        loginuser = User.objects.get(id=request.user.id)
        if loginuser.userprofile.all().exists():
            loginuser.userprofile.all().delete()
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user=request.user)
            return Response(serializers.data)
        
        return Response(serializer.data)

from django.db.models import FloatField, ExpressionWrapper, F,Prefetch,Count
from django.db.models.functions import Sqrt,Power

class recommandcourse(APIView):
    def get(self,request):
        _flag = request.query_params.get('flag','up')
        _cnt = int(request.query_params.get('cnt',1))
        _order = int(request.query_params.get('order',2))
        _taste = int(request.query_params.get('ta',3))
        _activity = int(request.query_params.get('ac',3))
        _tour = int(request.query_params.get('to',3))
        print(_order)
        imk = [_taste,_tour,_activity]
        ima = F('taste')*imk[0]+F('tour')*imk[1]+F('activity')*imk[2]
        imb = (Sqrt(Power(F('taste'),2)+Power(F('tour'),2) + Power(F('activity'),2)) *((imk[0]**2+imk[1]**2+imk[2]**2)**0.5))
        imc = ima/imb
        if _flag == 'up':
            imresult = CourseTotal.objects.annotate(cosdistance=ExpressionWrapper(imc,output_field=FloatField())).annotate(count=Count('coursedetail')).order_by('-cosdistance').filter(count=_order)[:_cnt]
        else:
            imresult = CourseTotal.objects.annotate(cosdistance=ExpressionWrapper(imc,output_field=FloatField())).annotate(count=Count('coursedetail')).order_by('cosdistance').filter(count=_order)[:_cnt]
        print(imresult)
        seriailizer = CourseSerializer(imresult,many=True)
        return Response(seriailizer.data)

class CoursePostView(APIView):
    permission_classes = [IsLogined]
    def get(self,request):
        category = request.GET.get('category')
        coursePost = CoursePost.objects.all().filter(category=category)
        serializer = CoursePostSerializer(coursePost, many=True)
        # for k in serializer.data:
        #     check = CoursePost.objects.get(pk=k['id']).like_users.filter(id=request.user.id).exists()
        #     k['likeusercheck'] = check
        return Response(serializer.data)

    def post(self,request):
        serializers = CoursePostSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            coursepost= serializers.save(user_id=request.user.id)
        try:
            images =  dict((request.data).lists())['image']
            for image in images:
                testserializer = ImageSerializer(data={
                    'image':image})
                if testserializer.is_valid(raise_exception=True):
                    testserializer.save(coursepost_id=coursepost.id)
        except:
            pass
        return Response(serializers.data)

class CoursePostDetailView(APIView):
    permission_classes = [IsLogined]
    def get(self,request,pk):
        coursePost = CoursePost.objects.get(pk=pk)
        coursePost.update_counter
        serializer = CoursePostSerializer(coursePost)
        return Response(serializer.data)

class MypageView(APIView):
    def get(self,request):
        user = request.user
        serializers = UserSerializer

class PostLikeView(APIView):
    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        return post.like_users.filter(id=request.user.id).exists()

    def post(self,request,pk):
        post = Post.objects.get(pk=pk)
        if post.like_users.filter(id=request.user.id).exists():
            post.like_users.remove(request.user)
            return Response({'message': "좋아요 취소"})
        else:
            post.like_users.add(request.user)
            return Response({'message': "좋아요"})