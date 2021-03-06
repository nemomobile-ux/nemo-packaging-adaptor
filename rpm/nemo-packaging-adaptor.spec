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


%package qt-linguist
Summary:    Matching requirements by Mer to Fedora: Qt Linguist
Group:      Configs
Requires:   qt5-linguist >= 5.12.0
Provides:   qt5-qttools-linguist = 5.12.0
BuildArch:  noarch

%description qt-linguist
%{summary}


%package qt-qmake
Summary:    Matching requirements by Mer to Fedora: Qt5 Qmake and Tools
Group:      Configs
Requires:   qt5-qtbase-devel >= 5.12.0
Provides:   qt5-qmake = 5.12.0
Provides:   qt5-tools = 5.12.0
BuildArch:  noarch

%description qt-qmake
%{summary}


%prep
%setup -q -n %{name}-%{version}

%install

install -D README.md %{buildroot}/%{_docdir}/%{name}-gstreamer-plugins-good/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-swi-prolog/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-linguist/README.md
install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-qmake/README.md

mkdir -p %{buildroot}/%{_bindir}

# linguist
ln -sf lconvert-qt5 %{buildroot}/%{_bindir}/lconvert
ln -sf linguist-qt5 %{buildroot}/%{_bindir}/linguist
ln -sf lrelease-qt5 %{buildroot}/%{_bindir}/lrelease
ln -sf lupdate-qt5 %{buildroot}/%{_bindir}/lupdate

# qmake
ln -sf qmake-qt5 %{buildroot}/%{_bindir}/qmake

%files gstreamer-plugins-good
%defattr(-,root,root,-)
%{_docdir}/%{name}-gstreamer-plugins-good

%files swi-prolog
%defattr(-,root,root,-)
%{_docdir}/%{name}-swi-prolog

%files qt-linguist
%defattr(-,root,root,-)
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_docdir}/%{name}-qt-linguist

%files qt-qmake
%defattr(-,root,root,-)
%{_bindir}/qmake
%{_docdir}/%{name}-qt-qmake
