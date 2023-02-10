#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fnotifystat
Version  : 0.02.10
Release  : 1
URL      : https://github.com/ColinIanKing/fnotifystat/archive/refs/tags/V0.02.10.tar.gz
Source0  : https://github.com/ColinIanKing/fnotifystat/archive/refs/tags/V0.02.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fnotifystat-bin = %{version}-%{release}
Requires: fnotifystat-data = %{version}-%{release}
Requires: fnotifystat-license = %{version}-%{release}
Requires: fnotifystat-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Fnotifystat
Fnotifystat is a program that dumps the file system activity in a given period of time.

%package bin
Summary: bin components for the fnotifystat package.
Group: Binaries
Requires: fnotifystat-data = %{version}-%{release}
Requires: fnotifystat-license = %{version}-%{release}

%description bin
bin components for the fnotifystat package.


%package data
Summary: data components for the fnotifystat package.
Group: Data

%description data
data components for the fnotifystat package.


%package license
Summary: license components for the fnotifystat package.
Group: Default

%description license
license components for the fnotifystat package.


%package man
Summary: man components for the fnotifystat package.
Group: Default

%description man
man components for the fnotifystat package.


%prep
%setup -q -n fnotifystat-0.02.10
cd %{_builddir}/fnotifystat-0.02.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676042564
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1676042564
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fnotifystat
cp %{_builddir}/fnotifystat-%{version}/COPYING %{buildroot}/usr/share/package-licenses/fnotifystat/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fnotifystat

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/fnotifystat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fnotifystat/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/fnotifystat.8.gz
