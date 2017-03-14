%{?scl:%scl_package nodejs-read-package-tree}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

# Tests are disabled until nodejs-tap is updated
%global enable_tests 0

Name:           %{?scl_prefix}nodejs-read-package-tree
Version:        5.1.5
Release:        2%{?dist}
Summary:        NPM's Package Tree Parser
License:        ISC
URL:            https://github.com/npm/read-package-tree
Source0:        http://registry.npmjs.org/read-package-tree/-/read-package-tree-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires: %{?scl_prefix}nodejs-devel
BuildRequires: %{?scl_prefix}npm(debuglog)
BuildRequires: %{?scl_prefix}npm(dezalgo)
BuildRequires: %{?scl_prefix}npm(once) >= 1.3.0
BuildRequires: %{?scl_prefix}npm(read-package-json) >= 2.0.0
BuildRequires: %{?scl_prefix}npm(readdir-scoped-modules)

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(archy)
BuildRequires: %{?scl_prefix}npm(tap) >= 1.2.0
%endif

%description
Read the contents of node_modules.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/read-package-tree
cp -pr package.json rpt.js %{buildroot}%{nodejs_sitelib}/read-package-tree

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#/usr/bin/tap test/*.js
#%endif

%files
%license LICENSE
%doc README.md
%{nodejs_sitelib}/read-package-tree

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 5.1.5-2
- Built for RHSCL

* Wed Jul 20 2016 Stephen Gallagher <sgallagh@redhat.com> - 5.1.5-1
- Update to latest upstream release 5.1.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 5.1.2-4
- Fix incorrect BuildRequires on nodejs-devel

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 5.1.2-3
- Fix package review issues
- Use npm(foo) syntax for BuildRequires
- Drop unnecessary buildroot cleanup
- Fix capitalization of Summary:

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 5.1.2-2
- Run basic tests in %%check
- Temporarily disable extensive tests due to incompatible nodejs-tap

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 5.1.2-1
- Initial release to support Node.js 4.x
- Disable tests until nodejs-tap is updated
