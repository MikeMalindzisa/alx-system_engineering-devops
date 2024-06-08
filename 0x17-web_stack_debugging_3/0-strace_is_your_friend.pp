# Ensure correct PHP extension in wp-settings.php by replacing 'phpp' with 'php'

# Fixing Apache returning a 500 error

exec { 'fix error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}