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
  dracut_install sort
  dracut_install awk
  dracut_install basename
  dracut_install date
  dracut_install cut
}
