Name:           btrfsmaintenance
Version:        0.3.1
Release:        2%{?dist}
Summary:        Scripts for btrfs periodic maintenance tasks
License:        GPL-2.0
Group:          System/Base
Url:            https://github.com/kdave/btrfsmaintenance
Source0:        https://github.com/kdave/btrfsmaintenance/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:  systemd
Requires:       btrfs-progs

%description
Scripts for btrfs maintenance tasks like periodic scrub, balance, trim or defrag
on selected mountpoints or directories.

%prep
%setup -q

%build

%install
# fix build error on openSUSE and SLE
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily/
mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly/
mkdir -p %{buildroot}%{_sysconfdir}/cron.monthly/

install -m 755 -d %{buildroot}%{_datadir}/%{name}
#install -m 755 btrfs-defrag.sh %{buildroot}%{_datadir}/%{name}
#install -m 755 btrfs-balance.sh %{buildroot}%{_datadir}/%{name}
#install -m 755 btrfs-scrub.sh %{buildroot}%{_datadir}/%{name}
#install -m 755 btrfs-trim.sh %{buildroot}%{_datadir}/%{name}
install -m 755 btrfs-*.sh %{buildroot}%{_datadir}/%{name}/
install -m644 btrfsmaintenance-functions %{buildroot}%{_datadir}/%{name}
install -m 755 btrfsmaintenance-refresh-cron.sh %{buildroot}%{_datadir}/%{name}

install -m 755 -d %{buildroot}%{_unitdir}
install -m 644 -D btrfsmaintenance-refresh.service %{buildroot}%{_unitdir}
install -m 755 -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbtrfsmaintenance-refresh


install -m 755 -d %{buildroot}%{_sysconfdir}/sysconfig/
install -m 644 sysconfig.btrfsmaintenance %{buildroot}%{_sysconfdir}/sysconfig/%{name}



%files
%defattr(-,root,root)
%doc COPYING README.md btrfsmaintenance.changes
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_unitdir}
%{_unitdir}/btrfsmaintenance-refresh.service
%{_sbindir}/rcbtrfsmaintenance-refresh


%post
%systemd_post btrfsmaintenance-refresh.service
%{_datadir}/%{name}/btrfsmaintenance-refresh-cron.sh

#%pre
#%systemd_pre btrfsmaintenance-refresh.service

%preun
%systemd_preun btrfsmaintenance-refresh.service
%{_datadir}/%{name}/btrfsmaintenance-refresh-cron.sh uninstall

%postun
%systemd_postun btrfsmaintenance-refresh.service


%changelog
* Sun Sep 03 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.3.1-1
- update to version 0.3.1

* Sun Feb 19 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.3-2
- bugfix: missing btrfsmaintenance-functions
- added btrfsmaintenance.changes to docs

* Fri Feb 17 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.3-1
- update to version 0.3

* Mon Aug 29 2016 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2-2.1
- added %config(noreplace) directive on /etc/sysconfig/btrfsmaintanance file

* Mon Aug 29 2016 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2-2
- moved sysconfig.btrfsmaintenance to /etc/sysconfig

* Sat Jul 02 2016 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2-1.1
- removed unexisting scriptlet

* Sat Jul 02 2016 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.2-1
- Initial build
