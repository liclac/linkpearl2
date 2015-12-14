linkpearl:
  postgres_user.present:
    - name: {{ pillar['linkpearl']['db_user'] }}
    - password: {{ pillar['linkpearl']['db_pass'] }}
  postgres_database.present:
    - name: {{ pillar['linkpearl']['db_name'] }}
    - owner: {{ pillar['linkpearl']['db_user'] }}
    - require:
      - postgres_user: linkpearl
