Name: plasma-theme-McMojave
Summary: Plasma theme resembling macOS
Version: 2020.01.13
Release: 2
Source0: https://github.com/vinceliuice/McMojave-kde/archive/master/McMojave-kde-%{version}.tar.gz
Source1: https://github.com/vinceliuice/McMojave-circle/archive/master/McMojave-circle-%{version}.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildArch: noarch
Requires: qt-theme-kvantum
# McMojave falls back to Numix-Circle for icons that aren't part of
# McMojave, but it's an optional fallback
Suggests: icon-theme-numix
# To replace the copyrighted (cr)Apple logo
BuildRequires: distro-theme-OpenMandriva

%description
Plasma theme resembling macOS

%prep
%autosetup -p1 -n McMojave-kde-master -a 1
# Replace per-user install paths with system wide paths
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh

cd McMojave-circle-master
sed -i -e 's,\$HOME/.local,%{buildroot}%{_prefix},g' install.sh
sed -i -e 's,gtk-update-icon-cache,# gtk-update-icon-cache,g' install.sh

# Replace copyrighted logo
cp -f %{_datadir}/icons/openmandriva.svg src/apps/scalable/preferences-desktop-icons.svg

# And teach McMojave that Falkon is a browser
ln -s browser.svg links/apps/scalable/falkon.svg

%build
# Nothing to do...

%install
./install.sh
cd McMojave-circle-master
./install.sh

# Let's not depend on gnome stuff too much...
sed -i -e 's|Adwaita|breeze,Adwaita|g' %{buildroot}%{_datadir}/icons/McMojave-circle/index.theme
sed -i -e 's|Adwaita|breeze-dark,Adwaita|g' %{buildroot}%{_datadir}/icons/McMojave-circle-dark/index.theme


%files
%license LICENSE
%{_datadir}/aurorae/themes/*
%{_datadir}/plasma/desktoptheme/*
%{_datadir}/color-schemes/*
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave
%{_datadir}/plasma/look-and-feel/com.github.vinceliuice.McMojave-light
%{_datadir}/icons/McMojave-circle
%{_datadir}/icons/McMojave-circle-dark
