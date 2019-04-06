Name:           zfs-beadm
Version:        1.1.10
Release:        2%{?dist}
Summary:        Beadm is used to setup and interact with Boot Environments with ZFS.
Provides:       beadm = %{version}

License:        GPL
URL:            https://github.com/jdsieci/beadm
Source0:        https://github.com/jdsieci/beadm/archive/v%{version}/beadm-%{version}.tar.gz

BuildArch:      noarch
Requires:       zfs


%description
Beadm is used to setup and interact with Boot Environments with ZFS.
Boot Environments allows the system to be upgraded,
while preserving the old system environment in a separate ZFS dataset.


%package dracut
Summary:        Dracut module
BuildRequires:  pkgconfig(dracut)
Requires:       %{name}

%description dracut
This package contains a dracut module used to construct an initramfs
image which is Boot Environments on ZFS aware

%package grub2-tools
Summary:        GRUB2 helper scripts
Requires:       %{name} >= 1.1.0
PreReq:         grub2-tools = 1:2.02

%description grub2-tools
This package contains scripts to generate GRUB2 config with
Boot Environment support.

%post grub2-tools
chmod -x %{_sysconfdir}/grub.d/10_linux

%preun grub2-tools
[[ $1 != 0 ]] && exit 0
chmod +x %{_sysconfdir}/grub.d/10_linux

%prep
%setup -q

%build
cp -f src/beadm.1 .
gzip beadm.1

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}/grub.d
install -pm 755 src/beadm %{buildroot}%{_sbindir}/
install -pm 644 src/beadm.conf %{buildroot}%{_sysconfdir}/
install -D -pm 644 beadm.1.gz %{buildroot}%{_mandir}/man1/beadm.1.gz
install -D -pm 644 src/dracut/90beadm/beadm.conf %{buildroot}%(pkg-config --variable=dracutmodulesdir dracut)/90beadm/beadm.conf
install -pm 755 src/dracut/90beadm/module-setup.sh %{buildroot}%(pkg-config --variable=dracutmodulesdir dracut)/90beadm/
install -pm 755 src/grub.d/* %{buildroot}%{_sysconfdir}/grub.d/

%files
%defattr(-,root,root,-)
%{_sbindir}/beadm
%{_mandir}/man1/beadm.1.gz
%{_sysconfdir}/beadm.conf

%files dracut
%defattr(-,root,root,-)
%(pkg-config --variable=dracutmodulesdir dracut)/90beadm

%files grub2-tools
%defattr(-,root,root,-)
%{_sysconfdir}/grub.d/11_linux_zfs
%{_sysconfdir}/grub.d/15_linux_zfs_be


%changelog
* Sat Apr 06 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.10-2
- Fixed version string

* Thu Apr 04 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.10-1
- Added mounting be to custom path

* Fri Jan 18 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.9-1
- Fixed check if BE already exists before creation

* Sun Jan 13 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.8-1
- Fixed wrong 'or' operator

* Sat Jan 12 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.7-1
- Update to upstream

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.6-1
- Added missing dependencies in dracut module

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.5-1
- Changed order of guard statements and config loading
- Changed initrd beadm config

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.4-1
- Added detection of rootfs for /sysroot when run in initrd

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.3-2.1
- Fixed files permissions in dracut module

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.3-2
- Fixed lack of dracut module files

* Thu Aug 30 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.3-1
- Added dracut module

* Mon Aug 27 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.2-1
- Mount and unmount commands refactored

* Sat Aug 25 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.1-1
- Fixed guard statement preventing removal of active BE

* Thu Aug 23 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.0-2.2
- Fixed file section for grub2-tools subpackage

* Thu Aug 23 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.0-2.1
- Fixed grub2-tools requisite

* Thu Aug 23 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.0-2
- Fixed: package name mismatch
- Added minimal version of beadm for grub2-tools subpackage

* Thu Aug 23 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1.0-1
- Added helper scripts for GRUB2
- FIX: beadm tries umount current be

* Thu Aug 23 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.4-1
- Added printing mountpoint after mounting BE
- Minor bug fixes

* Mon Aug 20 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.3-1
- Added destroying multiple BEs
- All messages writes to stderr
- 'mount' command ends with 0 exit code if BE is mounted

* Mon Aug 13 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.2-1
- Fixed unmounting noninherited mountpoints

* Fri Aug 10 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.1-2
- Added missing dependency for dracut subpackage

* Thu Aug 09 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.1-1
- Update to version 1.0.1

* Wed Aug 08 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.0-1
- Initial build
