# Generated from datamapper-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname datamapper

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: An Object/Relational Mapper for Ruby
Name: rubygem-%{gemname}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://datamapper.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(dm-core) => 1.2.0
Requires: rubygem(dm-core) < 1.3
Requires: rubygem(dm-aggregates) => 1.2.0
Requires: rubygem(dm-aggregates) < 1.3
Requires: rubygem(dm-constraints) => 1.2.0
Requires: rubygem(dm-constraints) < 1.3
Requires: rubygem(dm-migrations) => 1.2.0
Requires: rubygem(dm-migrations) < 1.3
Requires: rubygem(dm-transactions) => 1.2.0
Requires: rubygem(dm-transactions) < 1.3
Requires: rubygem(dm-serializer) => 1.2.0
Requires: rubygem(dm-serializer) < 1.3
Requires: rubygem(dm-timestamps) => 1.2.0
Requires: rubygem(dm-timestamps) < 1.3
Requires: rubygem(dm-validations) => 1.2.0
Requires: rubygem(dm-validations) < 1.3
Requires: rubygem(dm-types) => 1.2.0
Requires: rubygem(dm-types) < 1.3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Faster, Better, Simpler.


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
%{geminstdir}/Rakefile
%{geminstdir}/.gitignore
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.txt


%changelog
* Thu Feb 09 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
