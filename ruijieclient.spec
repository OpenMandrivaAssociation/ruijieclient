Summary:	A ruijie network supplicant for GNU/Linux
Name:		ruijieclient
Version:	0.7.0
Release:	%mkrel 1
License:	LGPLv3+
Group:		System/Servers
URL:		http://code.google.com/p/ruijieclient/
Source:		http://ruijieclient.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	ruijie.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libpcap-devel

%description
RuijieClient is a ruijie network supplicant for GNU/Linux which is based
on mystar, but re-writed form scratch.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -fr %buildroot%_datadir/doc

install -D %{SOURCE1} -m0644 %buildroot%_sysconfdir/ruijie.conf

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{_bindir}/ruijieclient
%config(noreplace) %_sysconfdir/ruijie.conf


%changelog
* Sun Jun 14 2009 Funda Wang <fundawang@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 385862
- import ruijieclient


