Summary:       C/C++ configuration file library
Name:          libconfig
Version:       1.7.2
Release:       1%{?dist}
License:       LGPLv2
URL:           http://www.hyperrealm.com/libconfig/
Source:        %{name}-%{version}.tar.gz
%define sha1   libconfig=a0b282e78409f9f1a165b0c0011ae2ea78e7a390
Group:         Development/Tools
Vendor:        VMware, Inc.
Distribution:  Photon

%description
Libconfig is a simple library for processing structured configuration files,
like this one: test.cfg. This file format is more compact and more readable than XML.
And unlike XML, it is type-aware, so it is not necessary to do string parsing in application code.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}/dir

%check
./tests/libconfig_tests

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING.LIB README
%{_libdir}/libconfig*.so.*
%{_includedir}/libconfig*
%{_libdir}/libconfig*.so
%{_libdir}/pkgconfig/libconfig*.pc
%exclude %{_libdir}/cmake/libconfig++/libconfig++Config.cmake
%exclude %{_libdir}/cmake/libconfig/libconfigConfig.cmake
%{_infodir}/libconfig.info*

%changelog
*   Wed Aug 12 2020 Gerrit Photon <photon-checkins@vmware.com> 1.7.2-1
-   Automatic Version Bump
*   Mon Jul 20 2020 Shreenidhi Shedi <sshedi@vmware.com> 1.7-1
-   Upgrade to version 1.7
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.5-2
-   GA - Bump release of all rpms
*   Tue Nov 24 2015 Xiaolin Li <xiaolinl@vmware.com> 0.7.2-1
-   Initial build.  First version
