Summary:	Convert the arpwatch flat-file into html
Name:		arpwatch2html
Version:	0.9
Release:	%mkrel 4
License:	GPL
Group:		System/Base
URL:		http://sisms.no-ip.com/software/arpwatch2html/
Source0:	arpwatch2html.pl.bz2
Requires:	arpwatch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
