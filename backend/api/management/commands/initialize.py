from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from api import models

class Command(BaseCommand):
    help = 'initialize database'
    DATA_DIR = Path(settings.BASE_DIR).parent / 'data'
    DATA_PATH = str(DATA_DIR/'datapreprocessing.pkl')

    def _load_dataframes(self):
        print(Command.DATA_PATH)
        data = pd.read_pickle(Command.DATA_PATH)
        return data

    def _initialize(self):
        print('loading data')
        dataframes = self._load_dataframes()
        print('Done')
        print('initialize models')
        models.Location.objects.all().delete()
        models.CategoryGroup.objects.all().delete()
        models.Category.objects.all().delete()
        categorygroups = dataframes['categorygroups']
        categorys = dataframes['categorys']
        locations = dataframes['locations']
        categorygroup_bulk = [
            models.CategoryGroup(
                id = categorygroup.id,
                name = categorygroup.name
            )
            for categorygroup in categorygroups.itertuples()
        ]
        models.CategoryGroup.objects.bulk_create(categorygroup_bulk)
        print('categorygroup_done')
        category_bulk = [
            models.Category(
                id = category.id,
                name = category.name,
                categorygroup_id = category.categorygroup,
            )
            for category in categorys.itertuples()
        ]


        models.Category.objects.bulk_create(category_bulk)
        print('category_done')
        location_bulk = [
            models.Location(
                id = location.id,
                name = location.name,
                address = location.address,
                tel = location.tel,
                latitude = location.latitude,
                longitude = location.longitude,
                category_id = location.category,
                rank = location.rank

            )
            for location in locations.itertuples()
        ]
        models.Location.objects.bulk_create(location_bulk)
        print('done')

    def handle(self,*args,**kwargs):
        self._initialize()

