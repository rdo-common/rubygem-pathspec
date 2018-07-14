%global gem_name pathspec

Name:           rubygem-%{gem_name}
Version:        0.2.1
Release:        3%{?dist}
Summary:        Use to match path patterns such as gitignore

License:        ASL 2.0
URL:            https://rubygems.org/gems/%{gem_name}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(fakefs)

%description
Use to match path patterns such as gitignore.


%package doc
Summary:        Documentation for %{name}
Requires:       rubygems

%description doc
Documentaion for %{name}


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
chmod 0755 %{buildroot}%{gem_instdir}/bin/pathspec-rb
mv %{buildroot}%{gem_instdir}/bin/pathspec-rb %{buildroot}%{_bindir}

%check
echo > spec/spec_helper.rb
rspec -Ilib spec


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}
%{_bindir}/pathspec-rb
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.1-2
- Bump release
- Ship new binary file

* Tue Feb 13 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.1-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.0-3
- Do not use simplecov
- Add spec directory to documentation subpackage
- Remove code for EOL fedora versions

* Mon Jun 05 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.0-2
- Remove unused Source

* Mon Jun 05 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.0-1
- New version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Orion Poplawski <orion@cora.nwra.com> - 0.0.2-2
- Fix files
- Doc subpackage
- Run tests

* Fri Apr 10 2015 Orion Poplawski <orion@cora.nwra.com> - 0.0.2-1
- Initial package
