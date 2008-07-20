Summary:	Autogenerator for NT logon scripts
Name:		ntlogon
Version:	0.8b
Release:	%mkrel 4
License:	GPL
Group:		Networking/Other
URL:		http://www.craigelachie.org/rhacer/ntlogon/
Source0:	%name-%version.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
NTLogon is a Python script that generates Samba/NT-logon scripts from an
easy-to-modify configuration file. It currently understands the Samba
macros for User, Group and Architecture. The configuration file looks like
a cross between an INI file and a DOS batchfile, so most Windows users
will feel somewhat comfortable with it.

%prep

%setup -c -n %{name}-%{version}

%build
# no build for no arch ... no build for no arch ...

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_prefix}/bin,/etc}/
install -m 755 ntlogon.py   %{buildroot}%{_bindir}/ntlogon
install -m 644 ntlogon.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
