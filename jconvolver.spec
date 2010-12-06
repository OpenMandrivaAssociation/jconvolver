%define name            jconvolver
%define version         0.8.7
%define release         %mkrel 2

Name:           %{name}
Summary:        Audio convolution engine for JACK
Version:        %{version} 
Release:        %{release}

Source:         http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio/
License:        GPLv2
Group:          Sound
BuildRequires:  clthreads-devel, libzita-convolver-devel
BuildRequires:  fftw3-devel, sndfile-devel, libjack-devel
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}
