%define upstream_name    MojoMojo
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A Catalyst & DBIx::Class powered Wiki
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)
BuildRequires:	perl(Algorithm::Merge)
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(Cache::FastMmap)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:	perl(Catalyst::Controller::HTML::FormFu)
BuildRequires:	perl(Catalyst::Model::DBIC::Schema)
BuildRequires:	perl(Catalyst::Plugin::Authentication)
BuildRequires:	perl(Catalyst::Plugin::Cache)
BuildRequires:	perl(Catalyst::Plugin::ConfigLoader)
BuildRequires:	perl(Catalyst::Plugin::I18N)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Catalyst::Plugin::Session::Store::Cache)
BuildRequires:	perl(Catalyst::Plugin::Setenv)
BuildRequires:	perl(Catalyst::Plugin::Static::Simple)
BuildRequires:	perl(Catalyst::Plugin::SubRequest)
BuildRequires:	perl(Catalyst::Plugin::Unicode)
BuildRequires:	perl(Catalyst::View::Email::Template)
BuildRequires:	perl(Catalyst::View::JSON)
BuildRequires:	perl(Catalyst::View::TT)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Config::JFDI)
BuildRequires:	perl(Crypt::CBC)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::DateTime::Epoch)
BuildRequires:	perl(DBIx::Class::EncodedColumn)
BuildRequires:	perl(DBIx::Class::TimeStamp)
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Mail)
BuildRequires:	perl(Directory::Scratch)
BuildRequires:	perl(Email::Send::Test)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FCGI::ProcManager)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::MMagic)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTML::FormFu)
BuildRequires:	perl(HTML::FormFu::Element::reCAPTCHA)
BuildRequires:	perl(HTML::FormFu::Model::DBIC)
BuildRequires:	perl(HTML::Strip)
BuildRequires:	perl(HTML::TagCloud)
BuildRequires:	perl(HTML::Toc)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Image::ExifTool)
BuildRequires:	perl(Image::Math::Constrain)
BuildRequires:	perl(Imager)
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(KinoSearch1)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Locale::Maketext::Lexicon)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Module::Pluggable::Ordered)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Net::Amazon)
BuildRequires:	perl(Number::Format)
BuildRequires:	perl(Pod::Simple::HTML)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(String::Diff)
BuildRequires:	perl(Syntax::Highlight::Engine::Kate)
BuildRequires:	perl(Template)
BuildRequires:	perl(Template::Plugin::JavaScript)
BuildRequires:	perl(Term::Prompt)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(Text::Context)
BuildRequires:	perl(Text::Emoticon::MSN)
BuildRequires:	perl(Text::MultiMarkdown)
BuildRequires:	perl(Text::Password::Pronounceable)
BuildRequires:	perl(Text::Textile)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::Fetch)
BuildRequires:	perl(URI::Find)
BuildRequires:	perl(WWW::Mechanize)
BuildRequires:	perl(WWW::Mechanize::TreeBuilder)
BuildRequires:	perl(XML::Feed)
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::LibXSLT)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(parent)

BuildArch:	noarch

%description
Mojomojo is a sort of content management system, borrowing many concepts
from wikis and blogs. It allows you to maintain a full tree-structure of
pages, and to interlink them in various ways. It has full version support,
so you can always go back to a previous version and see what's changed with
an easy AJAX- based diff system. There are also a bunch of other features
like built-in fulltext search, live AJAX preview of editing, and RSS feeds
for every wiki page.

To find out more about how you can use MojoMojo, please visit
http://mojomojo.org or read the installation instructions in the
MojoMojo::Installation manpage to try it out yourself.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 657450
- rebuild for updated spec-helper

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1
+ Revision: 644768
- update to new version 1.04

* Tue Feb 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1
+ Revision: 634729
- new version

* Sun Sep 05 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 576069
- update buildrequires:
- update to 1.02

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 553022
- adding missing buildrequires:
- adding missing buildrequires:
- update to 1.01

* Wed Dec 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.999.42-1mdv2010.1
+ Revision: 472673
- adding missing buildrequires:
- update to 0.999042
- no need to bump mkrel, previous builds failed
- adding missing buildrequires:
- add patch to run with yaml::xs
- fix %%patch0 -b arg
- adding files not packaged
- adding patch to fix fragile regex in test lib
- import perl-MojoMojo


* Sun Nov 29 2009 cpan2dist 0.999041-1mdv
- initial mdv release, generated with cpan2dist
