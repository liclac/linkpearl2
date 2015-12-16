linkpearl-worker:
  file.managed:
    - name: /etc/systemd/system/linkpearl-worker.service
    - source: salt://linkpearl/linkpearl-worker.service
    - template: jinja
    - mode: 755
  service.running:
    - enable: True
    - watch:
      - file: linkpearl-worker
