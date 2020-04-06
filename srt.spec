Name:           srt
Version:        1.2.3
Release:        2%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPLv2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  gnutls-devel

Requires: srt-libs%{?_isa} = %{version}-%{release}


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
%cmake \
  -DENABLE_STATIC=OFF \
  -DUSE_GNUTLS=ON \
  .

%make_build


%install
%make_install
# remove old upstream temporary compatibility pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc


%ldconfig_scriptlets libs


%files
%license LICENSE
%doc README.md docs
%{_bindir}/stransmit

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc


%changelog
* Mon Apr 06 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.2.3-2
- Switch to gnutls instead of openssl
- Enable tests
- Enforce strict EVR from main to -libs
- Switch branch to 1.2.3 for epel7

* Thu Aug  1 2019 Yanko Kaneti <yaneti@declera.com> - 1.2.3-1
- Initial spec
