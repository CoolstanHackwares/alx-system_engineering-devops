# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to perform a 301 redirect for /redirect_me
file_line { 'redirect_rule':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/CoolstanHackwares permanent;',
}

# Create an index.html file with the content "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
