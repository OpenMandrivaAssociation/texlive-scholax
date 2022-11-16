Name:		texlive-scholax
Version:	61836
Release:	1
Summary:	Extension of TeXGyreSchola (New Century Schoolbook) with math support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scholax
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scholax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scholax.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains an extension of TeXGyreSchola with
extensive superiors, inferior figures, upright punctuation
glyphs added to the Italic face for a theorem font, plus
slanted and bold slanted faces. Math support is provided by one
of two options to newtxmath, one of which uses an adaptation of
the fourier math Greek letters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scholax
%{_texmfdistdir}/fonts/vf/public/scholax
%{_texmfdistdir}/fonts/type1/public/scholax
%{_texmfdistdir}/fonts/tfm/public/scholax
%{_texmfdistdir}/fonts/opentype/public/scholax
%{_texmfdistdir}/fonts/map/dvips/scholax
%{_texmfdistdir}/fonts/enc/dvips/scholax
%{_texmfdistdir}/fonts/afm/public/scholax
%doc %{_texmfdistdir}/doc/fonts/scholax

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
