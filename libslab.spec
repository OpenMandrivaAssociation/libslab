%define major 0
%define libname %mklibname slab %{major}
%define develname %mklibname -d slab

Summary: Beautification app library
Name: libslab
Version: 2.30.0
Release: 4
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/libslab/2.30/%{name}-%{version}.tar.bz2
Patch0: libslab-bnc536778-fix-libslab-split.patch

Buildrequires: intltool
BuildRequires:  pkgconfig(gnome-desktop-2.0)
BuildRequires:  pkgconfig(libgnome-menu)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(sm)

%description
Beautification app library.

%package -n %{libname}
Summary: Beautification app library
Group: Graphical desktop/GNOME
Requires: %{name} = %{version}
Conflicts: %{_lib}gnome-main-menu < 0.9.14

%description -n %{libname}
This library provides functionality to create applications like
gnome-control center and the application-browser from gnome-main-menu.

%package -n %{develname}
Summary: Development file for libslab
Group: Graphical desktop/GNOME
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}gnome-main-menu-devel < 0.9.14

%description -n %{develname}
This library provides functionality to create applications like
gnome-control center and the application-browser from gnome-main-menu.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%files -f %{name}.lang

%files -n %{libname}
%{_libdir}/libslab.so.%{major}*

%files -n %{develname}
%{_libdir}/libslab.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libslab

