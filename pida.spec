Summary:	A framework for integrated development
Summary(pl.UTF-8):	Szkielet do programowania zintegrowanego
Name:		pida
Version:	0.3.1
Release:	0.2
License:	GPL
Group:		Development/Tools
Source0:	http://download.berlios.de/pida/%{name}-%{version}.tar.gz
# Source0-md5:	dca8a7d8b92ee7619992b26aa9dd6186
Source1:	%{name}.desktop
URL:		http://pida.berlios.de/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-gnome-desktop-gtksourceview
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PIDA is an integrated development environment (IDE) for UNIX-like
operating systems.

Unique Features:
- Vim embedding
- File browser that understands version status information for CVS,
  Subversion, Darcs, Monotone, Mercurial, Bazaar-ng and Arch
- Built in GTK+ rapid application development
- Many more unique and obsessive touches

%description -l pl.UTF-8
PIDA to zintegrowane środowisko programistyczne (IDE) dla uniksowych
systemów operacyjnych.

Unikalne cechy:
- osadzony Vim
- przeglądarka plików uwzględniająca informacje o stanie wersji dla
  systemów kontroli wersji CVS, Subversion, Darcs, Monotone, Mercurial,
  Bazaar-ng i Arch
- wbudowane środowisko szybkiego tworzenia aplikacji GTK+
- wiele innych unikalnych i pożądanych drobiazgów

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python setup.py install \
	--install-data=%{_datadir}/%{name} \
	--single-version-externally-managed \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/pida-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/html/* AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
