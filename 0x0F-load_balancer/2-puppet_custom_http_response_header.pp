exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure => 'installed',
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By $hostname;',
  match => 'http {',
  notify => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['http_header'],
}
