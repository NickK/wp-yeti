#api.py
import os
from libs.config import app
from libs.classes import createFiles as createClass

def scripts():
	#define config vars	
	THEME_FOLDER = os.environ.get('THEME_FOLDER')

	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
			"function script_init() {\n"+
			"	if (!is_admin()) {\n"+
			"		wp_deregister_script('jquery');\n"+
			"		wp_register_script('jquery', 'https://code.jquery.com/jquery-2.2.4.min.js',false, '2.2.4', true);\n"+
			"		wp_enqueue_script('jquery');\n"+
			"	}\n\n"+

			"	wp_register_script('app', get_bloginfo('template_url') . '/js/app.js', array('jquery'), true, true);\n"+
			"	wp_enqueue_script('app');\n"+
			"}\n"+
			"add_action('wp_enqueue_scripts', 'script_init');"
	    )

def api_routing():
	#define config vars	
	THEME_FOLDER = os.environ.get('THEME_FOLDER')

	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
				"// API routing\n"
				"Routes::map('api/:name/:id', function($params) {\n"
				"    $file = 'error';\n"
				"    Routes::load('api/' . $file . '.php', $params, null);\n"
				"});\n"
	    )

def acf_save_json():
	#define config vars	
	THEME_FOLDER = os.environ.get('THEME_FOLDER')

	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
	    		"//Save & load ACF fields to folder\n"
				"add_filter('acf/settings/save_json', 'my_acf_json_save_point');\n"
				"function my_acf_json_save_point( $path ) {\n"
				"    $path = get_stylesheet_directory() . '/acf-json';\n"
				"    return $path;\n"
				"}\n\n"


				"add_filter('acf/settings/load_json', 'my_acf_json_load_point');\n"
				"function my_acf_json_load_point( $paths ) {\n"
				"    unset($paths[0]);\n"
				"    $paths[] = get_stylesheet_directory() . '/acf-json';\n"
				"    return $paths;\n"
				"}\n"
	    )
def options():
	#define config vars	
	THEME_FOLDER = os.environ.get('THEME_FOLDER')

	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
				"// Register the global option page for editing templates\n"+
				"if(function_exists('register_options_page')) {\n"+
				"  register_options_page('General');\n"+
				"}\n"
		)

def acf_gmaps_key():
	#define config vars	
	THEME_FOLDER = os.environ.get('THEME_FOLDER')
	GMAPS_KEY = os.environ.get('GMAPS_KEY')

	if (GMAPS_KEY != 'INSERTKEY'):
			gmaps_acf_write(THEME_FOLDER, GMAPS_KEY)
	else:
		action = input('Gmaps key is missing. Continue anyway (y/n)')
		if (action == 'y'):
			gmaps_acf_write(THEME_FOLDER, GMAPS_KEY)

def gmaps_acf_write(THEME_FOLDER, GMAPS_KEY):
	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
				"// GOOGLE MAPS API KEY CALL\n" +
				"function my_acf_init() {\n"+
				"	acf_update_setting('google_api_key', " + GMAPS_KEY + ");\n"+
				"}\n"+
				"add_action('acf/init', 'my_acf_init');\n"
		)

def add_images():
	THEME_FOLDER = os.environ.get('THEME_FOLDER')

	with open(THEME_FOLDER + 'functions.php', 'a') as f:
	    f.write("\n\n\n\n" +
	    		"// Add additional image sizes\n"+
				"if ( function_exists( 'add_image_size' ) ) {\n"+
				"	add_image_size( '1680x945', 1680, 945, true );\n"+
				"}"
		)