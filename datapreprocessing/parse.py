#-*- encoding: utf-8 -*-

import json
import os
import pandas as pd
import io


DATA_DIR = '../data'
DATA_FILE = os.path.join(DATA_DIR,'total.json')
CATEGORY_FILE = os.path.join(DATA_DIR,'categorys.json')
DUMP_FILE = os.path.join(DATA_DIR,'datapreprocessing.pkl')
location_columns = (
    'id', # 장소 고유번호
    'name', # 장소의 이름
    'address', # 장소의 주소
    'tel', # 전화번호
    'latitude', # 위도
    'longitude', # 경도
    'category', # 카테고리
    'rank' , # 점수
)
review_columns = (
    'id',
    'location',
    'profile',
    'rate',
    'content',
    'author',
    'created_at',

)
category_columns = (
    'id',
    'name', # 카테고리 명
    'categorygroup', # 상위 카테고리 명
)
categorygroup_columns = (
    'id',
    'name', # 상위카테고리 그룹 명
)
def import_data(data_path=DATA_FILE,category_path=CATEGORY_FILE):
    with io.open(data_path,encoding='utf-8') as f:
        data = json.loads(f.read())
    with io.open(category_path,encoding='utf-8') as f:
        category_data = json.loads(f.read())
    location = []
    category = []
    categorygroup = []
    reviews = []
    location_check = []
    categorygroup_check ={}
    category_check = {}
    g_cnt = 1
    cnt = 1
    review_cnt = 1
    for d in data:
        if d['id'] not in location_check:
            location_check.append(d['id'])
            current_cate = d['category']
            if '음식점' in d['category']:
                cate = list(map(str.strip,d['category'].split('|')))
                for new_cate,old_cate in category_data.items():
                    if cate[1] in old_cate:
                        current_cate = new_cate
                        cate[1] = new_cate
                        break
                else:
                    continue
                if not categorygroup_check.get(cate[0]):
                    categorygroup_check[cate[0]] = g_cnt
                    category_check[cate[1]] = cnt
                    category.append([cnt,cate[1],categorygroup_check[cate[0]]])
                    categorygroup.append([g_cnt,cate[0]])
                    g_cnt += 1
                    cnt += 1
                else:
                    if not category_check.get(cate[1]):
                        category_check[cate[1]] = cnt
                        category.append([cnt,cate[1],categorygroup_check[cate[0]]])
                        cnt += 1
            else:
                if not categorygroup_check.get(d['category']):
                    categorygroup_check[d['category']] = g_cnt
                    category_check[d['category']] = cnt
                    category.append([cnt,d['category'],categorygroup_check[d['category']]])
                    categorygroup.append([g_cnt,d['category']])
                    g_cnt += 1
                    cnt += 1
            rank = -1
            if d['reviews']:
                temp = 0
                ind = 0
                for review in d['reviews']:
                    temp += int(review['rate'])
                    date_change = review['write_time'].replace('.','-')[:-1]
                    reviews.append([
                        review_cnt,
                        d['id'],
                        review['profile'],
                        review['rate'],
                        review['content'],
                        review['user_name'],
                        date_change
                    ])
                    review_cnt += 1
                    ind +=1 
                rank = temp/ind
            location.append(
                [
                    d['id'],
                    d['title'],
                    d['address'],
                    d['phone'],
                    d['latitude'],
                    d['longitude'],
                    category_check[current_cate],
                    rank
                ]
            )
    location_frame = pd.DataFrame(data=location,columns=location_columns)
    category_frame = pd.DataFrame(data=category,columns=category_columns)
    categorygroup_frame = pd.DataFrame(data=categorygroup,columns=categorygroup_columns)
    review_frame = pd.DataFrame(data=reviews,columns=review_columns)
    return {"locations":location_frame,'categorys':category_frame,'categorygroups':categorygroup_frame,'reviews':review_frame}
                
                

def dump_dataframes(dataframs):
    pd.to_pickle(dataframs,DUMP_FILE)

def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

def main():
    print('데이터 파일을 여는중입니다.')
    data = import_data()
    print('데이터 파일을 전부 pd화 했습니다.')

    print('데이터를 전부 pkl 파일로 변환합니다.')
    dump_dataframes(data)
    print('pkl 파일화 했습니다.')
    data = load_dataframes()
    print(data['locations'].head())
    print(data['locations'])
    print('-----')
    print(data['categorygroups'])
    print('--------')
    print(data['reviews'])

if __name__ =="__main__":
    main()