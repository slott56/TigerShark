use 5.000;
use ExtUtils::MakeMaker;
# See lib/ExtUtils/MakeMaker.pm for details of how to influence
# the contents of the Makefile that is written.
WriteMakefile(
   'NAME'          => 'X12::Parser',
   'VERSION_FROM'  => 'lib/X12/Parser.pm', # finds $VERSION
   'PREREQ_PM'     => {}, # e.g., Module::Name => 1.1
   'PM' => {
   'Readme.pod'               => '$(INST_MAN3DIR)/Parser/Readme.pod',
   'lib/X12/Parser.pm'        => '$(INST_LIBDIR)/Parser.pm',
   'lib/X12/Parser/Cf.pm'     => '$(INST_LIBDIR)/Parser/Cf.pm',
   'cf/270_004010X092.cf'     => '$(INST_LIBDIR)/Parser/cf/270_004010X092.cf',
   'cf/271_004010X092.cf'     => '$(INST_LIBDIR)/Parser/cf/271_004010X092.cf',
   'cf/276_004010X093.cf'     => '$(INST_LIBDIR)/Parser/cf/276_004010X093.cf',
   'cf/277_004010X092.cf'     => '$(INST_LIBDIR)/Parser/cf/277_004010X092.cf',
   'cf/278_004010X094_Req.cf' => '$(INST_LIBDIR)/Parser/cf/278_004010X094_Req.cf',
   'cf/278_004010X094_Res.cf' => '$(INST_LIBDIR)/Parser/cf/278_004010X094_Res.cf',
   'cf/820_004010X061.cf'     => '$(INST_LIBDIR)/Parser/cf/820_004010X061.cf',
   'cf/834_004010X095.cf'     => '$(INST_LIBDIR)/Parser/cf/834_004010X095.cf',
   'cf/835_004010X091.cf'     => '$(INST_LIBDIR)/Parser/cf/835_004010X091.cf',
   'cf/837_004010X096.cf'     => '$(INST_LIBDIR)/Parser/cf/837_004010X096.cf',
   'cf/837_004010X097.cf'     => '$(INST_LIBDIR)/Parser/cf/837_004010X097.cf',
   'cf/837_004010X098.cf'     => '$(INST_LIBDIR)/Parser/cf/837_004010X098.cf',
   'cf/997.cf'                => '$(INST_LIBDIR)/Parser/cf/997.cf',
   },
   ($] ge '5.005') ? (
    'AUTHOR'    => 'Prasad Poruporuthan (prasad@cpan.org)',
    'ABSTRACT'  => 'Perl module for parsing X12 transaction files',
   ) : (),
);



