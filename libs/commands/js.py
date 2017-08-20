#template.py
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	jsname = name
	files = createClass.createClass()
	files.createFile(
		jsname + '.js',
		app.config['folders']['js'],
		"module.exports = function() {\n\n"+
		"};"
	)