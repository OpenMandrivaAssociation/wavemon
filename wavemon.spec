%define name wavemon
%define version 0.4.0b
%define release %mkrel 3

Summary: Wireless network devices monitoring application
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch1: wavemon_0.4.0b_exit_arg.patch.bz2
Patch2: wavemon_0.4.0b_make_gcc_happy.patch.bz2
Patch3: wavemon-0.4.0b-gcc4.patch.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.janmorgenstern.de/projects-software.html
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

%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man5}

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/wavemon
%{_mandir}/man1/wavemon.1.bz2
%{_mandir}/man5/wavemonrc.5.bz2


