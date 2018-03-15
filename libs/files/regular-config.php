<?php

// BEGIN iThemes Security - Do not modify or remove this line
// iThemes Security Config Details: 2
define( 'DISALLOW_FILE_EDIT', true ); // Disable File Editor - Security > Settings > WordPress Tweaks > File Editor
// END iThemes Security - Do not modify or remove this line

require_once(__DIR__ . '/vendor/autoload.php');
(new \Dotenv\Dotenv(__DIR__))->load();


/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', getenv('DB_NAME'));

/** MySQL database username */
define('DB_USER', getenv('DB_USER'));

/** MySQL database password */
define('DB_PASSWORD', getenv('DB_PASSWORD'));

/** MySQL hostname */
define('DB_HOST', getenv('DB_HOST'));

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'sgEM1u-??&~b~%,@F8w>iQ-T&A{HX.^Op X6~EO9L<Hmq<&@yG?i$HY}6-yVWdwe');
define('SECURE_AUTH_KEY',  '1|m)Z6EG-y5CBR+||??e OT2}9h.g|z%a?s<kizO1J@eV=b0>,d+c1V9?_HTF6-k');
define('LOGGED_IN_KEY',    '-:w@cO6dPVY#pb+t;_J95P9;c5X{qtkj?:~C&SQS8Pd_:,b}ThaiYBUFOMVC `!o');
define('NONCE_KEY',        'c:ut|<>NGI+4`dnQDH+qL<~KTN_OX 0=pF,>B/8<+79@Hj$Ua8rE4_x]b&Dk+k!1');
define('AUTH_SALT',        '%1x56;f&$|=~ ?a]>m-IMl;J<W)%)D|xX:-<Odz4Fh{ ae>0nu9+1no`7+iThOj9');
define('SECURE_AUTH_SALT', 'Fm@:,b*@_l{ENb@Dd8d ]?Ffq2d(rXOrkmvW&mewk|QI|tJt%F~`@TV*~P3oCAif');
define('LOGGED_IN_SALT',   'n2q^Ts80l=5d|paWj-A*sF[^+_-1D+}YZqu[Yi<EK10.@Gh$W.Ii#f+,GWJ++ShV');
define('NONCE_SALT',       'jclZiW~E8GD$6xQ@2KzGL:V[UV02x{H.oF}y~&Sg:KTjO&Y?Gt;oWLx6ZD~|T5LJ');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = getenv('DB_PREFIX');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', true);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
