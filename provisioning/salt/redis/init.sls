redis-server:
  pkg.installed:
    - require:
      - pkgrepo: dotdeb
  service.running:
    - enable: True
    - require:
      - pkg: redis-server
    - watch:
      - file: /etc/redis/redis.conf

/etc/redis/redis.conf:
  file.managed:
    - source: salt://redis/redis.conf
    - require:
      - pkg: redis-server
