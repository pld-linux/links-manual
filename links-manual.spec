%define _noautocompressdoc *.txt

Summary:	Links User Reference Manual
Summary(pl):	Podrêcznik U¿ytkownika Linksa
Name:		links-manual
Version:	0.82
Release:	1
License:	Free
Group:		Documentation
Source0:	http://links.sourceforge.net/download/docs/manual-%{version}-en.tar.bz2
URL:		http://links.sourceforge.net/#man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This manual has been designed and written to be:
 - a complete user reference to Links,
 - easy to navigate with plenty of hypertext links,
 - displayed in Links!

%description -l pl
Ten podrêcznik zosta³ stworzony i napisany aby byæ:
 - kompletn± informacj± na temat Linksa,
 - dokumentem ³atwym w nawigacji i zawieraj±cym wiele odno¶ników,
 - wy¶wietlanym przez Linksa!

%prep
%setup -q -n manual-%{version}-en

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.txt
