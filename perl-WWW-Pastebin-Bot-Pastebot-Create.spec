
%define realname   WWW-Pastebin-Bot-Pastebot-Create
%define version    0.001
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    create pastes on sites powered by Bot::Pastebot
Source:     http://www.cpan.org/modules/by-module/WWW/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Data::Accessor)
BuildRequires: perl(Devel::TakeHashArgs)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description

The module provides interface to paste into pastebin sites powered by the
Bot::Pastebot manpage





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*



