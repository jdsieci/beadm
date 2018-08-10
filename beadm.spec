Name:           zfs-beadm
Version:        1.0.1
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


%prep
%setup -q

%build
cp -f src/beadm.1 .
gzip beadm.1

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}
install -pm 755 src/beadm %{buildroot}%{_sbindir}/
install -pm 644 src/beadm.conf %{buildroot}%{_sysconfdir}/
install -D -pm 644 beadm.1.gz %{buildroot}%{_mandir}/man1/beadm.1.gz
install -D -pm 644 src/dracut.conf.d/90-zfs-beadm.conf %{buildroot}%(pkg-config --variable=dracutconfdir dracut)/90-zfs-beadm.conf


%files
%defattr(-,root,root,-)
%{_sbindir}/beadm
%{_mandir}/man1/beadm.1.gz
%{_sysconfdir}/beadm.conf

%files dracut
%defattr(-,root,root,-)
%(pkg-config --variable=dracutconfdir dracut)/90-zfs-beadm.conf

%changelog
* Fri Aug 10 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.1-2
- Added missing dependency for dracut subpackage

* Thu Aug 09 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.1-1
- Update to version 1.0.1

* Wed Aug 08 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.0-1
- Initial build
