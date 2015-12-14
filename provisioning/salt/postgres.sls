postgresql:
  pkg.installed:
    - pkgs:
      - postgresql-9.4
      - libpq-dev
  service.running:
    - enable: True
    - require:
      - pkg: postgresql

{% if grains.get('vagrant', False) %}
postgresql_vagrant:
  postgres_user.present:
    - name: vagrant
    - superuser: True
{% endif %}

