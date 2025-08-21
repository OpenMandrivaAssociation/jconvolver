%global	debug_package	%{nil}

Summary:	Audio convolution engine for JACK
Name:	 jconvolver
Version:	1.1.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://www.kokkinizita.net/linuxaudio/
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Source100:	jconvolver.rpmlintrc
Patch0:	jconvolver-1.1.0-fix-makefile.patch
Patch1:	jconvolver-1.1.0-workaround-for-pipewire.patch
Patch2:	jconvolver-1.1.0-get-ldflags-from-jack-pkgconfig-file.patch
BuildRequires:	clthreads-devel
BuildRequires:	libzita-convolver-devel >=  4.0.0
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(sndfile)
# Missing
Suggests:	jconvolver-reverbs

%description
Jconvolver is a real-time convolution engine. It can execute up to a 64 by 64
convolution matrix (i.e. 4096 simultaneous convolutions) as long as your CPU
can handle the load. It is designed to be efficient also for sparse (e.g.
diagonal) matrices. Unused matrix elements do not take any CPY time.

%files
%license COPYING
%doc README.CONFIG
%{_bindir}/fconvolver
%{_bindir}/%{name}
%{_bindir}/makemulti
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix paths in configuration files
pushd config-files
	find . -name \*.conf \
		-exec sed -i -e "s|/audio/reverbs|%{_datadir}/%{name}/reverbs|g" {} \; \
		-exec sed -i -e "s|^#/cd |/cd |g" {} \;
popd


%build
pushd source
	%make_build
popd


%install
%make_install PREFIX=%{_prefix} -C source

# Install configuration files and demo reverbs
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a config-files/* %{buildroot}%{_datadir}/%{name}
