%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Name:           python3-alabaster
Version:        0.7.12
Release:        1%{?dist}
Summary:        A configurable sidebar-enabled Sphinx theme
License:        BSD
Group:          Development/Languages/Python
Url:            https://github.com/bitprophet/alabaster/
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://pypi.python.org/packages/d0/a5/e3a9ad3ee86aceeff71908ae562580643b955ea1b1d4f08ed6f7e8396bd7/alabaster-%{version}.tar.gz
%define sha1    alabaster=36c11bd5d8e99e2009b643b7f6e91bf2a0fd573b

BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-libs
BuildArch:      noarch

%description
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx documentation system. It is Python 2+3 compatible.

%prep
%setup -n alabaster-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 0.7.12-1
-   Automatic Version Bump
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 0.7.11-2
-   Mass removal python2
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 0.7.11-1
-   Update to version 0.7.11
*   Wed Jun 07 2017 Xiaolin Li <xiaolinl@vmware.com> 0.7.10-3
-   Add python3-setuptools and python3-xml to python3 sub package Buildrequires.
*   Thu Jun 01 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.7.10-2
-   Changed python to python2
*   Tue Apr 25 2017 Dheeraj Shetty <dheerajs@vmware.com> 0.7.10-1
-   Initial
