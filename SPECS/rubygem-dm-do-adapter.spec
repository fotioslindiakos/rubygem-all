# Generated from dm-do-adapter-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname dm-do-adapter

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: DataObjects Adapter for DataMapper
Name: rubygem-%{gemname}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/datamapper/dm-do-adapter
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(data_objects) => 0.10.6
Requires: rubygem(data_objects) < 0.11
Requires: rubygem(dm-core) => 1.2.0
Requires: rubygem(dm-core) < 1.3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
DataObjects Adapter for DataMapper


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
%{geminstdir}/tasks
%{geminstdir}/Gemfile
%{geminstdir}/Rakefile
%{geminstdir}/VERSION
%{geminstdir}/%{gemname}.gemspec
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
