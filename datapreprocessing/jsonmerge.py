import json
import os
DATA_DIR = '../data'
file_list = os.listdir(DATA_DIR)
TEST_FILE = os.path.join(DATA_DIR,'total.json')
result = []
store_index = file_list.index('음식점_좌표.json')
pc_index = file_list.index('PC방_좌표.json')
file_list[store_index],file_list[pc_index] = file_list[pc_index],file_list[store_index]
for i in file_list:
    if 'json' in i and 'data' not in i and 'total' not in i and '좌표' in i:
        DATA_FILE = os.path.join(DATA_DIR,i)
        print(DATA_FILE)
        with open(DATA_FILE,encoding='utf-8') as f:
            data = json.loads(f.read())
        result +=data
ind = []
print(len(result))


with open(TEST_FILE,'w',encoding='utf-8',) as make_file:
    json.dump(result,make_file,indent=4,ensure_ascii=False)

