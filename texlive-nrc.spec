%global tl_name nrc
%global tl_revision 29027

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.01a
Release:	%{tl_revision}.1
Summary:	Class for the NRC technical journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nrc
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nrc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros, and some documentation, for typesetting papers for submission to
journals published by the National Research Council Research Press. At
present, only nrc2.cls (for two-column layout) should be used.

