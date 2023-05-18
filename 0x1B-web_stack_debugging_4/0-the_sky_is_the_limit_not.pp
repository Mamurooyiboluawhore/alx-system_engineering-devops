# a puppet script that changes ulimit

exec { '/etc/default/nginx':
  command => "sed -i 's/15/3028/g' /etc/default/nginx",
  path => "/usr/local/bin/:/bin/"
}
exec { 'nginx_restart':
  command => "nginx restart",
  path => "/etc/init.d/"
}  
