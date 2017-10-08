# -*- coding: utf-8 -*-
'''
Created on 2017年10月8日

PROXIES = [
    {"ip_port": "219.159.105.180:8080"},
]

@author: Administrator
'''
import csv

if __name__ =="__main__":
    output = open('../misc/proxy.py', 'w')
    
    with open("../data/xicidaili.csv","r") as csvfile:
        reader = csv.reader(csvfile)
        output.writelines('PROXIES = [\n')
        for i,row in enumerate(reader):
            if i>0 and row[3].lower() == 'http':
                output.writelines('    {"ip_port": "'+ row[0]+':'+row[4]+'"},\n')
        output.writelines(']')
        output.close()