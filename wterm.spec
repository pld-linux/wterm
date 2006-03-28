Summary:	Terminal emulator for WindowMaker
Summary(pl):	Emulator terminala dla WindowMakera
Name:		wterm
Version:	6.2.9
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://largo.windowmaker.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	09ec12901333ad51aeca2ecd8c88730d
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://largo.windowmaker.org/files.php#wterm
BuildRequires:	WindowMaker-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wterm is a rxvt clone designed for WindowMaker. It has some
interesting featrues like very fast transparency or transparent NeXT
scroll bar.

%description -l pl
Wterm jest klonem rxvt stworzonym specjalnie z my¶l± o WindowMakerze.
Oferuje wiele interesuj±cych funkcji, takich jak bardzo szybka obs³uga
przezroczysto¶ci t³a czy przezroczysty pasek przewijania typu NeXT.

%prep
%setup -q 

%build
%configure2_13 \
	--enable-transparency \
	--enable-next-scroll \
	--enable-ttygid \
	--enable-xpm-background \
	--with-xpm-library=%{_libdir} \
	--enable-menubar \
	--enable-wtmp \
	--enable-utmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{BUGS,FAQ,README*,TODO}
%attr(755,root,root) %{_bindir}/wterm
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/wterm.1*
