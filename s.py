import os
import glob
import shutil
import json

src_list = os.listdir('ocpp_old/v201/schemas/')
src = 'ocpp_old/v201/schemas/'
dst = 'ocpp/v201/schemas/'

for file in src_list:

    path = src + file
    fd = open(path, 'r')
    json_data = json.load(fd)
    fd.close()


    fd = open(dst + file, 'r')
    json_data2 = json.load(fd)
    fd.close()

    print(file, '  ====  ', True if json_data2 == json_data2 else False )
