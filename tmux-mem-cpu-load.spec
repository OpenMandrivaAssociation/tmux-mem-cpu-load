Summary:	CPU, RAM, and load monitor for use with tmux
Name:		tmux-mem-cpu-load	
Version:	3.6.0
Release:	1
License:	Apache2.0
Group:		Text tools
Url:		https://github.com/thewtex/tmux-mem-cpu-load
Source0:	https://github.com/thewtex/tmux-mem-cpu-load/archive/v%{version}.tar.gz
BuildRequires:	cmake

%description
CPU, RAM, and load monitor for use with tmux

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_bindir}/%{name}
