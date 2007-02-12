%define _noautocompressdoc *.txt

Summary:	Links User Reference Manual
Summary(pl.UTF-8):   Podręcznik Użytkownika Linksa
Name:		links-manual
Version:	0.82
Release:	1
License:	Free
Group:		Documentation
Source0:	http://links.sourceforge.net/download/docs/manual-%{version}-en.tar.bz2
# Source0-md5:	947950d4974c25f95f1a3988bf88cb21
URL:		http://links.sourceforge.net/#man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
This manual has been designed and written to be:
 - a complete user reference to Links,
 - easy to navigate with plenty of hypertext links,
 - displayed in Links!

%description -l pl.UTF-8
Ten podręcznik został stworzony i napisany aby być:
 - kompletną informacją na temat Linksa,
 - dokumentem łatwym w nawigacji i zawierającym wiele odnośników,
 - wyświetlanym przez Linksa!

%prep
%setup -q -n manual-%{version}-en

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html *.txt
