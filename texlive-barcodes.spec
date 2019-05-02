# revision 15878
# category Package
# catalog-ctan /fonts/barcodes/willadt
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-barcodes
Version:	20190228
Release:	1
Summary:	Fonts for making barcodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/barcodes/willadt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/barcodes.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080817-2
+ Revision: 749447
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080817-1
+ Revision: 717881
- texlive-barcodes
- texlive-barcodes
- texlive-barcodes
- texlive-barcodes
- texlive-barcodes

