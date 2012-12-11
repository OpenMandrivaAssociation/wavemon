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



%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 645486
- update to new version 0.7.1

* Mon Aug 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.7-1mdv2010.0
+ Revision: 417362
- Update to new version 0.6.7
- Remove old build patches, not needed anymore
- SPEC file clean-ups

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0b-4mdv2009.0
+ Revision: 240162
- rebuild
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode man pages extension
- import wavemon

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Sep 28 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.4.0b-3mdk
- Fix BuildRequires

* Sun May 22 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.0b-2mdk
- gcc4 patch

* Fri May  7 2004 Juan Quintela <quintela@mandrakesoft.com> 0.4.0b-1mdk
- 1st mandrake package.
