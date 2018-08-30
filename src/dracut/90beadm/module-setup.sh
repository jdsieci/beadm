#!/bin/sh


check() {
  test -x /sbin/beadm || return 1
  return 0
}



depends() {
  echo zfs
  return 0
}

install() {
  inst "${moddir}/beadm.conf" "/etc/beadm.conf"
  dracut_install /sbin/beadm
}
