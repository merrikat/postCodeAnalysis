# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:42:47 2016

@author: leo
"""

import glob
import os
#from oscodepoint import open_codepoint
import re
from pprint import PrettyPrinter
from postcodes import PostCoder

fileList = []
postcodeList = []
os.chdir("/Users/leo/Documents/MyCode/walesCSVs/")
for counter, files in enumerate(glob.glob("*.csv")):
    fileList.append(files)
    
for fileIn in fileList:
    f = open(fileIn)
    lines = f.readlines()
    for line in lines[1:]:
        postCode = []
        postCode = re.findall(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', line)
        if postCode:
            postcodeList.append(postCode[0])
    f.close()
    
latLongList = []    
pc = PostCoder()
count = 0
for postcode in postcodeList:
    try:
        result = pc.get(postcode)
        latLongList.append([result['geo']['lat'],result['geo']['lng']])
        count+=1
        if count%25 ==0:
            print "Processed %d of %d results" %(count,len(postcodeList))
    except:
        pass