Name:           perl-Font-AFM
Version:        1.20
Release:        13%{?dist}
Summary:        Perl interface to Adobe Font Metrics files
Group:          Development/Libraries
License:        GPL+ or Artistic) and Copyright only
URL:            http://search.cpan.org/dist/Font-AFM/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz
Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  %{_datadir}/a2ps/afm/phvr.afm

%description
Interface to Adobe Font Metrics files

%prep
%setup -q -n Font-AFM-%{version}
# We don't have Helvetica, use phvr.afm instead
sed -i -e 's,Helvetica,phvr,g' t/afm.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
chmod -R u+w %{buildroot}/*

%check
make test METRICS=%{_datadir}/a2ps/afm

%files
%doc Changes README
%{perl_vendorlib}/Font
%{_mandir}/man3/Font*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.20-13
- Mass rebuild 2013-12-27

* Tue Jul 23 2013 Petr Šabata <contyk@redhat.com> - 1.20-12.1
- Add missing build-time dependencies
- Modernize the spec a little

* Wed Nov 28 2012 Petr Šabata <contyk@redhat.com> - 1.20-12
- BuildRequire perl(Carp)
- Drop command macros
- Reflect metrics copyright in the License tag

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.20-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.20-8
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.20-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.20-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.20-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.19-7
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.19-6
- rebuild for new perl

* Fri Aug 31 2007 Ralf Corsépius <rc040203@freenet.de> - 1.19-5
- BR: perl(ExtUtils::MakeMaker).
- Update license tag.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.19-4
- Mass rebuild.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 1.19-3
- Rebuild for perl-5.8.8.

* Sun Aug 21 2005 Ralf Corsepius <ralf@links2linux.de> - 1.19-3
- Changelog cleanup.

* Sun Aug 21 2005 Ralf Corsepius <ralf@links2linux.de> - 1.19-2
- Review feedback.

* Thu Aug 18 2005 Ralf Corsepius <ralf@links2linux.de> - 1.19-1
- FE submission.
