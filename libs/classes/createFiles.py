#template.py
import os
class createClass:
	def file_exist(self, pathtest):
		#return true if file doesnt exist
		if os.path.isfile(pathtest) or os.path.isdir(pathtest) and pathtest is not '':
			return True
		else:
			return False

	def dir_exist(self, path):
		if not os.path.isdir(path) and path is not '':
			os.makedirs(path)

	def createFile(self, file, path = '', content=''):
		self.dir_exist(path)
		if self.file_exist(path + file) == False:
			file_opened = open(path + file, 'w+')
			file_opened.write(content)
			file_opened.close()
			self.response(path + file)


	def response(self, path):
		print('Created ' + path + '..')
