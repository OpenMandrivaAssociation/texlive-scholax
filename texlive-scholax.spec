%global tl_name scholax
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.033
Release:	%{tl_revision}.1
Summary:	Extension of TeXGyreSchola (New Century Schoolbook) with math support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/scholax
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scholax.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scholax.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains an extension of TeXGyreSchola with extensive
superiors, inferior figures, upright punctuation glyphs added to the
Italic face for a theorem font, plus slanted and bold slanted faces.
Math support is provided by one of two options to newtxmath, one of
which uses an adaptation of the fourier math Greek letters.

