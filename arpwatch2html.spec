Summary:	Convert the arpwatch flat-file into html
Name:		arpwatch2html
Version:	0.9
Release:	8
License:	GPL
Group:		System/Base
URL:		http://sisms.no-ip.com/software/arpwatch2html/
Source0:	arpwatch2html.pl.bz2
Requires:	arpwatch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
arpwatch2html is a script to convert the arpwatch flat-file
database into a nice looking HTML page. It can sort arpwatch
entries by time, MAC address, IP address, or host name. Users can
select which fields from the address pairing database are to be
shown, and can omit old entries. It can also show the most recent
messages sent by arpwatch to the syslog daemon. 

%prep

%setup -q -T -c -n %{name}-%{version}
bzcat %{SOURCE0} > arpwatch2html.pl
perl -pi -e "s|/var/arpwatch|/var/lib/arpwatch|g" arpwatch2html.pl

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 arpwatch2html.pl %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-7mdv2011.0
+ Revision: 616605
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.9-6mdv2010.0
+ Revision: 423958
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-5mdv2009.0
+ Revision: 238955
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9-4mdv2008.0
+ Revision: 83866
- rebuild


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9-3mdv2007.0
+ Revision: 101572
- misc spec file fixes
- Import arpwatch2html

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdk
- rebuild

* Sat Nov 20 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9-1mdk
- initial mandrake package

