include:
  - postgres.client

postgresql:
  pkg.installed:
    - pkgs:
      - postgresql-9.4
  service.running:
    - enable: True
    - require:
      - pkg: postgresql
    - watch:
      - file: /etc/postgresql/9.4/main/pg_hba.conf
      - file: /etc/postgresql/9.4/main/postgresql.conf

/etc/postgresql/9.4/main/pg_hba.conf:
  file.managed:
    - source: salt://postgres/pg_hba.conf
    - require:
      - pkg: postgresql

/etc/postgresql/9.4/main/postgresql.conf:
  file.managed:
    - source: salt://postgres/postgresql.conf
    - require:
      - pkg: postgresql

{% if grains.get('vagrant', False) %}
postgresql_vagrant:
  postgres_user.present:
    - name: vagrant
    - superuser: True
    - require:
      - service: postgresql
      - pkg: postgresql-client
{% endif %}

