#api.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	#define config vars	
	API_FOLDER = os.environ.get('API_FOLDER')

	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		name + '.php',
		API_FOLDER,
		"<?php\n" +
		"	header('Content-Type: application/json');\n"
		"	echo json_encode($return);\n"
	)