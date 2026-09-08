$ENV{'TEXINPUTS'} = '../../../templates/daily-x//:' . ($ENV{'TEXINPUTS'} // '');
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error %O %S';
$max_repeat = 5;
