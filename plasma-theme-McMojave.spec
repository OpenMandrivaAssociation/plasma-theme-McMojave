Name: plasma-theme-McMojave
Summary: Plasma theme resembling macOS
Version: 2020.01.13
Release: 1
Source0: https://github.com/vinceliuice/McMojave-kde/archive/master/McMojave-kde-%{version}.tar.gz
Source1: https://github.com/vinceliuice/McMojave-circle/archive/master/McMojave-circle-%{version}.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch
Requires: qt-theme-kvantum

%description
Plasma theme resembling macOS

%prep
%autosetup -p1 -n McMojave-kde-master -a 1
# Replace per-user install paths with system wide paths
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh

cd McMojave-circle-master
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh
sed -i -e 's,gtk-update-icon-cache,# gtk-update-icon-cache,g' install.sh

%build
# Nothing to do...

%install
./install.sh
cd McMojave-circle-master
./install.sh

%files
%license LICENSE
%{_datadir}/aurorae/themes/*
%{_datadir}/plasma/desktoptheme/*
%{_datadir}/color-schemes/*
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave-light
%{_datadir}/icons/McMojave-circle
%{_datadir}/icons/McMojave-circle-dark
