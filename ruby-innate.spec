Summary:	Ramaze - Web framework
Name:		ruby-innate
Version:	2010.07
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/innate-%{version}.gem
# Source0-md5:	ebbe0cef40759f6834d45f9cd3e582c4
URL:		https://github.com/Ramaze/innate
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-rake
BuildRequires:	setup.rb = 3.4.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ramaze is web framework for Ruby.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
cp %{_datadir}/setup.rb .

%build
#mv innate.rb lib

ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/innate*
