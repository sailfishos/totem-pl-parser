Name:       totem-pl-parser
Summary:    Totem Playlist Parser library
Version:    3.26.6
Release:    1
License:    LGPLv2+
URL:        https://github.com/sailfishos/totem-pl-parser
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
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
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%meson -Denable-gtk-doc=false -Denable-libgcrypt=yes -Denable-libarchive=no
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS NEWS README.md

%find_lang %{name} --with-gnome

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib
%{_libexecdir}/totem-pl-parser/

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/TotemPlParser-1.0.gir

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
