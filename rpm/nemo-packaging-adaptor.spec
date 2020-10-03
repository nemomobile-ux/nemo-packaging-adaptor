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


%package gstreamer-plugins-good
Summary:    Matching requirements by Mer to Fedora: GStreamer Plugins Good
Group:      Configs
Requires:   gstreamer1-plugins-good >= 1.16.0
Provides:   gstreamer1.0-plugins-good = 1.16.0
BuildArch:  noarch

%description gstreamer-plugins-good
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
Requires:   pkgconfig(Qt5) >= 5.12.0
Requires:   pkgconfig(Qt5Core) >= 5.12.0
Provides:   qt5-qmake = 5.12.0
Provides:   qt5-tools = 5.12.0
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


%prep
%setup -q -n %{name}-%{version}

%install

install -D README.md %{buildroot}/%{_docdir}/%{name}-bluez-libs-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-gstreamer-plugins-good/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-swi-prolog/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-base-gui/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-help-devel/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-linguist/README.md

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

%files gstreamer-plugins-good
%defattr(-,root,root,-)
%{_docdir}/%{name}-gstreamer-plugins-good

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
