#!/usr/bin/env puppet
#setting up new server and nginx response hearder

exec { 'update-and-install-nginx':
  command => '/usr/bin/apt-get update -y -qq && /usr/bin/apt-get install nginx -y',
}

service { 'nginx':
  ensure  => 'running',
  require => Exec['update-and-install-nginx'],
}

exec { 'firewall-access':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
}

file { '/var/www/html':
  ensure => 'directory',
  owner  => $USER,
  group  => $USER,
  mode   => '0755',
}

file { '/var/www/html/index.nginx-debian.html.bckp':
  ensure  => 'present',
  source  => '/var/www/html/index.nginx-debian.html',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World!',
}

file_line { 'redirect-setting':
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Service['nginx'],
}

file { '/var/www/html/error_404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}

file_line { '404-page-setting':
  path    => '/etc/nginx/sites-available/default',
  line    => 'error_page 404 /error_404.html;',
  require => Service['nginx'],
}

file_line { 'custom-response-header':
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  match   => 'server_name',
  require => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => [
    File_line['redirect-setting'],
    File_line['404-page-setting'],
    File_line['custom-response-header'],
  ],
  subscribe => [
    File['/var/www/html/index.nginx-debian.html'],
    File['/var/www/html/error_404.html'],
  ],
}

