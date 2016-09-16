import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                    autoescape = True)


def converts(vari):
	words = []
	numbers = []
	splitext = list(vari)

	for i in splitext:
		numbers.append(ord(i))
			
	for x in numbers:
		if x >= 65 and x <= 77 or x >= 97 and x <= 109:
			words.append(chr(x + 13))
		elif x >= 78 and x <= 90 or x >= 110 and x <= 122:
			words.append(chr(x - 13))
		else:
			words.append(chr(x))

	words = ''.join(words)

	return words
 

class MainHandler(webapp2.RequestHandler):

	def printTemplate(self, template):
		templt = jinja_env.get_template(template)
		self.response.out.write(templt.render())

		
	def get(self):
		self.printTemplate('rot13.html')


	def post(self):
		converted = converts(self.request.get('text'))
		template = jinja_env.get_template('rot13.html')
		self.response.write(template.render(namecode=converted))

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)







