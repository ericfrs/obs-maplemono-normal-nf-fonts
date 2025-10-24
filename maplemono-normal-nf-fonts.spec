Name:           maplemono-normal-nf-fonts
Version:        7.8
Release:        0
Summary:        Maple Mono monospace font with nerd fonts patches
BuildArch:      noarch
License:        OFL-1.1
URL:            https://github.com/subframe7536/maple-font
Source0:        %{url}/releases/download/v%{version}/MapleMonoNormal-NF-unhinted.zip
Source1:        https://raw.githubusercontent.com/subframe7536/maple-font/refs/heads/variable/README.md#/README.md.upstream
Source2:        https://raw.githubusercontent.com/subframe7536/maple-font/refs/heads/variable/OFL.txt

BuildRequires:  fontpackages-devel
BuildRequires:  unzip

%reconfigure_fonts_prereq

%description
%{summary}.

%prep
%autosetup -c

%build

%install
install -dm 755 %{buildroot}%{_datadir}/fonts/truetype/maplemono-nf-unhinted
cp -p *.ttf %{buildroot}%{_datadir}/fonts/truetype/maplemono-nf-unhinted/
install -Dpm 644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm 644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/OFL.txt

%reconfigure_fonts_scriptlets

%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/OFL.txt
%doc %{_docdir}/%{name}/README.md
%dir %{_datadir}/fonts/truetype
%dir %{_datadir}/fonts/truetype/maplemono-nf-unhinted
%{_datadir}/fonts/truetype/maplemono-nf-unhinted/*.ttf

%changelog
* Fri Oct 24 2025 - 7.8
- Initial package
