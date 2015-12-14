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
