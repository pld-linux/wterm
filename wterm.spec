Summary:	Terminal emulator for WindowMaker
Summary(pl):	Emulator terminala dla WindowMakera
Name:		wterm
Version:	6.2.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://largo.windowmaker.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	09ec12901333ad51aeca2ecd8c88730d
URL:		http://largo.windowmaker.org/files.php#wterm
BuildRequires:	WindowMaker-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wterm is a rxvt clone designed for WindowMaker. It has some
interesting featrues like very fast transparency or transparent NeXT
scroll bar.

%description -l pl
Wterm to klon rxvt stworzony specjalnie z my¶l± o WindowMakerze.
Oferuje wiele interesuj±cych funkcji, takich jak bardzo szybka obsluga
przezroczystosci t³a czy przezroczysty pasek przewijania typu NeXT.

%prep
%setup -q 

%build
%configure2_13 \
	--enable-transparency \
	--enable-next-scroll \
	--enable-ttygid \
	--enable-xpm-background \
	--enable-menubar \
	--enable-wtmp \
	--enable-utmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{BUGS,FAQ,README*,TODO}
%attr(755,root,root) %{_bindir}/wterm
%{_mandir}/man1/wterm.1*
