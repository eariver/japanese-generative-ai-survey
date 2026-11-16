$ENV{'TEXINPUTS'} = '../../../templates/daily-x//:' . ($ENV{'TEXINPUTS'} // '');
$pdf_mode = 4;
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -halt-on-error %O %S';