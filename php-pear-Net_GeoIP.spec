%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	GeoIP
%define		_status		beta
%define		_pearname	Net_GeoIP
%define		subver	RC3
%define		rel		1
Summary:	%{_pearname} - Library to perform geo-location lookups of IP addresses
Summary(pl.UTF-8):	%{_pearname} - biblioteka do wykonywania wyszukiwań lokalizacji geograficznych adresów IP
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	LGPL 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	0614060aafef4b560a1361d163284e16
URL:		http://pear.php.net/package/Net_GeoIP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that uses Maxmind's GeoIP databases to accurately determine
geographic location of an IP address.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Korzystająca z baz GeoIP firmy Maxmind biblioteka do precyzyjnego
określania lokalizacji geograficznej adresów IP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/GeoIP.php
%{php_pear_dir}/Net/GeoIP

%{php_pear_dir}/data/%{_pearname}
