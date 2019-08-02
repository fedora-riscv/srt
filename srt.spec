Name:           srt
Version:        1.3.3
Release:        3%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPLv2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  openssl-devel

%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as 
the Internet.

%package libs
Summary: Secure Reliable Transport protocol libraries

%description libs
Secure Reliable Transport protocol libraries

%package devel
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: srt-libs%{?_isa} = %{version}-%{release}

%description devel
Secure Reliable Transport protocol development libraries and header files


%prep
%autosetup


%build
%cmake -DENABLE_STATIC=OFF
%make_build


%install
%make_install
# remove old upstream temporary compatibility pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc


%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc

%changelog
* Thu Aug  1 2019 Yanko Kaneti <yaneti@declera.com> - 1.3.3-3
- First attempt
- Adjustments suggested by review
