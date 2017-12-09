%define		_state	stable

Summary:	Very powerful Quake style Konsole
Summary(de.UTF-8):	Ein Quake ähnlicher Konsole Emulator
Summary(pl.UTF-8):	Rozbudowany emulator terminala w stylu Quake
Name:		yakuake
Version:	3.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.kde.org/%{_state}/yakuake/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	f8f43f2f3d99925d8853879ff1eb5826
URL:		http://yakuake.kde.org/
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	ka5-konsole
Obsoletes:	yakuake-split
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
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_localedir}/sr@ijekavian*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/yakuake
%{_datadir}/yakuake
%{_iconsdir}/hicolor/*x*/apps/yakuake.png
/etc/xdg/yakuake.knsrc
%{_desktopdir}/org.kde.yakuake.desktop
%{_datadir}/knotifications5/yakuake.notifyrc
%{_datadir}/metainfo/org.kde.yakuake.appdata.xml
