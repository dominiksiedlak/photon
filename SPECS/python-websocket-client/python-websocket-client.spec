%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Name:           python-websocket-client
Version:        0.44.0
Release:        1%{?dist}
Summary:        WebSocket client for python
License:        LGPL
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/websocket-client
Source0:        websocket_client-0.44.0.tar.gz
%define sha1    websocket_client=736908072e36c1f3dc5714b685e246d8090ee1df

BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python-setuptools
Requires:       python2
Requires:       python2-libs

BuildArch:      noarch

%description
WebSocket client for python

%package -n     python3-websocket-client
Summary:        WebSocket client for python3
BuildRequires:  python3-devel

%description -n python3-websocket-client
WebSocket client for python3

%prep
%setup -n websocket_client-%{version}
rm -rf ../p3dir
cp -a . ../p3dir

%build
python2 setup.py build
pushd ../p3dir
python3 setup.py build
popd

%install
pushd ../p3dir
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python2_sitelib}/*
/usr/bin/wsdump.py

%files -n python3-websocket-client
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
*   Thu Nov 30 2017 Xiaolin Li <xiaolinl@vmware.com> 0.44.0-1
-   Update websocket_client to version 0.44.0
*   Sun Jun 04 2017 Vinay Kulkarni <kulkarniv@vmware.com> 0.7.0-1
-   Initial version of python WebSocket for PhotonOS.