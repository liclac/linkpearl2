memcached:
  pkg.installed:
    - pkgs:
      - memcached
      - libmemcached11
      - libmemcached-dev
  service.running:
    - enable: True
    - require:
      - pkg: memcached
    - watch:
      - file: /etc/memcached.conf

/etc/memcached.conf:
  file.managed:
    - source: salt://memcached/memcached.conf
    - require:
      - pkg: memcached
