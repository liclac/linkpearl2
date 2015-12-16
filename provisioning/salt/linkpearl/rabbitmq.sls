linkpearl_rabbitmq:
  rabbitmq_user.present:
    - name: {{ pillar['linkpearl']['rabbitmq_user'] }}
    - password: {{ pillar['linkpearl']['rabbitmq_pass'] }}
    - perms:
      - '/':
        - '.*'
        - '.*'
        - '.*'
