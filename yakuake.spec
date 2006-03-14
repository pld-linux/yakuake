Summary:	Very powerful Quake style Konsole
Summary(pl):	Rozbudowany emulator terminala w stylu Quake
Name:		yakuake
Version:	2.7.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.softpedia.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	98576f75c94f75756ef4acb18ef93a5e
Patch0:		%{name}-desktop.patch
URL:		http://yakuake.uv.ro/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	qt-st
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE konsole which looks like those found in Quake.

%description -l pl
Konsola KDE wygl±dem przypominaj±ca tê z Quake.

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
rm -rf $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}}/yakuake.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/yakuake
%{_desktopdir}/*.desktop
%dir %{_datadir}/apps/yakuake
%dir %{_datadir}/apps/yakuake/default
%{_datadir}/apps/yakuake/default/tabs.skin
%dir %{_datadir}/apps/yakuake/default/tabs
%{_datadir}/apps/yakuake/default/tabs/*.png
%{_datadir}/apps/yakuake/default/title.skin
%dir %{_datadir}/apps/yakuake/default/title
%{_datadir}/apps/yakuake/default/title/*.png
%{_datadir}/apps/yakuake/default/install.sh
%{_datadir}/apps/yakuake/default/manual.readme
%{_iconsdir}/hicolor/16x16/apps/yakuake.png
%{_iconsdir}/hicolor/32x32/apps/yakuake.png
