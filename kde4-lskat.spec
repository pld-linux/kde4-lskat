%define		_state		stable
%define		orgname		lskat
%define		qtver		4.8.0

Summary:	KDE lskat
Summary(pl.UTF-8):	Lskat dla KDE
Summary(pt_BR.UTF-8):	Jogo de cartas Lieutenant Skat para KDE
Name:		kde4-%{orgname}
Version:	4.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a30ba2a7e2f41ff666ad224a7e2ad431
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lieutenant skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules. Every player has a set of cards
in front of him/her, half of them covered and half of them open. Both
players try to win more than 60 of the 120 possible points. After 16
moves all cards are played and the game ends.

%description -l pl.UTF-8
Lieutenant skat (oficerski skat, od niemieckiego Offizierskat) to gra
karciana dla dwóch graczy. Jest rozgrywana z grubsza na zasadach
skata, ale tylko między dwoma graczami i z uproszczonymi zasadami.
Każdy gracz ma zestaw kart przed sobą, z których połowa jest zakryta,
a połowa odkryta. Obaj gracze próbują wygrać ponad 60 ze 120 możliwych
punktów. Po 16 ruchach wszystkie karty są rozegrane i gra się kończy.

%description -l pt_BR.UTF-8
Jogo de cartas Lieutenant Skat para KDE

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lskat
%{_desktopdir}/kde4/lskat.desktop
%{_datadir}/apps/lskat
%{_iconsdir}/*/*/apps/lskat.png
