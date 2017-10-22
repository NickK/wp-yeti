#js.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	#define config vars
	JS_FOLDER = os.environ.get('JS_FOLDER')

	jsname = name
	files = createClass.createClass()
	files.createFile(
		jsname + '.js',
		JS_FOLDER,
		"module.exports = function() {\n\n"+
		"};"
	)