#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Tie-Cycle
Version  : 1.227
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-1.227.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Tie-Cycle-1.227.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtie-cycle-perl/libtie-cycle-perl_1.225-1.debian.tar.xz
Summary  : 'Cycle through a list of values via a scalar.'
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-Tie-Cycle-license = %{version}-%{release}
Requires: perl-Tie-Cycle-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Tie-Cycle package.
Group: Development
Provides: perl-Tie-Cycle-devel = %{version}-%{release}
Requires: perl-Tie-Cycle = %{version}-%{release}

%description dev
dev components for the perl-Tie-Cycle package.


%package license
Summary: license components for the perl-Tie-Cycle package.
Group: Default

%description license
license components for the perl-Tie-Cycle package.


%package perl
Summary: perl components for the perl-Tie-Cycle package.
Group: Default
Requires: perl-Tie-Cycle = %{version}-%{release}

%description perl
perl components for the perl-Tie-Cycle package.


%prep
%setup -q -n Tie-Cycle-1.227
cd %{_builddir}
tar xf %{_sourcedir}/libtie-cycle-perl_1.225-1.debian.tar.xz
cd %{_builddir}/Tie-Cycle-1.227
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Tie-Cycle-1.227/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle
cp %{_builddir}/Tie-Cycle-1.227/LICENSE %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle/40c57ec429e15412b20d729324e54569471f58e6
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Tie-Cycle/b3b506c47851fa5632c4ddbba7c3c6ed767f0cf8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Tie::Cycle.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Tie-Cycle/40c57ec429e15412b20d729324e54569471f58e6
/usr/share/package-licenses/perl-Tie-Cycle/b3b506c47851fa5632c4ddbba7c3c6ed767f0cf8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
