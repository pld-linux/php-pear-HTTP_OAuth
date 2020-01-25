%define		status		alpha
%define		pearname	HTTP_OAuth
Summary:	%{pearname} - PEAR implementation of the OAuth 1.0a specification
Name:		php-pear-%{pearname}
Version:	0.3.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ca61e3eec83dbfe18abcbd7d0818ec4a
URL:		http://pear.php.net/package/HTTP_OAuth/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-HTTP_Request2 >= 0.5.1
Obsoletes:	php-pear-HTTP_Request2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows the use of the consumer and provider angles of the OAuth 1.0a
specification.

%prep
%pear_package_setup

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
%{php_pear_dir}/HTTP/OAuth
%{php_pear_dir}/HTTP/OAuth.php
