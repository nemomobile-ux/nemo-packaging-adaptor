Name:       nemo-packaging-adaptor
Summary:    Helper packages for matching requirements by Mer to Fedora
Version:    0.1
Release:    0
Group:      Configs
License:    MIT
URL:        https://github.com/nemomobile-ux/nemo-packaging-adaptor
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch

%description
%{summary}


%package bluez-libs-devel
Summary:    Matching requirements by Mer to Fedora: Bluez5 devel libs
Group:      Configs
Requires:   pkgconfig(bluez) >= 5.54
Provides:   pkgconfig(bluez5) = 5.54
Provides:   bluez5-libs-devel = 5.54
BuildArch:  noarch

%description bluez-libs-devel
%{summary}


%package glibc-private
Summary:    Matching requirements by Mer to Fedora: Glibc Private
Group:      Configs
Requires:   glibc
Provides:   libc.so.6(GLIBC_PRIVATE)
BuildArch:  noarch

%description glibc-private
%{summary}


%package gstreamer-plugins-good
Summary:    Matching requirements by Mer to Fedora: GStreamer Plugins Good
Group:      Configs
Requires:   gstreamer1-plugins-good >= 1.16.0
Provides:   gstreamer1.0-plugins-good = 1.16.0
BuildArch:  noarch

%description gstreamer-plugins-good
%{summary}


%package iptables
Summary:    Matching requirements by Mer to Fedora: IP tables
Group:      Configs
Requires:   iptables >= 1.8.4
Provides:   iptables-ipv6 = 1.8.4
BuildArch:  noarch

%description iptables
%{summary}


%package swi-prolog
Summary:    Matching requirements by Mer to Fedora: Prolog
Group:      Configs
Requires:   pl >= 8.0
Provides:   swi-prolog = 8.0
Provides:   swi-prolog-library = 8.0
Provides:   swi-prolog-library-core = 8.0
BuildArch:  noarch

%description swi-prolog
%{summary}


%package qt-base
Summary:    Matching requirements by Mer to Fedora: Qt Base
Group:      Configs
Requires:   qt5-qtbase >= 5.12.0
Provides:   qt5-plugin-sqldriver-sqlite = 5.12.0
BuildArch:  noarch

%description qt-base
%{summary}


%package qt-base-devel
Summary:    Matching requirements by Mer to Fedora: Qt Base Development Tools
Group:      Configs
Requires:   qt5-qtbase-private-devel >= 5.12.0
Requires:   pkgconfig(Qt5) >= 5.12.0
Requires:   pkgconfig(Qt5Core) >= 5.12.0
Requires:   pkgconfig(Qt5Gui) >= 5.12.0
Requires:   pkgconfig(Qt5Network) >= 5.12.0
Provides:   qt5-qmake = 5.12.0
Provides:   qt5-tools = 5.12.0
Provides:   qt5-qtcore-devel = 5.12.0
Provides:   qt5-qtgui-devel = 5.12.0
Provides:   qt5-qtnetwork-devel = 5.12.0
Provides:   qt5-qtplatformsupport-devel = 5.12.0
BuildArch:  noarch

%description qt-base-devel
%{summary}


%package qt-base-gui
Summary:    Matching requirements by Mer to Fedora: Qt Base Gui
Group:      Configs
Requires:   qt5-qtbase-gui >= 5.12.0
Provides:   qt5-plugin-platform-minimal = 5.12.0
BuildArch:  noarch

%description qt-base-gui
%{summary}


%package qt-dbus-devel
Summary:    Matching requirements by Mer to Fedora: Qt DBus
Group:      Configs
Requires:   pkgconfig(Qt5DBus) >= 5.13.0
Provides:   qt5-qtdbus-devel = 5.13
BuildArch:  noarch

%description qt-dbus-devel
%{summary}


%package qt-declarative-devel
Summary:    Matching requirements by Mer to Fedora: Qt Declarative
Group:      Configs
Requires:   pkgconfig(Qt5Quick) >= 5.13.0
Provides:   qt5-qtdeclarative-qtquick-devel = 5.13
BuildArch:  noarch

%description qt-declarative-devel
%{summary}


%package qt-help-devel
Summary:    Matching requirements by Mer to Fedora: Qt Help Tools
Group:      Configs
Requires:   pkgconfig(Qt5Help) >= 5.12.0
Provides:   qt5-qttools-qthelp-devel = 5.12.0
BuildArch:  noarch

%description qt-help-devel
%{summary}


%package qt-linguist
Summary:    Matching requirements by Mer to Fedora: Qt Linguist
Group:      Configs
Requires:   qt5-linguist >= 5.12.0
Provides:   qt5-qttools-linguist = 5.12.0
BuildArch:  noarch

%description qt-linguist
%{summary}


%package qt-multimedia
Summary:    Matching requirements by Mer to Fedora: Qt Multimedia
Group:      Configs
Requires:   qt5-qtmultimedia >= 5.12.0
Provides:   qt5-qtmultimedia-gsttools = 5.12.0
BuildArch:  noarch

%description qt-multimedia
%{summary}


%package qt-wayland-devel
Summary:    Matching requirements by Mer to Fedora: Qt Wayland
Group:      Configs
Requires:   pkgconfig(Qt5WaylandCompositor) >= 5.13.0
Requires:   pkgconfig(Qt5WaylandClient) >= 5.13.0
Provides:   qt5-qtwayland-wayland_egl-devel = 5.13
BuildArch:  noarch

%description qt-wayland-devel
%{summary}


%prep
%setup -q -n %{name}-%{version}

%install

install -D README.md %{buildroot}/%{_docdir}/%{name}-bluez-libs-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-glibc-private/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-gstreamer-plugins-good/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-iptables/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-swi-prolog/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base-gui/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-dbus-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-declarative-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-help-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-linguist/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-multimedia/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-wayland-devel/README.md

mkdir -p %{buildroot}/%{_bindir}

# linguist
ln -sf lconvert-qt5 %{buildroot}/%{_bindir}/lconvert
ln -sf linguist-qt5 %{buildroot}/%{_bindir}/linguist
ln -sf lrelease-qt5 %{buildroot}/%{_bindir}/lrelease
ln -sf lupdate-qt5 %{buildroot}/%{_bindir}/lupdate

# qmake as a part of qt base devel
ln -sf qmake-qt5 %{buildroot}/%{_bindir}/qmake

%files bluez-libs-devel
%defattr(-,root,root,-)
%{_docdir}/%{name}-bluez-libs-devel

%files glibc-private
%defattr(-,root,root,-)
%{_docdir}/%{name}-glibc-private

%files gstreamer-plugins-good
%defattr(-,root,root,-)
%{_docdir}/%{name}-gstreamer-plugins-good

%files iptables
%defattr(-,root,root,-)
%{_docdir}/%{name}-iptables

%files swi-prolog
%defattr(-,root,root,-)
%{_docdir}/%{name}-swi-prolog

%files qt-base
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-base

%files qt-base-devel
%defattr(-,root,root,-)
%{_bindir}/qmake
%{_docdir}/%{name}-qt-base-devel

%files qt-base-gui
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-base-gui

%files qt-dbus-devel
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-dbus-devel

%files qt-declarative-devel
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-declarative-devel

%files qt-help-devel
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-help-devel

%files qt-linguist
%defattr(-,root,root,-)
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_docdir}/%{name}-qt-linguist

%files qt-multimedia
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-multimedia

%files qt-wayland-devel
%defattr(-,root,root,-)
%{_docdir}/%{name}-qt-wayland-devel
