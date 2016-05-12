/*
MN: 12/05/16

Importowanie danych PKWiU08 do Staty i czyszczenie
*/

* Import CSV
import delimited data/pkwiu08.csv, delimiter(comma) bindquote(strict) varnames(1) encoding(UTF-8) 

* Usuwanie pustych wierszy
drop if symbol == ""
drop if regexm(symbol, "[a-z]")

* Zamian działu na nr.
replace dzial = regexs(0) if regexm(dzial, "[0-9]+")
destring dzial, replace

* Tylko ostateczne kategorie
keep if length(symbol) == 10
