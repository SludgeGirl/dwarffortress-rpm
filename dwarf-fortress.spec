Name:           dwarf-fortress
Version:        50.13
Release:        1%{?dist}
License:        custom:dwarffortress
Summary:        Dwarf fortress
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source1: dwarfort
Source2: dwarffortress.desktop
Source3: dwarffortress.png

BuildRequires: curl
BuildRequires: coreutils
BuildRequires: tar

Requires: SDL2_image-devel
Requires: SDL2_mixer-devel

%description
Dwarf Fortress is a single-player fantasy game. You can control a dwarven outpost or an adventurer in a randomly generated, persistent world. 

%prep
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}
install %{SOURCE2} %{buildroot}/%{_datadir}/applications
install %{SOURCE3} %{buildroot}/%{_datadir}/pixmaps

%install
HASH=7cbad9a4493123bbd39c41e54547b5c34faf60cad7c3dec43e7883fd9a7e9fa7

mkdir -p %{buildroot}%{_libdir}/%{name}

curl -o %{buildroot}%{_libdir}/%{name}/%{name}.tar.bz2 -O "https://bay12games.com/dwarves/df_$(echo %{version} | sed -r 's/\./_/g')_linux.tar.bz2"
sha=$( sha256sum %{buildroot}%{_libdir}/%{name}/%{name}.tar.bz2 | awk '{ print $1 }' )

if [[ $sha == $HASH ]]; then
    echo "hash matched. Continuing".
else
    echo "hash failed to match. Failing".
    exit 1
fi

tar -xjf %{buildroot}%{_libdir}/%{name}/%{name}.tar.bz2 -C %{buildroot}%{_libdir}/%{name}
rm %{buildroot}%{_libdir}/%{name}/%{name}.tar.bz2

%files
%doc readme.txt release\ notes.txt command\ line.txt
%{_libdir}/%{name}/*
%{_bindir}/dwarfort

%changelog