%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name http_parser.rb

Name: rubygem-http_parser.rb
Version:        0.6.0
Release:        2%{?dist}
Summary:        Provides ruby bindings to http parser
Group:          Development/Languages
License:        MIT
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Source0:        https://rubygems.org/downloads/http_parser.rb-%{version}.gem
%define sha1    http_parser.rb=0d69273a2e74b82358b19f01632e06601732a64e
BuildRequires:  ruby
Provides: rubygem-http_parser.rb = %{version}

%description
Provides ruby bindings to http parser.

%prep
%setup -q -c -T

%build

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{SOURCE0}

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Wed Sep 02 2020 Sujay G <gsujay@vmware.com> 0.6.0-2
-   rebuilt with ruby-2.7.1
*   Tue Jul 24 2018 Srinidhi Rao <srinidhir@vmware.com> 0.6.0-1
-   Initial build
