# TODO:
# - investigate the documentation format in doc
# - verify if such a big version jump actually works
# - move .po files to glibc dir and test if it works
#   are these used afterall, as they are .po sources not .mo compiled
# - moo_stub is just sample? kill it and can make package noarch.
#
%define		realname PIDA
#
Summary:	A framework for integrated development
Summary(pl.UTF-8):	Szkielet do programowania zintegrowanego
Name:		pida
Version:	0.5.1
Release:	5
License:	GPL
Group:		Development/Tools
Source0:	http://pida.googlecode.com/files/%{realname}-%{version}.tar.gz
# Source0-md5:	d24bbdc2c07172062cf55dffe58c85f6
Source1:	%{name}.desktop
URL:		http://pida.berlios.de/
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-gnome-desktop-gtksourceview
Requires:	python-gnome-gconf
Requires:	python-kiwi
Requires:	python-vte
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
%setup -q -n %{realname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

python setup.py install \
	--install-data=%{_datadir}/%{name} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp $RPM_BUILD_ROOT%{py_sitedir}/%{name}/resources/pixmaps/pida-icon.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/pida
%attr(755,root,root) %{_bindir}/pida-remote

# see todo at top of the spec
%dir %{py_sitedir}/pida/resources/locale
%dir %{py_sitedir}/pida/services/appcontroller/locale
%dir %{py_sitedir}/pida/services/buffer/locale
%dir %{py_sitedir}/pida/services/bugreport/locale
%dir %{py_sitedir}/pida/services/commander/locale
%dir %{py_sitedir}/pida/services/editor/locale
%dir %{py_sitedir}/pida/services/filemanager/locale
%dir %{py_sitedir}/pida/services/grepper/locale
%dir %{py_sitedir}/pida/services/help/locale
%dir %{py_sitedir}/pida/services/manhole/locale
%dir %{py_sitedir}/pida/services/notify/locale
%dir %{py_sitedir}/pida/services/openwith/locale
%dir %{py_sitedir}/pida/services/optionsmanager/locale
%dir %{py_sitedir}/pida/services/plugins/locale
%dir %{py_sitedir}/pida/services/project/locale
%dir %{py_sitedir}/pida/services/sessions/locale
%dir %{py_sitedir}/pida/services/shortcuts/locale
%dir %{py_sitedir}/pida/services/versioncontrol/locale
%dir %{py_sitedir}/pida/services/webbrowser/locale
%dir %{py_sitedir}/pida/services/window/locale
%lang(fr) %{py_sitedir}/pida/resources/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/appcontroller/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/buffer/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/bugreport/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/commander/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/editor/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/filemanager/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/grepper/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/help/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/manhole/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/notify/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/openwith/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/optionsmanager/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/plugins/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/project/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/sessions/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/shortcuts/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/versioncontrol/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/webbrowser/locale/fr_FR
%lang(fr) %{py_sitedir}/pida/services/window/locale/fr_FR

%if "%{py_ver}" > "2.4"
%{py_sitedir}/*-*.egg-info
%{py_sitedir}/*-*.egg-info
%{py_sitedir}/*-py2.*.egg-info
%endif

%dir %{py_sitedir}/pida
%attr(755,root,root) %{py_sitedir}/moo_stub.so
%{py_sitedir}/pida/*.py[co]
%{py_sitedir}/pida/core
%{py_sitedir}/pida/editors
%dir %{py_sitedir}/pida/resources
%{py_sitedir}/pida/resources/glade
%{py_sitedir}/pida/resources/pixmaps
%{py_sitedir}/pida/resources/uidef
%dir %{py_sitedir}/pida/services
%dir %{py_sitedir}/pida/services/appcontroller
%{py_sitedir}/pida/services/appcontroller/*.py[co]
%{py_sitedir}/pida/services/appcontroller/service.pida
%{py_sitedir}/pida/services/appcontroller/uidef
%dir %{py_sitedir}/pida/services/buffer
%{py_sitedir}/pida/services/buffer/glade
%{py_sitedir}/pida/services/buffer/*.py[co]
%{py_sitedir}/pida/services/buffer/service.pida
%{py_sitedir}/pida/services/buffer/uidef
%dir %{py_sitedir}/pida/services/bugreport
%{py_sitedir}/pida/services/bugreport/glade
%{py_sitedir}/pida/services/bugreport/*.py[co]
%{py_sitedir}/pida/services/bugreport/service.pida
%{py_sitedir}/pida/services/bugreport/uidef
%dir %{py_sitedir}/pida/services/commander
%{py_sitedir}/pida/services/commander/*.py[co]
%{py_sitedir}/pida/services/commander/service.pida
%{py_sitedir}/pida/services/commander/uidef
%dir %{py_sitedir}/pida/services/contexts
%{py_sitedir}/pida/services/contexts/*.py[co]
%{py_sitedir}/pida/services/contexts/service.pida
%{py_sitedir}/pida/services/contexts/uidef
%dir %{py_sitedir}/pida/services/editor
%{py_sitedir}/pida/services/editor/*.py[co]
%{py_sitedir}/pida/services/editor/service.pida
%dir %{py_sitedir}/pida/services/filemanager
%{py_sitedir}/pida/services/filemanager/*.py[co]
%{py_sitedir}/pida/services/filemanager/service.pida
%{py_sitedir}/pida/services/filemanager/uidef
%dir %{py_sitedir}/pida/services/filewatcher
%{py_sitedir}/pida/services/filewatcher/*.py[co]
%{py_sitedir}/pida/services/filewatcher/service.pida
%dir %{py_sitedir}/pida/services/grepper
%{py_sitedir}/pida/services/grepper/glade
%{py_sitedir}/pida/services/grepper/*.py[co]
%{py_sitedir}/pida/services/grepper/service.pida
%{py_sitedir}/pida/services/grepper/uidef
%dir %{py_sitedir}/pida/services/help
%{py_sitedir}/pida/services/help/*.py[co]
%{py_sitedir}/pida/services/help/service.pida
%{py_sitedir}/pida/services/help/uidef
%dir %{py_sitedir}/pida/services/manhole
%{py_sitedir}/pida/services/manhole/*.py[co]
%{py_sitedir}/pida/services/manhole/service.pida
%{py_sitedir}/pida/services/manhole/uidef
%dir %{py_sitedir}/pida/services/notify
%{py_sitedir}/pida/services/notify/*.py[co]
%{py_sitedir}/pida/services/notify/service.pida
%{py_sitedir}/pida/services/notify/uidef
%dir %{py_sitedir}/pida/services/openwith
%{py_sitedir}/pida/services/openwith/glade
%{py_sitedir}/pida/services/openwith/*.py[co]
%{py_sitedir}/pida/services/openwith/service.pida
%{py_sitedir}/pida/services/openwith/uidef
%dir %{py_sitedir}/pida/services/optionsmanager
%{py_sitedir}/pida/services/optionsmanager/glade
%{py_sitedir}/pida/services/optionsmanager/*.py[co]
%{py_sitedir}/pida/services/optionsmanager/service.pida
%{py_sitedir}/pida/services/optionsmanager/uidef
%dir %{py_sitedir}/pida/services/plugins
%{py_sitedir}/pida/services/plugins/glade
%{py_sitedir}/pida/services/plugins/*.py[co]
%{py_sitedir}/pida/services/plugins/service.pida
%{py_sitedir}/pida/services/plugins/uidef
%dir %{py_sitedir}/pida/services/project
%{py_sitedir}/pida/services/project/glade
%{py_sitedir}/pida/services/project/*.py[co]
%{py_sitedir}/pida/services/project/service.pida
%{py_sitedir}/pida/services/project/uidef
%{py_sitedir}/pida/services/*.py[co]
%dir %{py_sitedir}/pida/services/rpc
%{py_sitedir}/pida/services/rpc/*.py[co]
%{py_sitedir}/pida/services/rpc/service.pida
%dir %{py_sitedir}/pida/services/sessions
%{py_sitedir}/pida/services/sessions/*.py[co]
%{py_sitedir}/pida/services/sessions/service.pida
%{py_sitedir}/pida/services/sessions/uidef
%dir %{py_sitedir}/pida/services/shortcuts
%{py_sitedir}/pida/services/shortcuts/*.py[co]
%{py_sitedir}/pida/services/shortcuts/service.pida
%{py_sitedir}/pida/services/shortcuts/uidef
%dir %{py_sitedir}/pida/services/statusbar
%{py_sitedir}/pida/services/statusbar/*.py[co]
%{py_sitedir}/pida/services/statusbar/service.pida
%dir %{py_sitedir}/pida/services/versioncontrol
%{py_sitedir}/pida/services/versioncontrol/glade
%{py_sitedir}/pida/services/versioncontrol/*.py[co]
%{py_sitedir}/pida/services/versioncontrol/service.pida
%{py_sitedir}/pida/services/versioncontrol/uidef
%dir %{py_sitedir}/pida/services/webbrowser
%{py_sitedir}/pida/services/webbrowser/*.py[co]
%{py_sitedir}/pida/services/webbrowser/service.pida
%{py_sitedir}/pida/services/webbrowser/uidef
%dir %{py_sitedir}/pida/services/window
%{py_sitedir}/pida/services/window/*.py[co]
%{py_sitedir}/pida/services/window/service.pida
%{py_sitedir}/pida/services/window/uidef
%{py_sitedir}/pida/ui
%{py_sitedir}/pida/utils

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
