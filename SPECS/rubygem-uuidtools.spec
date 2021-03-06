# Generated from uuidtools-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname uuidtools

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: UUID generator
Name: rubygem-%{gemname}
Version: 2.1.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://uuidtools.rubyforge.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A simple universally unique ID generation library.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/spec
%{geminstdir}/tasks
%{geminstdir}/Rakefile
%{geminstdir}/LICENSE
%{geminstdir}/CHANGELOG
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%exclude %{geminstdir}/website

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 2.1.2-1
- Initial package
