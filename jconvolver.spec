%define name            jconvolver
%define version         0.9.2
%define release         1

Name:           %{name}
Summary:        Audio convolution engine for JACK
Version:        %{version}
Release:        %{release}

Source:         http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio/
License:        GPLv2
Group:          Sound
BuildRequires:  clthreads-devel, libzita-convolver-devel
BuildRequires:  fftw3-devel, sndfile-devel, jackit-devel
Suggests:       jconvolver-reverbs

%description
Jconvolver is a Convolution Engine for JACK using FFT-based partitioned
convolution with multiple partition sizes. It is mainly used to create
realistic acoustic environments such as reverbs for sounds sent to its
input. Jconvolver uses a configurable smallest partition size at the
start of the impulse response, and longer ones further on. This
allows long impulse responses along with minimal or even zero delay at
a reasonable CPU load. It is recommended to install also jcgui, a
graphical user interface for JConvolver as well as the example reverb
data jconvolver-reverbs.

%prep
%setup -q
cd source
perl -pi -e 's/PREFIX =/#PREFIX =/g' Makefile
perl -pi -e 's/-march=native//g' Makefile

%build
cd source
make

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_datadir}/%{name}
cp -a config-files %{buildroot}/%{_datadir}/%{name}
cd source
install -d %{buildroot}/%{_bindir}
PREFIX=%{buildroot}%{_prefix} make install
chmod 644 %{buildroot}%{_datadir}/%{name}/config-files/ambisonic/super-stereo.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}


%changelog
* Sun Apr 15 2012 Frank Kober <emuse@mandriva.org> 0.9.2-1
+ Revision: 791128
- kill march CPP flag
- update to new version 0.9.2

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.7-2mdv2011.0
+ Revision: 612441
- the mass rebuild of 2010.1 packages

* Sun Apr 11 2010 Frank Kober <emuse@mandriva.org> 0.8.7-1mdv2010.1
+ Revision: 533597
- new version
- new version

* Tue Mar 02 2010 Frank Kober <emuse@mandriva.org> 0.8.4-1mdv2010.1
+ Revision: 513719
- import jconvolver
- import jconvolver


