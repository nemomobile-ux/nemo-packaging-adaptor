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

%package qt-linguist
Summary:    Matching requirements by Mer to Fedora: Qt Linguist
Group:      Configs
Requires:   qt-linguist
Provides:   qt5-qttools-linguist
BuildArch:  noarch

%description qt-linguist
%{summary}
 
%prep
%setup -q -n %{name}-%{version}

%install

install -D README.md %{buildroot}/%{_docdir}/%{name}-qt-linguist/README.md

mkdir -p %{buildroot}/%{_bindir}

# linguist
ln -sf lconvert-qt5 %{buildroot}/%{_bindir}/lconvert
ln -sf linguist-qt5 %{buildroot}/%{_bindir}/linguist
ln -sf lrelease-qt5 %{buildroot}/%{_bindir}/lrelease
ln -sf lupdate-qt5 %{buildroot}/%{_bindir}/lupdate

%files qt-linguist
%defattr(-,root,root,-)
%{_bindir}/lconvert
%{_bindir}/linguist
%{_bindir}/lrelease
%{_bindir}/lupdate
%{_docdir}/%{name}-qt-linguist
