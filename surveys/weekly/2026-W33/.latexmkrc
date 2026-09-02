$ENV{'TEXINPUTS'} = '../../../templates/survey//:' . ($ENV{'TEXINPUTS'} // '');
do '../../../.latexmkrc';
