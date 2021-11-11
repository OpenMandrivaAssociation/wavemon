Summary: Wireless network devices monitoring application
Name: wavemon
Version: 0.9.4
Release: 1
Source0: https://github.com/uoaerg/wavemon/archive/v%{version}/%{name}-%{version}.tar.gz
License: GPLv2+
Group: System/Kernel and hardware
Url: http://eden-feed.erg.abdn.ac.uk/wavemon/

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libnl-1)
BuildRequires:  pkgconfig(libcap)

%description
Wavemon is a wireless device monitoring application that allows you to watch
signal and noise levels, packet statistics, device configuration and network
parameters of your wireless network hardware. It has currently only been
tested with the Lucent Orinoco series of cards, although it *should* work 
(though with varying features) with all devices supported by the wireless 
kernel extensions by Jean Tourrilhes <jt@hpl.hp.com>.

%prep
%setup -q
sed -r 's|\?=|=|g' -i Makefile.in

%build

export CFLAGS="%{optflags} `pkg-config --cflags libnl-3.0` -D_REENTRANT -pthread"
#export CC=gcc
#export CXX=g++
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/wavemon
%{_mandir}/man1/wavemon.1*
%{_mandir}/man5/wavemonrc.5*


%changelog
* Wed Mar 16 2011 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 0.7.1-1mdv2011.0
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


* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.0b-3mdk
- Fix BuildRequires

* Sun May 22 2005 Pascal Terjan <pterjan@mandriva.org> 0.4.0b-2mdk
- gcc4 patch

* Fri May  7 2004 Juan Quintela <quintela@mandrakesoft.com> 0.4.0b-1mdk
- 1st mandrake package.
