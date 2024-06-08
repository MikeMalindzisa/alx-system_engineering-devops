# Fixes bad `phpp` extensions to `php` in wp-settings.php

exec { 'fix_wordpress_extension':
  command     => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path        => '/usr/bin:/bin',
  onlyif      => 'grep -q "phpp" /var/www/html/wp-settings.php',
  refreshonly => true,
  notify      => Service['apache2'],
}
