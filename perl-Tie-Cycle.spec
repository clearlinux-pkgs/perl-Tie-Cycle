#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : perl-Tie-Cycle
Version  : 1.231
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Tie-Cycle-1.231.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Tie-Cycle-1.231.tar.gz
Summary  : 'Cycle through a list of values via a scalar.'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Tie-Cycle-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Tie-Cycle package.
Group: Development
Provides: perl-Tie-Cycle-devel = %{version}-%{release}
Requires: perl-Tie-Cycle = %{version}-%{release}

%description dev
dev components for the perl-Tie-Cycle package.


%package perl
Summary: perl components for the perl-Tie-Cycle package.
Group: Default
Requires: perl-Tie-Cycle = %{version}-%{release}

%description perl
perl components for the perl-Tie-Cycle package.


%prep
%setup -q -n Tie-Cycle-1.231
cd %{_builddir}/Tie-Cycle-1.231
pushd ..
cp -a Tie-Cycle-1.231 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Tie::Cycle.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
