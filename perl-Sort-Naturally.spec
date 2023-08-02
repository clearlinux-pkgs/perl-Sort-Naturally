#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sort-Naturally
Version  : 1.03
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-1.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-1.03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsort-naturally-perl/libsort-naturally-perl_1.03-2.debian.tar.xz
Summary  : 'sort lexically, but sort numeral parts numerically'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sort-Naturally-license = %{version}-%{release}
Requires: perl-Sort-Naturally-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Time-stamp: "2001-05-25 21:17:33 MDT"
Sort::Naturally
[extracted from the Pod...]

%package dev
Summary: dev components for the perl-Sort-Naturally package.
Group: Development
Provides: perl-Sort-Naturally-devel = %{version}-%{release}
Requires: perl-Sort-Naturally = %{version}-%{release}

%description dev
dev components for the perl-Sort-Naturally package.


%package license
Summary: license components for the perl-Sort-Naturally package.
Group: Default

%description license
license components for the perl-Sort-Naturally package.


%package perl
Summary: perl components for the perl-Sort-Naturally package.
Group: Default
Requires: perl-Sort-Naturally = %{version}-%{release}

%description perl
perl components for the perl-Sort-Naturally package.


%prep
%setup -q -n Sort-Naturally-1.03
cd %{_builddir}
tar xf %{_sourcedir}/libsort-naturally-perl_1.03-2.debian.tar.xz
cd %{_builddir}/Sort-Naturally-1.03
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sort-Naturally-1.03/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sort-Naturally
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sort-Naturally/eadfab6cc46a0e4abf06e9b5bf97414647a794b7
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
/usr/share/man/man3/Sort::Naturally.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sort-Naturally/eadfab6cc46a0e4abf06e9b5bf97414647a794b7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
