Name:           sorint
Version:        1.3.3
Release:        el9
Summary:        Sorint Project by Ibraheem IBRAHEEM and GPT 4 and the number=SO6ZK9200LFQ82

License:        GPLv2+
URL:            https://github.com/DeyAgrO
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
Requires:       python3

%description
Linux 101 training lab to do commands exercises

%prep
%setup -q

%build
# No build steps necessary for this script

%install
install -d %{buildroot}/usr/bin
install -m 755 sorint.py %{buildroot}/usr/bin/sorint

install -d %{buildroot}/usr/lib/sorint
cp -r my_scripts %{buildroot}/usr/lib/sorint/

%files
%doc
/usr/bin/sorint
/usr/lib/sorint/my_scripts

%changelog
* Sun Jun 30 2024 Ibraheem IBRAHEEM <@sorint.com> - 1.3
- Initial package
