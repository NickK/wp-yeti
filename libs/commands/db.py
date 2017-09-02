#template.py
from libs.config import db
from libs.classes import createFiles as createClass
import pymysql.cursors

def configure_db():
	# Connect to the database
	connection = pymysql.connect(host=db.config['host'],
	                             user=db.config['user'],
	                             password=db.config['password'],
	                             db=db.config['db'],
	                             charset=db.config['charset'],
	                             cursorclass=pymysql.cursors.DictCursor)

	try:
	    with connection.cursor() as cursor:
	        # Read a single record

	        boolean = input('Would you like to empty the blog description? (y/n) ')
	        if (boolean == 'y'):
	        	sql = "UPDATE "+ db.config['prefix'] + "options SET option_value = '' WHERE option_name = 'blogdescription'"
	        	cursor.execute(sql)

	        boolean = input('Would you like to change the permalink structure to /%postname%/ ? (y/n) ')
	        if (boolean == 'y'):
	        	sql = "UPDATE "+ db.config['prefix'] + "options SET option_value = '/%postname%/' WHERE option_name = 'permalink_structure'"
	        	cursor.execute(sql)


	        boolean = input('Would you like to change all the media image sizes to 0 ? (y/n) ')
	        if (boolean == 'y'):
	       		sql = "UPDATE "+ db.config['prefix'] + "options SET option_value = 0 WHERE option_name = 'thumbnail_size_w' or option_name = 'thumbnail_size_h' or option_name = 'medium_size_w' or option_name = 'medium_size_h' or option_name = 'large_size_w' or option_name = 'large_size_h'"
	        	cursor.execute(sql)
	        
	        boolean = input('Would you like to add pages? (y/n) ')
	        if (boolean == 'y'):
		        count = 3
		        insert_sql = 'INSERT INTO '+ db.config['prefix'] + 'posts (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES '
		        pages = input('Which pages would you like to create automatically? (Comma seperated+no spacing before and after) ')
		       	pages = pages.split(',')
		       	for page in pages:
		       		#print(page.strip())
		       		count = count+1
		       		insert_sql += "(" + str(count) + ", 1, now(), now(), '', '" + page.strip() + "', '', 'publish', 'closed', 'open', '', '"+ slugify(page.strip()) +"', '', '', now(), now(), '', 0, 'http://graduatehotels.loc/?page_id=" + str(count) + "', 0, 'page', '', 0),"


		       	cursor.execute(insert_sql[:-1])

	        #
	
	       	connection.commit()

	finally:
	    connection.close()

def slugify(text):
	text = text.replace(' ', '-').lower()
	return text