from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from api import models
from django.contrib.auth import get_user_model
import random
from django.db.models.functions import Radians, Power, Sin, Cos, ATan2, Sqrt, Radians
from django.db.models import F
import datetime
User = get_user_model()

class Command(BaseCommand):
    help = 'dummydata input'

    def _dummyinput(self):
        print('dummydata를 input합니다.')
        User.objects.all().delete()
        models.CourseTotal.objects.all().delete()
        models.CourseDetail.objects.all().delete()
        _lat = 35.1874726
        _lon = 126.900115
        searchrange = (15.9*(2**(19-11.5))*2)/1000
        dlat = Radians(F('latitude') - _lat)
        dlong = Radians(F('longitude') - _lon)
        a = (Power(Sin(dlat/2), 2) + Cos(Radians(_lat)) 
        * Cos(Radians(F('latitude'))) * Power(Sin(dlong/2), 2)
        )

        c = 2 * ATan2(Sqrt(a), Sqrt(1-a))
        d = 6371 * c
        te = models.Location.objects.select_related('category').annotate(distance=d).filter(distance__lt=searchrange).order_by('rank')
        getlist = list(te.values_list('id',flat=True))
        for i in range(10):
            print(f'{i+1}회 시작')
            login_email = f'test{i+1}@test.com'
            age = random.choice(range(20,50))
            random_plate = []
            for j in range(10):
                random_plate.extend([j+1]*random.randint(1,5))
            testuser = User.objects.create_user(email=login_email,password='loveline',nickname=f'test{i+1}',gender='남',age=age)
            for k in range(100):
                taste = random.choice(random_plate)
                tour = random.choice(random_plate)
                activity = random.choice(random_plate)
                N = random.choice(range(2,6))
                days = random.choice(range(1,30))
                input_days = datetime.date(2020,10,days)
                coursetotal = models.CourseTotal.objects.create(user_id=testuser.id,taste=taste,tour=tour,activity=activity,traveldate=input_days)
                location_sample = random.sample(getlist,N)
                for ind,location_id in enumerate(location_sample):
                    models.CourseDetail.objects.create(location_id=location_id,order=ind+1,coursetotal_id=coursetotal.id)
            print(f'{i+1}회 Done')


    def handle(self,*args,**kwargs):
        self._dummyinput()