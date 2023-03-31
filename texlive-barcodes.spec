Name:		texlive-barcodes
Version:	15878
Release:	2
Summary:	Fonts for making barcodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/barcodes/willadt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package deals with EAN barcodes; MetaFont fonts are
provided, and a set of examples; for some codes, a small Perl
script is needed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/barcodes/wlc11.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc128.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc39.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc93.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlcr39.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlean.mf
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc11.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc128.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc39.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc93.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlcr39.tfm
%{_texmfdistdir}/tex/latex/barcodes/barcodes.sty
%doc %{_texmfdistdir}/doc/latex/barcodes/README
%doc %{_texmfdistdir}/doc/latex/barcodes/bcfaq.tex
%doc %{_texmfdistdir}/doc/latex/barcodes/changes
%doc %{_texmfdistdir}/doc/latex/barcodes/code39.tex
%doc %{_texmfdistdir}/doc/latex/barcodes/codean.pl
%doc %{_texmfdistdir}/doc/latex/barcodes/eandoc.pdf
%doc %{_texmfdistdir}/doc/latex/barcodes/eandoc.tex
%doc %{_texmfdistdir}/doc/latex/barcodes/examples.tex
%doc %{_texmfdistdir}/doc/latex/barcodes/install.bat
%doc %{_texmfdistdir}/doc/latex/barcodes/wlcdb.vpl
%doc %{_texmfdistdir}/doc/latex/barcodes/wlcf39.vpl
%doc %{_texmfdistdir}/doc/latex/barcodes/wlitf.vpl
#- source
%doc %{_texmfdistdir}/source/latex/barcodes/barcodes.dtx
%doc %{_texmfdistdir}/source/latex/barcodes/barcodes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
