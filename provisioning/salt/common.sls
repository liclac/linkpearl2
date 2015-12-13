essentials:
  pkg.installed:
    - pkgs:
      - build-essential
      - vim
      - git
      - tmux
      - htop
      - strace
      - ltrace
      - zsh
      - curl

apt-transport-https:
  pkg.installed
