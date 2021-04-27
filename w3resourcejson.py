import json
import os
# json_obj='{ "Name":"David", "Class":"I", "Age":6 , "Name":"warner", "Class":"II", "Age":7 }'
f=open('book1.json',)
data=json.load(f)
# print(data)
print(data)

for i in data['book']:
    # print(i)
    dataid1=print(i.get('author'))
    # print(dataid1)
    a = None
    if dataid1 is None:
        print("")
    else:
        print(dataid1)

j_str={'4':5, '6':7, '3':9}
print(j_str)
print(json.dumps(j_str,indent=2,sort_keys=True))

with open('book1.json') as f:
    subdata=json.load(f)
for i in subdata['book']:
    del i['edition']
with open('newbook.json','w') as f:
    json.dump(subdata,f,indent=2)
j=open('newbook.json',)
print(json.load(j))





