base:
  '*':
    - common
    - python
    - dotdeb
    - linkpearl.libraries

  'roles:db':
    - match: grain
    - postgres
    - redis
    - memcached
    - rabbitmq.server
    - linkpearl.database

  'roles:worker':
    - match: grain
    - rabbitmq.client
