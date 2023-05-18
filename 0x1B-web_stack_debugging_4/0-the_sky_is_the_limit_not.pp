#a puppet script that changes ulimit
exec { 'change_ulimit':
  command => "sed -i 's/15/3028/' /etc/default/nginx",
  path => "/usr/local/bin/:/bin/"
}->

#Restart nginx
exec { 'nginx_restart':
  command => "nginx restart",
  path => "/etc/init.d/"
}  
