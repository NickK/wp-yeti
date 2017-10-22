#taxonomy.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	#define config vars
	CUSTOM_POSTS_FOLDER = os.environ.get('CUSTOM_POSTS')

	taxonomyname = 'taxonomy-' + name
	registertaxonomyname = input('Taxonomy Name (used for register_taxonomy. Used for fetching data): ')
	custom_post = input('Which custom post type does it belong to: ')
	taxonomylabel= input('Taxonomy Label: ')
	taxonomyadditem= input('Add Item Label (Singular): ')

	files = createClass.createClass()
	#passing path through is weird
	files.createFile(
		taxonomyname + '.php',
		CUSTOM_POSTS_FOLDER,
		"<?php\n"+
		"$labels = array(\n"+
		"	'name'        => '" + taxonomylabel + "',\n"+
		"	'add_new_item' => 'Add new " + taxonomyadditem + "'\n"+
		");\n"+
		"register_taxonomy('" + registertaxonomyname + "', array('" + custom_post + "'),\n"+
		"	array('hierarchical' => true,\n"+
		"	  'labels'       => $labels,\n"+
		"	  'rewrite'      => true,\n"+
		"	  'show_tagcloud' => true\n"+
		"	)\n"+
		");"
	)