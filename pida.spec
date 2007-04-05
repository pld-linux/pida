# TODO:
# - investigate the documentation format in doc
# - package only py[co] files
# - verify if such a big version jump actually works
#
Summary:	A framework for integrated development
Summary(pl.UTF-8):	Szkielet do programowania zintegrowanego
Name:		pida
Version:	0.4.4
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://pida.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	462542ce70b47d16a019b403b741a411
Source1:	%{name}.desktop
URL:		http://pida.berlios.de/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-gnome-desktop-gtksourceview
Requires:	python-vte
Requires:	python-kiwi
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

cp $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/data/icons/pida-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
