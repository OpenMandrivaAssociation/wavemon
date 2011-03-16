%define name wavemon
%define version 0.7.1
%define release %mkrel 1

Summary: Wireless network devices monitoring application
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://eden-feed.erg.abdn.ac.uk/wavemon/stable-releases/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: System/Kernel and hardware
Url: http://eden-feed.erg.abdn.ac.uk/wavemon/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ncurses-devel

%description
Wavemon is a wireless device monitoring application that allows you to watch
signal and noise levels, packet statistics, device configuration and network
parameters of your wireless network hardware. It has currently only been
tested with the Lucent Orinoco series of cards, although it *should* work 
(though with varying features) with all devices supported by the wireless 
kernel extensions by Jean Tourrilhes <jt@hpl.hp.com>.



%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_mandir}/{man1,man5}

%makeinstall
rm %{buildroot}%{_datadir}/{AUTHORS,COPYING,ChangeLog,NEWS,README,THANKS}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/wavemon
%{_mandir}/man1/wavemon.1*
%{_mandir}/man5/wavemonrc.5*
%doc NEWS AUTHORS README THANKS

