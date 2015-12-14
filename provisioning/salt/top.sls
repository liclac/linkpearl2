base:
  '*':
    - common
    - python

  'roles:db':
    - match: grain
    - postgres
    - rabbitmq.server
    - linkpearl.database

  'roles:worker':
    - match: grain
    - rabbitmq.client
