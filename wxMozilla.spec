#
# Conditional build:
%bcond_without	ansi			# only unicode packages
%bcond_without	x11			# don't build wxX11 packages
#
# TODO:
# wxPython
# ansi
# x11

%define 	_name	wxmozilla

Summary:	wxWidgets component for embedding the Mozilla browser into wxWidgets applications
Summary(pl):	Komponent wxWidgets do osadzania przegl±darki Mozilla w aplikacjach wxWidgets
Name:		wxMozilla
Version:	0.5.6
Release:	0.2
License:	wxWidgets Licence (LGPL with exception)
Group:		Applications
Source0:	http://dl.sourceforge.net/wxmozilla/%{_name}-%{version}.tar.gz
# Source0-md5:	f67edaaa17ed33a360c7c636b98b78fd
Patch0:		%{name}-seamonkey.patch
URL:		http://wxmozilla.sourceforge.net/
BuildRequires:	wxGTK2-unicode-devel
%{?with_x11:BuildRequires:	wxX11-unicode-devel
%{?with_ansi:BuildRequires:	wxX11-devel}
}
%{?with_ansi:BuildRequires:	wxGTK2-devel}
BuildRequires:	wxWidgets-devel
BuildRequires:	nspr-devel
BuildRequires:	seamonkey-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxMozilla is a project to develop a wxWidgets component for embedding
the Mozilla browser into any wxWidgets application. The wxMozilla
classes use Mozilla's XPCOM (Cross Platform COM) interface to embed a
HTML browser or editor within the application.

%description -l pl
wxMozilla to projekt stworzenia komponentu do osadzania przegl±darki
Mozilla w aplikacjach wxWidgets. Klasy wxMozilla wykorzystuj±
interfejs Mozilli XPCOM (miêdzyplatformowy COM) do osadzania
przegl±darki lub edytora HTML wewn±trz aplikacji.

%package devel
Summary:	Header files for wxMozilla library
Summary(pl):	Pliki nag³ówkowe biblioteki wxMozilla
Group:		Development/Libraries

%description devel
Header files for wxMozilla library.

%description devel -l pl
Pliki nag³ówkowe biblioteki wxMozilla

#%%package wxBase-devel
#%%package wxBase-unicode-devel
#%%package wxGTK2-devel

%package wxGTK2-unicode-devel
Summary:	Header files for wxMozilla library GTK2, Unicode version
Summary(pl):	Pliki nag³ówkowe biblioteki wxMozilla wersja GTK2, Unicode
Group:		Development/Libraries
Requires:	%{name}-devel
Requires:	wxGTK2-unicode

%description wxGTK2-unicode-devel
Header files for wxMozilla library GTK2, Unicode version.

%description wxGTK2-unicode-devel -l pl
Pliki nag³ówkowe biblioteki wxMozilla wersja GTK2, Unicode


%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}

for gui in 'gtk2' %{?with_x11:'x11univ'} ; do

for mode in 'unicode' %{?with_ansi:'ansi'} ; do
	objdir=`echo obj${gui}${mode}`
	mkdir $objdir
	cd $objdir
	../%configure \
            --enable-seamonkey \
            --with-wx-config=/usr/bin/wx-${gui}-${mode}-config
        %{__make}
	cd ..
done

done


%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

for gui in 'gtk2' %{?with_x11:'x11univ'} ; do

for mode in 'unicode' %{?with_ansi:'ansi'} ; do
	objdir=`echo obj${gui}${mode}`
	cd $objdir
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT
	mv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/wxmozilla.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/wxmozilla-${gui}-${mode}.pc 
	cd ..
done

done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/wxmozilla/*

#%%files wxBase-devel
#%%files wxBase-unicode-devel
#%%files wxGTK2-devel

%files wxGTK2-unicode-devel
%defattr(644,root,root,755)
%{_includedir}/wx*
%{_libdir}/libwxmozilla_gtk2u*
%{_libdir}/pkgconfig/wxmozilla-gtk2-unicode.pc
