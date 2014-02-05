%define upstream_name    WWW-Pastebin-Bot-Pastebot-Create
%define upstream_version 0.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Create pastes on sites powered by Bot::Pastebot
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-Pastebin-Bot-Pastebot-Create-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Data::Accessor)
BuildRequires:	perl(Devel::TakeHashArgs)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
The module provides interface to paste into pastebin sites powered by the
Bot::Pastebot manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.1.0-5mdv2011.0
+ Revision: 655241
- rebuild for updated spec-helper

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.1.0-4mdv2011.0
+ Revision: 505280
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.001-3mdv2010.0
+ Revision: 430658
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.001-2mdv2009.0
+ Revision: 268877
- rebuild early 2009.0 package (before pixel changes)

* Sat Apr 12 2008 Olivier Thauvin <nanardon@mandriva.org> 0.001-1mdv2009.0
+ Revision: 192625
- import perl-WWW-Pastebin-Bot-Pastebot-Create



