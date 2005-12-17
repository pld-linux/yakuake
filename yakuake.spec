Name:		yakuake
Summary:	Very powerful Quake style Konsole
Summary(pl):	Rozbudowany emulator terminala w stylu Quake
Version:	2.7.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.softpedia.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	98576f75c94f75756ef4acb18ef93a5e
Patch0:		%{name}-po.patch
URL:		http://yakuake.uv.ro/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE konsole which looks like those found in Quake.

%description -l pl
Konsola KDE wygl�dem przypominaj�ca t� z Quake.

%prep
%setup -q
%patch0 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING AUTHORS
%attr(755,root,root) %{_bindir}/yakuake
#%{_menudir}/%{name}
%{_datadir}/applnk/Utilities/yakuake.desktop
%{_datadir}/apps/yakuake/default/tabs.skin
%{_datadir}/apps/yakuake/default/tabs/*.png
%{_datadir}/apps/yakuake/default/title.skin
%{_datadir}/apps/yakuake/default/title/*.png
%{_datadir}/apps/yakuake/default/install.sh
%{_datadir}/apps/yakuake/default/manual.readme
%{_iconsdir}/hicolor/16x16/apps/yakuake.png
%{_iconsdir}/hicolor/32x32/apps/yakuake.png
