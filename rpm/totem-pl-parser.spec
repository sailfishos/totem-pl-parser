Name:       totem-pl-parser
Summary:    Totem Playlist Parser library
Version:    3.10.7
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gnome.org/projects/totem/
Source0:    http://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.bz2
Patch0:     fix-automake.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.21.6
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  gettext
BuildRequires:  perl(XML::Parser)
BuildRequires:  intltool
BuildRequires:  gnome-common

%description
A library to parse and save playlists, as used in music and movie players.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

# fix-automake.patch
%patch0 -p1

%build
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make
NOCONFIGURE=1 REQUIRED_PKG_CONFIG_VERSION=0.17.1 REQUIRED_AUTOMAKE_VERSION=1.9 USE_GNOME2_MACROS=1 . gnome-autogen.sh --disable-gtk-doc

%configure --disable-static --disable-introspection
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%find_lang %{name} --with-gnome

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_datadir}/gtk-doc/html/totem-pl-parser
