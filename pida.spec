Summary:	A framework for integrated development
Summary(pl):	Szkielet do programowania zintegrowanego
Name:		pida
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://download.berlios.de/pida/%{name}-%{version}.tar.gz
# Source0-md5:	dca8a7d8b92ee7619992b26aa9dd6186
URL:		http://pida.vm.bytemark.co.uk/projects/pida
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
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

%description -l pl
PIDA to zintegrowane ¶rodowisko programistyczne (IDE) dla uniksowych
systemów operacyjnych.

Unikalne cechy:
- osadzony Vim
- przegl±darka plików uwzglêdniaj±ca informacje o stanie wersji dla
  systemów kontroli wersji CVS, Subversion, Darcs, Monotone, Mercurial,
  Bazaar-ng i Arch
- wbudowane ¶rodowisko szybkiego tworzenia aplikacji GTK+
- wiele innych unikalnych i po¿±danych drobiazgów

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--install-data=%{_datadir}/%{name} \
	--single-version-externally-managed \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/html/* AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_datadir}/%{name}
