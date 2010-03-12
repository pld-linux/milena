#
# TODO: do something with *.so and *.h files

Summary:	Text to speech system
Summary(pl.UTF-8):	Syntezator mowy
Name:		milena
Version:	0.2.7.1
Release:	0.1
License:	GPL v3, LGPL v2
Group:		Applications/Sound
Source0:	http://tts.polip.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	b56b193a3c2a6844f8c72829c090d6c1
URL:		http://milena.polip.com/
BuildRequires:	enca-devel
BuildRequires:	libao-devel
BuildRequires:	mbrola-voice-pl
Requires:	mbrola
Requires:	mbrola-voice-pl
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system.

%description -l pl.UTF-8
Polski syntezator mowy.

%package devel
Summary:	Libraries and header files for milena development
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe dla milena
Group:		Development/Libraries

%description devel
This is the milena development package.

%prep
%setup -q

%{__sed} -i 's/export prefix=\/usr\/local/export prefix=$(DESTDIR)\/usr/' Makefile
%{__sed} -i 's/export speechd_dir=$(shell .\/find_speechd)/export speechd_dir=$(DESTDIR)$(shell .\/find_speechd)/' Makefile
%{__sed} -i 's/ldconfig//' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	prefix=%{_prefix} \
	mbrola=%{_bindir}/mbrola \
	mbrola_voice=%{_datadir}/festival/lib/voices/polish/pl1_mbrola/pl1/pl1 \
	speechd=%{_sysconfdir}/speech-dispatcher/modules \
	distro="PLD Linux" \
	contrast=contrast

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/milena,%{_libdir},%{_includedir},%{_sysconfdir}/speech-dispatcher/modules}

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
%{_datadir}/milena-words

%files devel
%defattr(644,root,root,755)
%{_includedir}/milena*.h
