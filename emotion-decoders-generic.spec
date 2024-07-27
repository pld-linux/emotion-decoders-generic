Summary:	Generic decoders for Emotion library
Summary(pl.UTF-8):	Ogólne programy dekodujące dla biblioteki Emotion
Name:		emotion-decoders-generic
Version:	1.11.0
Release:	1
License:	BSD
Group:		Libraries
#Source0:	http://download.enlightenment.org/rel/libs/emotion_generic_players/emotion_generic_players-%{version}.tar.bz2
Source0:	http://sources.openembedded.org/emotion_generic_players-%{version}.tar.gz
# Source0-md5:	432febd580ed1a4d7d7b42984ee4c693
URL:		https://www.enlightenment.org/_legacy_embed/emotion_main.html
BuildRequires:	ecore-devel >= 1.8.0
BuildRequires:	eina-devel >= 1.2.0
BuildRequires:	emotion-devel >= 1.11
BuildRequires:	pkgconfig
BuildRequires:	vlc-devel >= 2.0
Requires:	ecore >= 1.8.0
Requires:	eina >= 1.2.0
Requires:	emotion >= 1.11
Requires:	vlc >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		arch_tag	v-1.11

%description
These are binary players for Emotion using the "generic" module.

Emotion supports multiple modules provided as shared-objects under
LIBDIR/emotion/modules, making it extensible. However these live in
the same process as the application, thus problems handling the media
may crash or halt the application. Unfortunately media handling is
very error prone due multiple sources, sinks, decoders et al, each
with their own level of stability.

To solve this, Emotion ships with a "generic" module that is a layer
to talk to another process, the "player", using pipes and shared
memory (shm). If this external process dies, the main application
remains working (without any media, of course). Thus it is safer and
has some nice side effects such as avoiding bringing in many libraries
to decode media, saving memory in the application process, etc.

A secondary benefit is that the generic player is a separate process
and does not link with the user application code or EFL, avoiding
license conflicts. Many decoding libraries or elements exist with
conflicting licenses with GPL, LGPL or even proprietary code.

%description -l pl.UTF-8
Ten pakiet zawiera binarne odtwarzacze dla Emotion wykorzystujące
moduł "generic".

Biblioteka Emotion obsługuje wiele modułów dostarczanych jako obiekty
współdzielone w LIBDIR/emotion/modules, co czyni ją rozszerzalną.
Jednak te moduły działają w tym samym procesie, co aplikacja, więc
problemy z obsługą treści mogą spowodować awarię lub zawieszenie
aplikacji. Niestety obsługa multimediów jest bardzo podatna na błędy
ze względu na wiele źródeł, warstw, dekoderów itp., z których każdy ma
własny poziom stabilności.

Aby ten problem rozwiązać, Emotion jest dostarczany z modułem ogólnym
"generic", który jest warstwą pozwalającą na porozumiewanie z innym
procesem "odtwarzacza" przy użyciu potoków i pamięci dzielonej (shm).
Jeśli ten zewnętrzny proces zginie, główna aplikacja działa nadal
(oczywiście bez odtwarzanej treści). Ten sposób jest bezpieczniejszy i
ma dodatkowe pozytywne efekty uboczne, takie jak unikanie dodawania
wielu bibliotek do dekodowania multimediów, oszczędzanie pamięci w
procesie aplikacji itp.

Dodatkową zaletą jest to, że odtwarzacz ogólny jest osobnym procesem i
nie linkuje się z kodem aplikacji użytkownika ani EFL, co zapobiega
konfliktom licencji. Wiele bibliotek lub elementów dekodujących ma
licencje niezgodne z GPL, LGPL, albo jest kodem własnościowym.

%prep
%setup -q -n emotion_generic_players-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%dir %{_libdir}/emotion/generic_players
%dir %{_libdir}/emotion/generic_players/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/generic_players/%{arch_tag}/vlc
