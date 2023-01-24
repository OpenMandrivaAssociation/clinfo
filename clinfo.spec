%define _empty_manifest_terminate_build 0

Name:		clinfo
Summary:	Enumerates OpenCL platform and device properties
Version:	3.0.21.02.21
Release:	1
Group:		System/Configuration
License:	CC0
URL:		https://github.com/Oblomov/clinfo
Source0:	https://github.com/Oblomov/clinfo/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(ocl-icd)

%description
A simple command-line application that enumerates all possible (known)
properties of the OpenCL platform and devices available on the
system. Inspired by AMD's program of the same name, it is coded in
pure C and it tries to output all possible information, including
those provided by platform-specific extensions, trying not to crash on
unsupported properties (e.g. 1.2 properties on 1.1 platforms).

%prep
%autosetup -p1

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1

install -m 0755 ./%{name} %{buildroot}%{_bindir}/
install -m 0644 ./man1/%{name}.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE legalcode.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
