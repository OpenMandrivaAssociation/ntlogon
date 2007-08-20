%define name    ntlogon
%define version 0.8b
%define release %mkrel 1

Summary: Autogenerator for NT logon scripts
Name: %name
Version: %version
Release: %release
Source0: %name-%version.tar.bz2
URL: http://www.craigelachie.org/rhacer/ntlogon/
License: GPL
Group: Networking/Other
BuildRoot: %_tmppath/%name-buildroot
BuildArch: noarch

%description
NTLogon is a Python script that generates Samba/NT-logon scripts from an
easy-to-modify configuration file. It currently understands the Samba
macros for User, Group and Architecture. The configuration file looks like
a cross between an INI file and a DOS batchfile, so most Windows users
will feel somewhat comfortable with it.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -c -n %{name}-%{version}

%build
# no build for no arch ... no build for no arch ...

%install
mkdir -p $RPM_BUILD_ROOT{%{_prefix}/bin,/etc}/
install -m 755 ntlogon.py   $RPM_BUILD_ROOT%_bindir/ntlogon
install -m 644 ntlogon.conf $RPM_BUILD_ROOT%_sysconfdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/*
%config(noreplace) %_sysconfdir/*

