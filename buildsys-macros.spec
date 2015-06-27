# HACK to fix pacakge version in koji
%define dist .v%{version}

Name:		buildsys-macros
Summary:	Macros for the CentOS Buildsystem
# The value for version should match the version of CentOS.
Version:	7
Release:	1%{?dist}
License:	GPL
Group:		Development/Buildsystem
Source:         %{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildarch:  	noarch
Requires:	rpmdevtools

%description
Macros for the CentOS Buildsystem

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rpm/
VERSION=%{version}
printf %s%b "%" "rhel $VERSION\n" >> $RPM_BUILD_ROOT/etc/rpm/macros.disttag
printf %s%b "%" "dist .v$VERSION\n" >> $RPM_BUILD_ROOT/etc/rpm/macros.disttag
printf %s%b "%" "el$VERSION 1\n" >> $RPM_BUILD_ROOT/etc/rpm/macros.disttag
printf %s%b "%" "__arch_install_post /usr/lib/rpm/check-buildroot\n" >> $RPM_BUILD_ROOT/etc/rpm/macros.checkbuild

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/rpm/macros.disttag
/etc/rpm/macros.checkbuild

%changelog
* Sun Mar 13 2011 Shad L. Lords <slords@mail.com>
- Update el<ver> to v<ver> to match clearos builds

* Mon Aug 02 2010 Shad L. Lords <slords@mail.com>
- Update el<ver> to v<ver> to match clearos builds

* Mon May 21 2007 Dennis Gilmore <dennis@ausil.us> 
- add el<ver> 1  fro new disttag guidelines

* Wed Sep 27 2006 Dennis Gilmore <dennis@ausil.us>
- add macro to run check-buildroot

* Mon Jul 07 2006 Dennis Gilmore <dennis@ausil.us>
- rhel version

* Tue May 10 2005 Tom "spot" Callaway <tcallawa@redhat.com>
- Initial build.
