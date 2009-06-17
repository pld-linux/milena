#
# TODO: do something with *.so and *.h files

%define ver	0.1.9
%define rel	5

Summary:	Text to speech system
Summary(pl.UTF-8):	Syntezator mowy
Name:		milena
Version:	%{ver}.%{rel}
Release:	0.1
License:	GPL v3, LGPL v2
Group:		Applications/Sound
Source0:	http://tts.polip.com/files/%{name}-%{ver}-%{rel}.tar.gz
# Source0-md5:	e26f8d73f49bda7c077273ad8d381664
URL:		http://milena.polip.com/
BuildRequires:	libao-devel
BuildRequires:	mbrola-voice-pl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system.

%description -l pl.UTF-8
Polski syntezator mowy.

%prep
%setup -q -n %{name}-%{ver}

%{__sed} -i 's/export prefix=\/usr\/local/export prefix=$(DESTDIR)\/usr/' Makefile
%{__sed} -i 's/export speechd_dir=$(shell .\/find_speechd)/export speechd_dir=$(DESTDIR)$(shell .\/find_speechd)/' Makefile
%{__sed} -i 's/ldconfig//' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_sysconfdir}/speech-dispatcher/modules}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libmilena*.so
%{_datadir}/milena
%{_sysconfdir}/speech-dispatcher/modules/milena*.conf
#%{_includedir}/milena*.h
