Summary:	ACS CCID (Chip/Smart Card Interface Devices) PC/SC driver
Summary(pl.UTF-8):	Sterownik PC/SC CCID (Chip/Smart Card Interface Devices) dla czytników ACS
Name:		pcsc-driver-acsccid
Version:	1.0.8
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# from e.g. http://www.acs.com.hk/en/driver/4/acr38-smart-card-reader/
# (the same Linux driver is used for multiple ACS card readers)
Source0:	http://www.acs.com.hk/download-driver-unified/6258/ACS-Unified-Driver-Lnx-Mac-108-P.zip
# Source0-md5:	0b235156a66f280a81f949b0c9bb3052
URL:		http://www.acs.com.hk/en/drivers/
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	pcsc-lite-devel >= 1.3.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	unzip
Requires:	pcsc-lite >= 1.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers

# pcscd provides log_msg and log_xxd functions
#define		skip_post_check_so	libccid.so.1.4.0 libccidtwin.so.1.4.0

%description
This package provides CCID (Chip/Smart Card Interface Devices) PC/SC
driver for ACS CCID smart card readers.

%description -l pl.UTF-8
Ten pakiet zawiera sterownik PC/SC CCID (Chip/Smart Card Interface
Devices) dla czytników kart firmy ACS zgodnych z CCID.

%prep
%setup -q -n ACS-Unified-Driver-Lnx-Mac-108-P
tar xjf acsccid-%{version}.tar.bz2

%build
cd acsccid-%{version}
%configure \
	--disable-silent-rules \
	--enable-usbdropdir=%{usbdropdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/udev/rules.d

%{__make} -C acsccid-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p acsccid-%{version}/src/92_pcscd_acsccid.rules $RPM_BUILD_ROOT/lib/udev/rules.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc acsccid-%{version}/{AUTHORS,ChangeLog,README}
%dir %{usbdropdir}/ifd-acsccid.bundle
%dir %{usbdropdir}/ifd-acsccid.bundle/Contents
%{usbdropdir}/ifd-acsccid.bundle/Contents/Info.plist
%dir %{usbdropdir}/ifd-acsccid.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/ifd-acsccid.bundle/Contents/Linux/libacsccid.so
/lib/udev/rules.d/92_pcscd_acsccid.rules
