base:
  '*':
    - common
    - python

  'roles:db':
    - match: grain
    - postgres
    - linkpearl.database
