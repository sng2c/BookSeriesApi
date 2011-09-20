#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import bookseries
import simplejson


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(u"""
        <html>
        <body>
        <ul>Yes24
        <li>isbn으로 yes24상세페이지 찾기<br><a href="/yes24/url_by_isbn.do?isbn=9788925282756">/yes24/url_by_isbn.do?isbn=9788925282756</a></li>
        <li>yes24상세페이지로 시리즈정보 찾기<br><a href="/yes24/series_urls.do?url=http%3A%2F%2Fwww.yes24.com%2F24%2Fgoods%2F5547485">/yes24/series_urls.do?url=http%3A%2F%2Fwww.yes24.com%2F24%2Fgoods%2F5547485</a></li>
        </ul>
        <ul>Aladin
        <li>isbn으로 aladin상세페이지 찾기<br><a href="/aladin/url_by_isbn.do?isbn=9788925282756">/aladin/url_by_isbn.do?isbn=9788925282756</a></li>
        <li>aladin상세페이지로 시리즈정보 찾기<br><a href="/aladin/series_urls.do?url=http%3A%2F%2Fwww.aladin.co.kr%2Fshop%2Fwproduct.aspx%3FISBN%3D9788925282756">/aladin/series_urls.do?url=http%3A%2F%2Fwww.aladin.co.kr%2Fshop%2Fwproduct.aspx%3FISBN%3D9788925282756</a></li>
        </ul>
        </body>
        </html>
        """)



class Yes24SeriesHandler(webapp.RequestHandler):
    def get(self):
        url = self.request.get("url",None);
        if url == None :
            self.response.out.write(simplejson.dumps([]))
            return
        p = bookseries.Yes24Series();
        s = p.parse(url)
        self.response.out.write(simplejson.dumps(s))

class Yes24IsbnHandler(webapp.RequestHandler):
    def get(self):
        isbn = self.request.get("isbn",None);
        if isbn == None :
            self.response.out.write(simplejson.dumps([]))
            return
        
        p = bookseries.Yes24Series();
        u = p.url(isbn)
        self.response.out.write(simplejson.dumps(u))

class AladinSeriesHandler(webapp.RequestHandler):
    def get(self):
        url = self.request.get("url",None);
        if url == None :
            self.response.out.write(simplejson.dumps([]))
            return
        p = bookseries.AladinSeries();
        s = p.parse(url)
        self.response.out.write(simplejson.dumps(s))

class AladinIsbnHandler(webapp.RequestHandler):
    def get(self):
        isbn = self.request.get("isbn",None);
        if isbn == None :
            self.response.out.write(simplejson.dumps([]))
            return
        
        p = bookseries.AladinSeries();
        u = p.url(isbn)
        self.response.out.write(simplejson.dumps(u))


def main():
    application = webapp.WSGIApplication(
        [('/yes24/series_urls.do',Yes24SeriesHandler),
         ('/yes24/url_by_isbn.do',Yes24IsbnHandler),
         ('/aladin/series_urls.do',AladinSeriesHandler),
         ('/aladin/url_by_isbn.do',AladinIsbnHandler),
         ('/', MainHandler)
         ], debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
