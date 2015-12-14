redis-server:
  pkg.installed:
    - require:
      - pkgrepo: dotdeb
  service.running:
    - enable: True
    - require:
      - pkg: redis-server
