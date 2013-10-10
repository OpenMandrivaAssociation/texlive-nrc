# revision 29027
# category Package
# catalog-ctan /macros/latex/contrib/nrc
# catalog-date 2012-11-05 18:31:34 +0100
# catalog-license lppl
# catalog-version 2.01
Name:		texlive-nrc
Epoch:		1
Version:	2.01
Release:	1
Summary:	Class for the NRC technical journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nrc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros, and some documentation, for typesetting papers for
submission to journals published by the National Research
Council Research Press. At present, only nrc2.cls (for two-
column layout) should be used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nrc/nrc1.cls
%{_texmfdistdir}/tex/latex/nrc/nrc1.sty
%{_texmfdistdir}/tex/latex/nrc/nrc2.cls
%{_texmfdistdir}/tex/latex/nrc/nrc2.sty
%doc %{_texmfdistdir}/doc/latex/nrc/00-2013-feb-authors.txt
%doc %{_texmfdistdir}/doc/latex/nrc/README
%doc %{_texmfdistdir}/doc/latex/nrc/userguide.pdf
%doc %{_texmfdistdir}/doc/latex/nrc/userguide.tex
#- source
%doc %{_texmfdistdir}/source/latex/nrc/nrc.dtx
%doc %{_texmfdistdir}/source/latex/nrc/nrc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
