base:
  '*':
    - common
    - python
    - dotdeb
    - linkpearl.libraries

  'roles:db':
    - match: grain
    - postgres.server
    - redis
    - memcached
    - rabbitmq.server
    - linkpearl.database
    - linkpearl.rabbitmq

  'roles:worker':
    - match: grain
    - memcached
    - postgres.client
    - rabbitmq.client
    - linkpearl.worker
