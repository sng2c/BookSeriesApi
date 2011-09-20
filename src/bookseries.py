# -*- coding: utf-8 -*-
'''
Created on 2011. 9. 17.

@author: sng2nara
'''

import re
import urllib



class Yes24Series:
    '''
    Yes24Series 모듈
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def url(self,isbn):
        srchurl = "http://www.yes24.com/searchcorner/Result?keywordAd=&keyword=&domain=BOOK&qdomain=%%B1%%B9%%B3%%BB%%B5%%B5%%BC%%AD&query=%s" % isbn
        f = urllib.urlopen(srchurl)
        html = f.read()
        f.close()
        m = re.search('<a href="(/24/goods/.+?)\\?scode=',html)
        if m != None :
            return ["http://www.yes24.com"+m.group(1)]
        else:
            return []

    def parse(self,dataurl):
        ret = []
        f = urllib.urlopen(dataurl)
        html = f.read()
        f.close()
        html = html.decode('EUC-KR')
        m = re.search('<ul id="series_list">(.+?)</ul>',html,re.S)
        if m != None :
            ul = m.group(1)
            for m in re.finditer('<a href="(.+?)">(.+?)</a>', ul) :
                ret.insert(0, [m.group(2),"http://www.yes24.com"+m.group(1)])
        return ret

class AladinSeries:
    '''
    Yes24Series 모듈
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def url(self,isbn):
        srchurl = "http://www.aladin.co.kr/shop/wproduct.aspx?ISBN=%s" % isbn
        return [srchurl]

    def parse(self,dataurl):
        ret = []
        f = urllib.urlopen(dataurl)
        html = f.read()
        f.close()
        html = html.decode('EUC-KR')
        m = re.search('<div class="np_series_box" style="float:none;">(.+?)</div>',html,re.S)
        if m != None :
            ul = m.group(1)
            for m in re.finditer('<a class="np_bfpm2" href="(.+?)">(.+?)</a>', ul) :
                ret.append([m.group(2),m.group(1)])
        return ret


import unittest
class Test(unittest.TestCase):

    def testYes24(self):
        bs = Yes24Series()
        
        url = bs.url("9788925282756")
        print url
        
        sinfo = bs.parse("http://www.yes24.com/24/goods/5547485");
        print sinfo[0][0]
        self.assertEqual(u"킹덤 (KINGDOM) 1", sinfo[0][0]);
        

    def testAladin(self):
        bs = AladinSeries()
        
        url = bs.url("9788925282756")
        print url
        
        sinfo = bs.parse("http://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9788925282756");
        print sinfo[0][0]
        self.assertEqual(u"킹덤 Kingdom 1", sinfo[0][0]);
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()