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
define('AUTH_KEY',         't|[4_D49/ ,h>)fp*<Yj|-@>/A{3l<NbKg2-9eTsDx>qOcuu2s|Y9|A_Wup.`wi&');
define('SECURE_AUTH_KEY',  '>u#b@HyWW_q3({62e5 E_cW8>B6$S9D@q~K9Ne4 9A)>m?XH.005b#Dh75nmiNyr');
define('LOGGED_IN_KEY',    '[~l3M^|yrLbAuMZRuxmP6ra;aR$XI%?Q%14M(;2!Hi@yn}<V2m4rDnk4c--TJ%1G');
define('NONCE_KEY',        ')4u~10DYP0WWb59.jiICJoC;r]SuNId6 &a4j&*K7,~tf8^+Znz=UB-:,]vKXKh&');
define('AUTH_SALT',        'O7Z^5|GBnD?&{g+4-5.=@5Ka!I[+>1 Ar1vVT1%*c}.BW&gT=7QY|%~v-#yeu=Dt');
define('SECURE_AUTH_SALT', '`YkA!)yQR2d@RHV1q`>P%1TcAy[|n)?&,e;va{o`%t++#zm0g7JYL47u.Qu^*P2<');
define('LOGGED_IN_SALT',   'q;;Li,odi*y5b~oaCS/Gzu|B#3W|Q:%PC_P^fOqM|xN<3DF,:0|Oa18<JzIXSY@T');
define('NONCE_SALT',       'x#vrjypj!4!+U~|=Iy0*C,nMUTRI-S,3Ca(IlS/vz!on|0wb+.+^yp|EdCoD)YSa');


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

/* Multisite */
define( 'WP_ALLOW_MULTISITE', true );
define('MULTISITE', true);
define('SUBDOMAIN_INSTALL', false);
define('DOMAIN_CURRENT_SITE', getenv('SERVER_NAME'));
define('PATH_CURRENT_SITE', '/');
define('SITE_ID_CURRENT_SITE', 1);
define('BLOG_ID_CURRENT_SITE', 1);


/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
