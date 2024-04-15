"""
What: IPTCINFO3 example
Author: James Campbell
Date: 5 July 2019
"""
import iptcinfo3

try:
    info = iptcinfo3.IPTCInfo('assets/guy881.jpg', inp_charset="cp1250",
                              out_charset='cp1250', force=True)
    print('-------IPTC DATA FOUND-------')
    print(info.packedIIMData())
    for k, v in info._data.items():
        print(f"KEY: {k} VALUE: {str(v)}")
    # info['city'] = '#magistræde #🇩🇰'
    # info.save()
except Exception as e:
    if str(e) != "No IPTC data found.":
        raise
