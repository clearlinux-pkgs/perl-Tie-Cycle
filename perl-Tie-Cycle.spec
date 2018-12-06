#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Tie-Cycle
Version  : 1.225
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-1.225.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-1.225.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtie-cycle-perl/libtie-cycle-perl_1.225-1.debian.tar.xz
Summary  : 'Cycle through a list of values via a scalar.'
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-Tie-Cycle-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Tie-Cycle package.
Group: Development
Provides: perl-Tie-Cycle-devel = %{version}-%{release}

%description dev
dev components for the perl-Tie-Cycle package.


%package license
Summary: license components for the perl-Tie-Cycle package.
Group: Default

%description license
license components for the perl-Tie-Cycle package.


%prep
%setup -q -n Tie-Cycle-1.225
cd ..
%setup -q -T -D -n Tie-Cycle-1.225 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Tie-Cycle-1.225/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Tie/Cycle.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Tie::Cycle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Tie-Cycle/LICENSE
/usr/share/package-licenses/perl-Tie-Cycle/deblicense_copyright
