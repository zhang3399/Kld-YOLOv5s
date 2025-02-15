# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = ['defective_insulator', 'broken_defect', 'good_insulator', 'flashover_defect']
abs_path = os.getcwd()



wd = getcwd()
for image_set in sets:
    if not os.path.exists('../labelTxt/'):
        os.makedirs('../labelTxt/')
    image_ids = open('hf_txt/%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '/images/%s.jpg\n' % (image_id))

    list_file.close()
