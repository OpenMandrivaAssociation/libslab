%define major 0
%define libname %mklibname slab %major
%define develname %mklibname -d slab

Summary: Beautification app library
Name: libslab
Version: 2.27.91
Release: %mkrel 2
License: GPLv2+
Group: Graphical desktop/GNOME
Source0: http://ftp.gnome.org/pub/GNOME/sources/libslab/2.27/%{name}-%{version}.tar.bz2
URL: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgnome-menu-devel
BuildRequires: gnome-desktop-devel
BuildRequires: librsvg-devel
Buildrequires: intltool

%description
Beautification app library.

%package -n %libname
Summary: Beautification app library
Group: Graphical desktop/GNOME
Requires: %name = %version
Conflicts: %{_lib}gnome-main-menu < 0.9.13

%description -n %libname
This library provides functionality to create applications like
gnome-control center and the application-browser from gnome-main-menu.

%package -n %develname
Summary: Development file for libslab
Group: Graphical desktop/GNOME
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %{_lib}gnome-main-menu-devel < 0.9.13

%description -n %develname
This library provides functionality to create applications like
gnome-control center and the application-browser from gnome-main-menu.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)

%files -n %libname
%defattr(-, root, root)
%{_libdir}/libslab.so.%{major}
%{_libdir}/libslab.so.%{major}.*

%files -n %develname
%defattr(-, root, root)
%{_libdir}/libslab.so
%{_libdir}/libslab.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libslab
