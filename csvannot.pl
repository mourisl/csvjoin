#!/usr/bin/env perl

use strict ;
use warnings ;

die "Usage: perl csvannot.pl [OPTIONS]:\n".
"" if (@ARGV == 0) ;

my $i ;
my %argvs = (
  "-A"=>"",
  "-B"=>"",
  "-A-key"=>"",
  "-B-key"
);
my %noparamArgvs
