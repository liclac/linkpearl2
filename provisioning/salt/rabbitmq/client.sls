include:
  - rabbitmq._common

rabbitmq-client:
  pkg.installed:
    - pkgs:
      - librabbitmq1
      - librabbitmq-dev
    - require:
      - pkgrepo: rabbitmq
