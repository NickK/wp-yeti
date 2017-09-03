# Kleinisan
Python script that helps with my WordPress development. (Name needs work). The script helps create PHP + Timber/twig files and a default script. For example, after executing a command it will create a template.php file like this automatically in the correct folders:
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
In order to run this script you will need python3 and python-dotenv (pip install python-dotenv). Here's how to get it for each platform:

### How to use it
1. Place the folder inside your root folder
2. Change the details inside the .env and copy it to the root folder
3. Navigate to kleinisan through terminal

```python3 kleinisan.py --make:template gallery```

#### -h, --help
#### --make:template FILENAME
Creates a "template" php file + timber/twig file. 

```Response:
Created ../template-FILENAME.php..
Created ../_views/template-FILENAME.twig..
```


#### --make:page FILENAME
#### --make:single FILENAME
#### --make:taxonomy FILENAME
#### --make:custom_posts FILENAME
#### --make:js FILENAME
#### --make:ajax functionname
#### --make:api functionname
#### --acf:global_general
#### --acf:gallery
#### --acf:maps
#### --build:theme
#### --build:configure_db
