Name:		jurt
Summary:	A package builder
Version:	0.01
Release:	1
Source0:	jurt-0.01.tar.gz
URL:		http://gitorious.org/jurt
Group:		Development/Python
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildArch:	noarch
License:	GPLv2

BuildRequires:	python
BuildRequires:	python-devel

Requires:	python
Requires:	sudo

%description
Jurt is a package builder.

%prep
%setup -q

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root=%buildroot
install -d %buildroot/%_sbindir/
mv %buildroot/%_bindir/jurt-{root-command,setup} %buildroot/%_sbindir/

install -d %buildroot/%_var/spool/jurt/builds/
install -m 1770 -d %buildroot/%_var/spool/jurt/builds/spools/
install -m 1770 -d %buildroot/%_var/spool/jurt/builds/logs/
install -m 1770 -d %buildroot/%_var/spool/jurt/builds/fail/
install -m 1770 -d %buildroot/%_var/spool/jurt/builds/success/
install -m 1770 -d %buildroot/%_var/spool/jurt/chroots/
install -m 0770 -d %buildroot/%_var/spool/jurt/chroots/cached

%clean
%__rm -rf %buildroot

%pre
%_pre_useradd jurt /var/empty /sbin/nologin

%postun
%_postun_userdel jurt

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %_sysconfdir/jurt/jurt.conf
%{py_sitedir}/*
%_sbindir/jurt-root-command
%_sbindir/jurt-setup
%_bindir/jurt
%_bindir/jurt-build
%_bindir/jurt-shell
%_bindir/jurt-put
%_bindir/jurt-showrc
%_bindir/jurt-list-targets
%_bindir/jurt-test-sudo
%attr(1770,root,jurt) %dir %_var/spool/jurt/builds/spools/
%attr(1770,root,jurt) %dir %_var/spool/jurt/builds/logs/
%attr(1770,root,jurt) %dir %_var/spool/jurt/builds/fail/
%attr(1770,root,jurt) %dir %_var/spool/jurt/builds/success/
%attr(1770,root,jurt) %dir %_var/spool/jurt/chroots/
%_var/spool/jurt/chroots/cached/
