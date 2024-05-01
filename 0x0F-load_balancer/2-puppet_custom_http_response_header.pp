exec { 'update-system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update-system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirect-me':
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;',
  match   => 'rewrite ^/redirect_me',
  require => Package['nginx'],
}

file_line { 'add-http-header':
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname;',
  match   => 'rewrite ^/redirect_me',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
