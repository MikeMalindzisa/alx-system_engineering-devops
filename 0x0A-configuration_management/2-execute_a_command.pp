#create a manifest that kills a process named killmenow.

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}

