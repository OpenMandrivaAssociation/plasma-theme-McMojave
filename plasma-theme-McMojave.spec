%define circle_version 2020-10-11

Name: plasma-theme-McMojave
Summary: Plasma theme resembling macOS
Version: 2020.07.09
Release: 1
# Similar theme exists at https://github.com/zayronxio/Plasma-MojaveCT
Source0: https://github.com/vinceliuice/McMojave-kde/archive/master/McMojave-kde-%(echo %{version} | sed -e 's/\./-/g').tar.gz
Source1: https://github.com/vinceliuice/McMojave-circle/archive/master/McMojave-circle-%{circle_version}.tar.gz
# Let's add a fitting mouse cursor theme...
Source2: https://github.com/douglascomim/MacOSMOD/archive/master/MacOSMOD-2020.01.13.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch
Requires: qt-theme-kvantum
# McMojave falls back to Numix-Circle for icons that aren't part of
# McMojave, but it's an optional fallback
Suggests: icon-theme-numix
# To replace the copyrighted (cr)Apple logo
BuildRequires: distro-release-theme

%description
Plasma theme resembling macOS.

%prep
%autosetup -p1 -n McMojave-kde-%(echo %{version} | sed -e 's/\./-/g') -a 1
tar xf %{S:2}
# Replace per-user install paths with system wide paths
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh

cd McMojave-circle-%{circle_version}
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh
sed -i -e 's,gtk-update-icon-cache,# gtk-update-icon-cache,g' install.sh

# Teach McMojave that Falkon is a browser
ln -s browser.svg links/apps/scalable/falkon.svg

# Replace copyrighted logo
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg src/apps/scalable/preferences-desktop-icons.svg
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg src/places/symbolic/start-here-symbolic.svg
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg src/places/16/folder-apple.svg
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg src/status/22/start-here-symbolic.svg
cd ..
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg plasma/desktoptheme/McMojave/icons/
gzip -9 plasma/desktoptheme/McMojave/icons/openmandriva.svg
mv -f plasma/desktoptheme/McMojave/icons/openmandriva.svg.gz plasma/desktoptheme/McMojave/icons/start.svgz
cp -f plasma/desktoptheme/McMojave/icons/start.svgz plasma/desktoptheme/McMojave-light/icons/
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg plasma/look-and-feel/com.github.vinceliuice.McMojave/contents/splash/images/logo.svg
cp -f %{_datadir}/icons/hicolor/scalable/apps/openmandriva.svg plasma/look-and-feel/com.github.vinceliuice.McMojave-light/contents/splash/images/logo.svg

%build
# Nothing to do...

%install
./install.sh
cd McMojave-circle-%{circle_version}
./install.sh
cd ..

# Let's not depend on gnome stuff too much...
sed -i -e 's|Adwaita|breeze,Adwaita|g' %{buildroot}%{_datadir}/icons/McMojave-circle/index.theme
sed -i -e 's|Adwaita|breeze-dark,Adwaita|g' %{buildroot}%{_datadir}/icons/McMojave-circle-dark/index.theme

# Add the mouse cursors
cp -a MacOSMOD-master/cursors %{buildroot}%{_datadir}/icons/McMojave-circle/
cp -a MacOSMOD-master/index.theme %{buildroot}%{_datadir}/icons/McMojave-circle/cursor.theme
ln -s ../McMojave-circle/cursors %{buildroot}%{_datadir}/icons/McMojave-circle-dark/
ln -s ../McMojave-circle/cursor.theme %{buildroot}%{_datadir}/icons/McMojave-circle-dark/

%files
%license LICENSE
%{_datadir}/aurorae/themes/*
%{_datadir}/plasma/desktoptheme/*
%{_datadir}/color-schemes/*
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave-light
%{_datadir}/icons/McMojave-circle
%{_datadir}/icons/McMojave-circle-dark
%{_datadir}/plasma/layout-templates/contents/layout.js
%{_datadir}/plasma/layout-templates/metadata.desktop
%{_datadir}/plasma/layout-templates/org.github.desktop.McMojavePanel
%{_datadir}/wallpapers/McMojave-light
%{_datadir}/wallpapers/McMojave
