Summary:	Autogenerator for NT logon scripts
Name:		ntlogon
Version:	0.11.0
Release:	%mkrel 3
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

mkdir -p %{buildroot}{%{_prefix}/bin,/etc,%{_datadir}/doc/%{name}}
install -m 755 %{name}-%{version}/ntlogon.py   %{buildroot}%{_bindir}/ntlogon
install -m 644 %{name}-%{version}/ntlogon.conf %{buildroot}%{_sysconfdir}
install -m 644 %{name}-%{version}/CHANGES %{buildroot}%{_datadir}/doc/%{name}
install -m 644 %{name}-%{version}/LICENSE %{buildroot}%{_datadir}/doc/%{name}
install -m 644 %{name}-%{version}/PKG-INFO %{buildroot}%{_datadir}/doc/%{name}
install -m 644 %{name}-%{version}/README %{buildroot}%{_datadir}/doc/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{name}-%{version}/CHANGES %{name}-%{version}/LICENSE %{name}-%{version}/PKG-INFO %{name}-%{version}/README
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
