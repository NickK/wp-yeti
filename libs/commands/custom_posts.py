#custom_posts.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def init(name):
	#define config vars
	CUSTOM_POSTS_FOLDER = os.environ.get('CUSTOM_POSTS')

	custom_post_name = name
	plural = input('Plural Label: ').lower()
	singular = input('Singular Label: ').lower()
	slug = input('Slug: ' ).lower()

	singular_upper = singular[0].upper() + singular[1:]
	plural_fupper = plural[0].upper() + plural[1:]

	files = createClass.createClass()
	files.createFile(
		custom_post_name.lower() + '.php',
		CUSTOM_POSTS_FOLDER,
		"<?php\n" +
		"$labels = array(\n" +
		"	'name' => _x('" + plural_fupper + "', 'post type " + plural + "'),\n" +
		"	'singular_name' => _x('" + singular_upper + "', 'post type singular "+ singular + "'),\n" +
		"	'add_new' => _x('Add new "+ singular + "', '"+ plural + "'),\n" +
		"	'add_new_item' => __('Add new "+ singular + " item'),\n" +
		"	'edit_item' => __('Edit "+ singular + " item'),\n" +
		"	'new_item' => __('New "+ singular + " item'),\n" +
		"	'view_item' => __('View "+ singular + " item'),\n" +
		"	'search_items' => __('Search items'),\n" +
		"	'not_found' =>  __('Nothing found'),\n" +
		"	'not_found_in_trash' => __('Nothing found in Trash'),\n" +
		"	'parent_item_colon' => ''\n"+
		");\n" +
		"$args = array(\n"+
		"	'labels' => $labels,\n"+
		"	'public' => true,\n"+
		"	'publicly_queryable' => true,\n"+
		"	'show_ui' => true,\n"+
		"	'query_var' => true,\n"+
		"	'show_in_rest' => true,\n"+
		"	'rewrite' => array('slug' => '" + slug + "'),\n"+
		"	'capability_type' => 'post',\n"+
		"	'hierarchical' => false,\n"+
		"	'menu_position' => null,\n"+
		"	'supports' => array('title','taxonomy', 'thumbnail', 'editor', 'excerpt'),\n"+
		"	'rest_base' => 'maps',\n"+
		"	'rest_controller_class' => 'WP_REST_Posts_Controller',\n"+
		"  ); \n"+
		"register_post_type( '"+ custom_post_name.lower() + "' , $args );\n"

	)