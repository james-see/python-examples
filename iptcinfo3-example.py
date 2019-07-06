"""
What: IPTCINFO3 example
Author: James Campbell
Date: 5 July 2019
"""
import sys

import iptcinfo3

im = open(sys.argv[1])
try:
    info = iptcinfo3.IPTCInfo(sys.argv[1])
    print('-------IPTC DATA FOUND-------')
    for k, v in info._data.items():
        print(k, v)
    # info['city'] = '#magistræde #🇩🇰'
    # info.save()
except Exception as e:
    if str(e) != "No IPTC data found.":
        raise
