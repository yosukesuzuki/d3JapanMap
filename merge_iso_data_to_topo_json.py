#!/usr/bin/python
# coding: UTF-8

import json

f = open('iso3166-2_data_from_wikipedia.txt', 'r')

prefectures = {} 
for line in f:
    cells = line.strip().split('\t')
    prefecture = None
    prefecture = {'name':cells[0],'japanese':cells[1],'capital':cells[2],'region':cells[3],'major_island':cells[4],'iso':cells[10]}
    print prefecture
    prefectures[cells[0]] = prefecture


f = open('japan_topo_with_ne.json', 'r')
json_data = json.loads(f.read())
for i in range(len(json_data['objects']['japan']['geometries'])):
    pname = json_data['objects']['japan']['geometries'][i]['properties']['NAME']
    print pname
    json_data['objects']['japan']['geometries'][i]['properties'] = prefectures[pname]


result_file = open('japan_topo_with_properties.json','w')
result_file.write(json.dumps(json_data, encoding='UTF-8'))
