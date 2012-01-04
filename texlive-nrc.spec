# revision 18087
# category Package
# catalog-ctan /macros/latex/contrib/nrc
# catalog-date 2007-01-12 08:59:52 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-nrc
Version:	20070112
Release:	2
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
Council of Canada. The macros are provided as a pair of
classes, one for journals printed in two columns and the other
for journals (such as the Canadian Journal of Physics, post-
1997) which are printed in a single-column format.

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
%doc %{_texmfdistdir}/doc/latex/nrc/README
%doc %{_texmfdistdir}/doc/latex/nrc/authors.txt
%doc %{_texmfdistdir}/doc/latex/nrc/userguide.pdf
%doc %{_texmfdistdir}/doc/latex/nrc/userguide.ps.gz
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
