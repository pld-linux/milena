#
# TODO: do something with *.so and *.h files

%define ver	0.1.9
%define rel	6

Summary:	Text to speech system
Summary(pl.UTF-8):	Syntezator mowy
Name:		milena
Version:	%{ver}.%{rel}
Release:	0.5
License:	GPL v3, LGPL v2
Group:		Applications/Sound
Source0:	http://tts.polip.com/files/%{name}-%{ver}-%{rel}.tar.gz
# Source0-md5:	8a4ee898f225842988c41bd805ce556d
URL:		http://milena.polip.com/
BuildRequires:	enca-devel
BuildRequires:	libao-devel
Requires:	mbrola
Requires:	mbrola-voice-pl
Requires:	sox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish text to speech system.

%description -l pl.UTF-8
Polski syntezator mowy.

%prep
%setup -q -n %{name}-%{ver}

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
