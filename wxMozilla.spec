#

%define 	_name	wxmozilla

Summary:	wxWidgets component for embedding the Mozilla browser into any wxWidgets application.
Summary(pl):	Komponent wxWidgets s³u¿±cy do osadzania przegl±darki Mozilla w aplikacjach wxWidgets.
Name:		wxMozilla
Version:	0.5.6
Release:	0.1
License:	wxWidgets Licence (LGPL with exception)
Group:		Applications
Source0:	http://dl.sourceforge.net/alleg/%{_name}-%{version}.tar.gz
# Source0-md5:	f67edaaa17ed33a360c7c636b98b78fd
Patch0:		%{name}-seamonkey.patch
URL:		http://wxmozilla.sourceforge.net/
BuildRequires:	wxWidgets-devel
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	nspr-devel
BuildRequires:	seamonkey-devel
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxMozilla is a project to develop a wxWidgets component for embedding the
Mozilla browser into any wxWidgets application. The wxMozilla classes use
Mozilla's XPCOM (Cross Platrom COM) interface to embed a HTML browser or
editor within the application.

%description -l pl

%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ... library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
             --enable-seamonkey \
             --with-wx-config=/usr/bin/wx-gtk2-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
