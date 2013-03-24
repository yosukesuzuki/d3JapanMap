#!/usr/bin/python
# coding: UTF-8

import json

f = open('iso3166-2_data_from_wikipedia.txt', 'r')

prefectures = []
for line in f:
    cells = line.strip().split('\t')
    prefecture = None
    prefecture = {'prefecture':cells[0],'japanese':cells[1],'capital':cells[2],'region':cells[3],'major_island':cells[4],'iso':cells[10]}
    print prefecture
    prefectures.append(prefecture)

print len(prefectures)

f = open('jpn_topo.json', 'r')
jpn_topo = f.read()

result_dic = {'prefectures':prefectures}

result_file = open('jpn_prefecture_meta_data_sort_alphabetical.json','w')
result_file.write(json.dumps(result_dic, encoding='UTF-8'))
