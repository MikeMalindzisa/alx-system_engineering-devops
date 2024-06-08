# Ensure correct PHP extension in wp-settings.php by replacing 'phpp' with 'php'

# Define an exec resource to execute a command
exec { 'fix_wordpress_extension':
  # Command to replace 'phpp' with 'php' in wp-settings.php using sed
  command   => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider  => 'shell',
}
