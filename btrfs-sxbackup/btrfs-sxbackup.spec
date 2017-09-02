%if 0%{?rhel} >= 7
%define pythonpkg python34
%endif

%if 0%{?fedora} >= 21
%define pythonpkg python3
%endif

Name:           btrfs-sxbackup
Version:        0.6.11
Release:        1%{?dist}
Summary:        Incremental btrfs snapshot backups with push/pull support via SSH
License:        GPLv2+
URL:            https://github.com/masc3d/btrfs-sxbackup
Source0:        https://github.com/masc3d/btrfs-sxbackup/archive/%{version}/%{name}-%{version}.tar.gz
# Add a manpage. The manpage was sent upstream but rejected, because they want
# to avoid maintaining multiple documentations and generate the manpage from the
# existing documentation instead. Keep the manpage until upstream has found a
# solution. Also see https://github.com/masc3d/btrfs-sxbackup/issues/26.
Patch0:         btrfs-sxbackup-manpages.patch
# Fix missing test suite from setup.py.
Patch1:         btrfs-sxbackup-tests.patch

BuildArch:      noarch
#BuildRequires:  python3-devel
BuildRequires: %{pythonpkg}-devel %{pythonpkg}-setuptools
Requires: %{pythonpkg} btrfs-progs %{pythonpkg}-setuptools

%description
Btrfs snapshot backup utility with push/pull support via SSH, retention, Email
notifications, compression of transferred data, and syslog logging.


%prep
%autosetup -p 1 -n %{name}-%{version}


%build
%py3_build


%install
%py3_install
install -d %{buildroot}/%{_mandir}/man1
install -p -m644 man/* %{buildroot}/%{_mandir}/man1


%check
%{__python3} setup.py test


%files
%doc README.rst
%license LICENSE
%{_bindir}/btrfs-sxbackup
%{python3_sitelib}/*
%{_mandir}/man1/*


%changelog
* Sun Sep 03 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.6.11-1
- Update to 0.6.11

* Sat Jul 02 2016 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 0.6.9-1
- Update to 0.6.9
- Bckwards compability with RHEL7

* Wed Jun 15 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.7-1
- Update to 0.6.7

* Mon Jun 06 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.6-2
- Change license to GPLv2+, add license file

* Sat Jun 04 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.6-1
- Update to 0.6.6

* Fri Jan 01 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-3
- Patch setup.py to run unit tests correctly

* Fri Jan 01 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-2
- Add manpages

* Sat Dec 05 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.9-1
- Update to newest upstream release

* Tue Nov  3 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.5.8-1
- Initial package
