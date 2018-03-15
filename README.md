# WP Yeti
Python script that helps with my WordPress development. The script speeds up creating PHP + Timber/twig files. For example, after executing ```python3 yeti.py --make:template gallery``` it will create a PHP and Twig file inside the correct like this:

```
<?php
/*
Template Name: Gallery Template
*/

$context = Timber::get_context();
$post = new TimberPost();
$context['post'] = $post;
Timber::render( array( 'template-gallery.twig' ), $context );
```

### Requirements
In order to run this script you will need python3, pip3, python-dotenv, and pymysql.
```pip3 install python-dotenv pymysql```


### How to use it
1. Place the folder inside your root folder
2. Change the details inside the .env and copy it to the root folder
3. Navigate to kleinisan through terminal

```python3 yeti.py --make:template gallery```

#### -h, --help
#### --make:template [FILE NAME]
Quickly create a "template" php file + timber/twig file inside the theme folder


```Response:
Created ../wp-content/themes/[THEME]/template-[FILENAME].php..
Created ../wp-content/themes/[THEME]/_views/template-[FILENAME].twig..
```


#### --make:page [FILE NAME]
Quickly create a 'page' php file + twig file inside the theme folder

```Response:
Created ../wp-content/themes/[THEME]/page-[FILENAME].php..
Created ../wp-content/themes/[THEME]/_views/page-[FILENAME].twig..
```

#### --make:single [FILE NAME]
Quickly create a 'single' php file + twig file inside the theme folder

```Response:
Created ../wp-content/themes/[THEME]/single-[FILENAME].php..
Created ../wp-content/themes/[THEME]/_views/single-[FILENAME].twig..
```

#### --make:taxonomy [FILE NAME]
Quickly create a taxonomy file inside your theme / custom post folder.

```Response:
Created ../wp-content/themes/[THEME]/custom_posts/taxonomy-[FILENAME].php
```


#### --make:custom_posts [FILE NAME]
Quickly create a custom post file inside your theme / custom post folder.

```Response:
Created ../wp-content/themes/[THEME]/custom_posts/[FILENAME].php..
```

#### --make:js [FILE NAME]
Quickly create a JS file inside your source folder.

```Response:
Created ../source/js/[FILENAME].js..
```


#### --make:ajax [FILE NAME]
Quickly create a PHP inside your theme / ajax folder.

```Response:
Created ../wp-content/themes/[THEME]/custom_posts/[FILENAME].php..
```


#### --make:api [FILE NAME]
Quickly create a PHP inside your theme / api folder.

```Response:
Created ../wp-content/themes/[THEME]/api/[FILENAME].php..
```


#### --acf:global_general
Quickly create an ACF JSON file for Global fields inside the theme / acf-json folder (Social Media, 404 page)

```Response:
Created ../wp-content/themes/[THEME]/acf-json/group_5924c60418aa5.json..
```

#### --acf:gallery
Quickly create an ACF JSON file for Gallery fields inside the theme / acf-json

```Response:
Created ../wp-content/themes/[THEME]/acf-json/group_594158f5097e7.json..
```

#### --acf:acf_maps
Quickly create ACF JSON files for Map pins, and Map category (pin categories)

```Response:
Created ../wp-content/themes/[THEME]/acf-json/group_58e2e23fe9d48.json..
Created ../wp-content/themes/[THEME]/acf-json/group_58e3d20cb88e9.json..
```

#### --build:first_project
This command is used when you first start developing a new project. This command does the following things:

- This command executes the composer file inside your root folder, which will fetch your plugins and WP core files.
- If you've entered the ACF key inside your .env file it will fetch the latest ACF PRO plugin
- Fetches the most up-to-date theme files from Timbers starter theme (https://github.com/timber/starter-theme)
- Creates a custom style.css inside your theme folder

#### --build:finished_project
This command is used for finished projects. This command does the following things:

- This command executes the composer file inside your root folder, which will fetch your plugins and WP core files.
- If you've entered the ACF key inside your .env file it will fetch the latest ACF PRO plugin
- Sets up a prepared wp-config file with phpenv support (+ an option to use multisite wp-config)
- Search & Replace + Import DB

#### --build:configure_db
After you've set up the build and set up the database, you can use this command to setup some database options. You will be able to choose which options you want, and which ones you don't. This command can do the the following things:

- Clear blog description
- Change permalinks to /%postname%/ 
- Change all image sizes to 0
- Create multiple pages at once


#### --insert:scripts
Quickly adds the following inside your functions file:

```
function script_init() {
	if (!is_admin()) {
		wp_deregister_script('jquery');
		wp_register_script('jquery', 'https://code.jquery.com/jquery-2.2.4.min.js',false, '2.2.4', true);
		wp_enqueue_script('jquery');
	}

	wp_register_script('app', get_bloginfo('template_url') . '/js/app.js', array('jquery'), true, true);
	wp_enqueue_script('app');
}
add_action('wp_enqueue_scripts', 'script_init');
```


#### --insert:api_routing
Quickly adds the following inside your functions file:

```
Routes::map('api/:name/:id', function($params) {
    $file = 'error';
    Routes::load('api/' . $file . '.php', $params, null);
});
```

#### --insert:options_menu
Quickly adds the following inside your functions file:

```
if(function_exists('register_options_page')) {
  register_options_page('General');
}
```


#### --insert:images
Quickly adds the following inside your functions file:

```
if ( function_exists( 'add_image_size' ) ) {
	add_image_size( '1680x945', 1680, 945, true );
}
```

#### --insert:menus
Quickly adds the following inside your functions file:

```
if(function_exists('register_options_page')) {
  register_options_page('Navigation');
}
```

#### --insert:cache_json
Quickly adds the following inside your functions file:

```
Class cacheJSON {
  public $return;

  function init($json, $path, $id = null) {
      $this->return = $this->fileAge($json, $path);
  }

  function fileAge($json, $path) {
    $minutes = 1800; // twenty four hours
    if (file_exists($path)) {
      // If file exist, check if the file is older than 2 hours, if yes cache new
      if (time()-filemtime($path) > $minutes) {
        return $this->cacheData($json, $path);
      } else {
        return json_decode(file_get_contents($path), true);
      }
    } else {
      // If file doesn't exist cache
      return $this->cacheData($json, $path);
    }
  }

  //Only for checks
  function checkAge($path, $id = null) {
    $minutes = 1800; // twenty four hours

    if (file_exists($path)) {
      // If file exist, check if the file is older than 2 hours, if yes cache new
      if (time()-filemtime($path) > $minutes) {
        return true;
      } else {
        return false;
      }
    } else {
      // If file doesn't exist cache
      return true
;    }
  }

  function cacheData($json, $path) {
    $buffer = fopen($path, 'w+');
    fwrite($buffer, json_encode(json_decode($json)));
    fclose($buffer);
    return $json;
  }
}
```

#### --insert:acf_gmaps_key
Add Gmap API key for ACF

```
function my_acf_init() {
	acf_update_setting('google_api_key', "KEY")
}
add_action('acf/init', 'my_acf_init')
```


#### --insert:acf_save_json
Adds ACF json automatic file import and export 

```
add_filter('acf/settings/save_json', 'my_acf_json_save_point');
function my_acf_json_save_point( $path ) {
    $path = get_stylesheet_directory() . '/acf-json';
    return $path;
}

add_filter('acf/settings/load_json', 'my_acf_json_load_point');
function my_acf_json_load_point( $paths ) {
    unset($paths[0]);
    $paths[] = get_stylesheet_directory() . '/acf-json';
    return $paths;
}
```
