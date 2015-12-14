include:
  - rabbitmq._common
  - rabbitmq.client

rabbitmq-server:
  pkg.installed:
    - require:
      - pkgrepo: rabbitmq
  service.running:
    - enable: True
    - require:
      - pkg: rabbitmq-server
