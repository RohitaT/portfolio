#!/usr/bin/env python
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
import webapp2 
import os
import logging
import jinja2

#class MainHandler(webapp2.RequestHandler):
 #   def get(self):
  #      self.response.write(template.render())

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
	def get (self):
		path =self.request.path

		if path =='/':#path=='/' :
			path='/index.html'
			check = path.strip('/') # remove the / from the input path
			handle=check.split('.') #remove the . such that the path is split into index html out here
			h1=handle[0] # store index
			h2=handle[1] #store html

			if h1=='index':
				template = JINJA_ENVIRONMENT.get_template('template/index.html')
				self.response.write(template.render({}))

		elif path=='/work.html':  #work template 
			path='/work.html'
			logging.info('path is ='+path)
			check=path.strip('/')
			handle=check.split('.')
			h1=handle[0]
			h2=handle[1]

			if h1=='work':
  				template = JINJA_ENVIRONMENT.get_template('template/work.html')
  				self.response.write(template.render({}))


app = webapp2.WSGIApplication([
   ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/work.html',IndexHandler) #,('/awards.html',AwardHandler)
], debug=True)
