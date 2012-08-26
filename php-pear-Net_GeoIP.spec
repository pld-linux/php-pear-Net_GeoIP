%define		status		beta
%define		pearname	Net_GeoIP
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Library to perform geo-location lookups of IP addresses
Summary(pl.UTF-8):	%{pearname} - biblioteka do wykonywania wyszukiwań lokalizacji geograficznych adresów IP
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	2
License:	LGPL 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	f4c0b232ca6d19e41316febe0dc986fe
URL:		http://pear.php.net/package/Net_GeoIP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 5.0.0
Requires:	php-pear
Suggests:	GeoIP-db-Country
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that uses Maxmind's GeoIP databases to accurately determine
geographic location of an IP address.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Korzystająca z baz GeoIP firmy Maxmind biblioteka do precyzyjnego
określania lokalizacji geograficznej adresów IP.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

# use system db
rm .%{php_pear_dir}/data/Net_GeoIP/data/GeoIP.dat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/GeoIP.php
%{php_pear_dir}/Net/GeoIP
