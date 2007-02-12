Summary:	TeX/LaTeX to ASCII converter
Summary(pl.UTF-8):   Konwerter TeXa/LaTeXa na ASCII
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
BuildRequires:	flex >= 2.5.31-6
Provides:	deTeX
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
detex is filter to strip TeX/LaTeX commands.

%description -l pl.UTF-8
detex jest filtrem usuwającym makra TeXa/LaTeXa.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} \${DEFS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install detex $RPM_BUILD_ROOT%{_bindir}
ln -sf detex $RPM_BUILD_ROOT%{_bindir}/delatex

install detex.1l $RPM_BUILD_ROOT%{_mandir}/man1/detex.1
echo '.so detex.1' > $RPM_BUILD_ROOT%{_mandir}/man1/delatex.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
