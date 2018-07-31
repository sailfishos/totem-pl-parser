Name:       totem-pl-parser
Summary:    Totem Playlist Parser library
Version:    3.26.1
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gnome.org/projects/totem/
Source0:    http://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.21.6
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  ninja

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

%build
%meson -Denable-gtk-doc=false
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_datadir}/gtk-doc/html/totem-pl-parser
%{_datadir}/gir-1.0/TotemPlParser-1.0.gir

