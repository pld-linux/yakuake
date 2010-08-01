Summary:	Very powerful Quake style Konsole
Summary(de.UTF-8):	Ein Quake ähnlicher Konsole Emulator
Summary(pl.UTF-8):	Rozbudowany emulator terminala w stylu Quake
Name:		yakuake
Version:	2.9.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/yakuake/%{name}-%{version}.tar.bz2
# Source0-md5:	c5a6d1f50ab9464d62563cdb18d6afb7
URL:		http://yakuake.kde.org/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
# for libkonsolepart
Requires:	kde4-kdebase-konsole
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE konsole which looks like those found in Quake.

%description -l de.UTF-8
Eine KDE Konsole die der aus Quake ähnelt.

%description -l pl.UTF-8
Konsola KDE wyglądem przypominająca tę z Quake.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/yakuake
%{_desktopdir}/kde4/*.desktop
%{_datadir}/apps/yakuake
%{_iconsdir}/hicolor/*x*/apps/yakuake.png
%{_iconsdir}/hicolor/scalable/apps/yakuake.svgz
