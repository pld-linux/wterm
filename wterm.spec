Summary:	Terminal Emulator for WindowMaker
Summary(pl):	Emulator terminala dla WindowMaker'a
Name:		wterm
Version:	6.2.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://largo.windowmaker.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	09ec12901333ad51aeca2ecd8c88730d
URL:		http://largo.windowmaker.org/files.php#wterm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wterm is a rxvt clone designed for WindowMaker. It has some interesting
featrues like very fast transparency or transparent NeXT scroll bar.

%description -l pl
Wterm to klon rxvt stworzony specjalnie z mysla o WindowMakerze. Oferuje wiele
interesujacych funkcji jak bardzo szybkie przezroczyste tlo czy przezroczysty
pasek przewijania typu  NeXT.

%prep
%setup -q -n %{name}-%{version}.orig -a 1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-transparency \
	--enable-next-scroll \
	--enable-ttygid \
	--enable-xpm-background

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}

#%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: wterm.spec,v $
Revision 1.1  2003-10-13 18:29:17  gausus
- Initiale release of wterm

Revision 1.26  2003/08/04 19:06:42  qboosh
- "rm missing" is not necessary in general, so don't propagate it everywhere

Revision 1.25  2003/07/30 17:18:42  qboosh
- Requires are placed after Requires()

Revision 1.24  2003/07/28 12:40:47  qboosh
- added more common filenames to doc (easier to remove than to add...
  and now it's harder to forget about updating doc section)

Revision 1.23  2003/07/13 13:29:45  deejay1
- inspired by ...., cut off changelog
