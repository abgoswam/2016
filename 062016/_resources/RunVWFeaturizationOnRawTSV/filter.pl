my @header = ();
my $count = 0;
open F, "raw.tsv";
my @columns = qw(time camp_id offer_id lp_id click_lead click_leadvalue);
print join("\t", @columns) . "\n";
while (<F>) {
	chomp;
	if ($count++ == 0) { 
		@header = split(/\t/,$_);
	} else {
		my %hash = ();
		my @items = split(/\t/,$_);
		for (my $i= 0; $i<@header; $i++) {
			$hash{$header[$i]} = $items[$i];
		}
		if ($hash{'bucket'} = "rr" && $hash{'offer_id'} != 0) {
			my @list = ();
			map { push(@list, $hash{$_}) ; } @columns;
			print join("\t", @list) . "\n";

		}

	}
}