import os
import xml.etree.ElementTree as ET
from loadingxml import *

wafer_list = ['D07','D08','D23','D24']
requested_list = []
values = []
global name_list
name_list = []

def data_reader():
    path = str(os.getcwd()).replace("src", "")
    while True:
        wafer_id = input('wafer_id : ')
        wafer_cordinate = input('wafer_cordinate : ')
        if wafer_id in wafer_list:
            requested_list.append(wafer_id)
            break
        else:
            if wafer_id == '':
                for wafer_id in wafer_list:
                    requested_list.append(wafer_id)
                break
            else:
                print("This is not a file")

    for wafer in requested_list:
        for folder in os.listdir(path + 'data/HY202103/' + wafer + '/'):
            for root, dirs, files in os.walk(path + 'data/HY202103/' + wafer + '/'):
                for name in files:
                    if name.endswith(".xml"):
                        if f'({wafer_cordinate})' in name:
                            if 'LMZ' in name:
                                print('Single Wafer:')
                                print(name)
                                name_list.append(name)
                                return
                        #else:
                            #print('All Wafers:')
                            #print(name)
                            #name_list.append(name)
    xml_loader()







data_reader()