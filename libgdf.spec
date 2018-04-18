Name:       libgdf
Version:	%{VERSION}
Release:    1%{?dist}
Summary:	C GPU Dataframe Library
License:	Apache 2.0
URL:		https://github.com/gpuopenanalytics/libgdf
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake
#BuildRequires:	apache-arrow-devel
BuildRequires:	moderngpu-devel

%description
libgdf is a C library for implementing common functionality for a GPU Data Frame.

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
mkdir build
cd build && cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr && make %{?_smp_mflags}

%check
cd build && make pytest

%install
rm -rf $RPM_BUILD_ROOT
cd build && make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
