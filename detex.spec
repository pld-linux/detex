Summary:	TeX/LaTeX to ASCII converter
Summary(pl):	Konwerter TeX-a/LaTex-a na ASCII
Name:		detex
Version:	2.7
Release:	1
Epoch:		0
License:	distributable
Group:		Applications/Text
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	22cbca475eedb39deee64e126dfd5ddb
Patch0:		%{name}-suse.patch
Patch1:		%{name}-install.patch
URL:		http://www.cs.purdue.edu/homes/trinkle/detex/
BuildRequires:	flex
Provides:	deTeX
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
detex is filter to strip TeX/LaTeX commands.

%description -l pl
detex jest filtrem usuwaj±cy makra TeX-a/LaTex-a .

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -s detex $RPM_BUILD_ROOT%{_bindir}
(cd $RPM_BUILD_ROOT%{_bindir}; ln -s detex delatex)
install detex.1l $RPM_BUILD_ROOT%{_mandir}/man1/detex.1
(cd $RPM_BUILD_ROOT%{_mandir}/man1; ln -s detex.1 delatex.1)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
