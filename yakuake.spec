Summary:	Very powerful Quake style Konsole
Summary(de.UTF-8):	Ein Quake ähnlicher Konsole Emulator
Summary(pl.UTF-8):	Rozbudowany emulator terminala w stylu Quake
Name:		yakuake
Version:	2.8
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/yakuake/%{name}-%{version}.tar.bz2
# Source0-md5:	595f704fd098db01b29b16329a598cb2
Patch0:		%{name}-desktop.patch
URL:		http://extragear.kde.org/apps/yakuake/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
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
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
		--enable-libsuffix=64 \
%endif
		--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
		--with-qt-libraries=%{_libdir}

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} install \
	xdg_appsdir=%{_desktopdir} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/yakuake
%{_desktopdir}/*.desktop
%dir %{_datadir}/apps/yakuake
%dir %{_datadir}/apps/yakuake/*
%{_datadir}/apps/yakuake/*/tabs.skin
%{_datadir}/apps/yakuake/*/icon.png
%dir %{_datadir}/apps/yakuake/*/tabs
%{_datadir}/apps/yakuake/*/tabs/*.png
%{_datadir}/apps/yakuake/*/title.skin
%dir %{_datadir}/apps/yakuake/*/title
%{_datadir}/apps/yakuake/*/title/*.png
%{_datadir}/config.kcfg/*.kcfg
%{_iconsdir}/hicolor/*x*/apps/yakuake.png
