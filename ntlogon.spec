Summary:	Autogenerator for NT logon scripts
Name:		ntlogon
Version:	0.11.0
Release:	3
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


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.11.0-2mdv2010.0
+ Revision: 440348
- rebuild

* Fri Jan 09 2009 Jérôme Soyer <saispo@mandriva.org> 0.11.0-1mdv2009.1
+ Revision: 327397
- New version

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8b-4mdv2009.0
+ Revision: 239082
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.8b-2mdv2008.0
+ Revision: 70383
- use %%mkrel


* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 0.8b-1mdk
- 0.8b

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.8-6mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.8-5mdk
- rebuild

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.8-4mdk
- same player, try again : fix typo in desc(Yura Gusev)

* Mon Sep 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.8-3mdk
- fix typo in desc(Yura Gusev)

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.8-2mdk
- rebuild
- url

* Wed Aug 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.8-1mdk
- updated to 0.8

* Thu Nov 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.7b-1mdk
- new in contribs
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com> :
	- v0.7b (initial packaging)

