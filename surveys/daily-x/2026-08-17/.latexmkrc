$ENV{'TEXINPUTS'} = '../../../templates/daily-x//:' . ($ENV{'TEXINPUTS'} // '');
do '../../../.latexmkrc';
