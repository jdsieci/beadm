Name:		beadm
Version:	1.0.0
Release:	1%{?dist}
Summary:	Beadm is used to setup and interact with Boot Environments with ZFS.

Group:		
License:	GPL
URL:		https://github.com/jdsieci/beadm
Source0:	https://github.com/jdsieci/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:	zfs

%description
Beadm is used to setup and interact with Boot Environments with ZFS.
Boot Environments allows the system to be upgraded,
while preserving the old system environment in a separate ZFS dataset.

%prep
%setup -q


%build
cp -f src/beadm.1 %{buildsubdir}/
gzip %{buildsubdir}/beadm.1

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}
install -pm 755 src/beadm %{buildroot}%{_sbindir}/
install -pm 644 beadm.conf %{buildroot}%{_sysconfdir}/
install -D -pm 644 %{buildsubdir}/beadm.1.gz %{buildroot}%{_mandir}/man1/beadm.1.gz

%files
%defattr(-,root,root,-)
%{_sbindir}/beadm
%{_mandir}/man1/beadm.1.gz


%changelog
* Wed Sep 08 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0.0-1
- Initial build
