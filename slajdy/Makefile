all: lekcja1.pdf lekcja2.pdf
lekcja2.pdf: lekcja2.latex styles.tex if_statement.tex while_statement.tex for_statement.tex Makefile
	latex -output-format pdf lekcja2.latex

lekcja1.pdf: lekcja1.latex styles.tex console.tex script.tex literals.tex operators.tex assignment.tex float.tex tuple.tex zadanie1.tex unmutable.tex mutable.tex mutable-copy.tex list.tex list.tex dict.tex Makefile
	latex -output-format pdf lekcja1.latex

# Lekcja 1
styles.tex: Makefile                                                            
	pygmentize -S manni -f latex > styles.tex                                   

console.tex: console.pycon Makefile                                               
	pygmentize -l pycon -o console.tex console.pycon

script.tex: script.py Makefile
	pygmentize -l py -o script.tex script.py

literals.tex: literals.py Makefile
	pygmentize -l py -o literals.tex literals.py

operators.tex: operators.pycon Makefile
	pygmentize -l pycon -o operators.tex operators.pycon

assignment.tex: assignment.py Makefile
	pygmentize -l py -o assignment.tex assignment.py

float.tex: float.pycon Makefile
	pygmentize -l pycon -o float.tex float.pycon

tuple.tex: tuple.pycon Makefile
	pygmentize -l pycon -o tuple.tex tuple.pycon

zadanie1.tex: zadanie1.bash Makefile
	pygmentize -l bash -o zadanie1.tex zadanie1.bash

unmutable.tex: unmutable.pycon Makefile                                               
	pygmentize -l pycon -o unmutable.tex unmutable.pycon

mutable.tex: mutable.pycon Makefile                                               
	pygmentize -l pycon -o mutable.tex mutable.pycon

mutable-copy.tex: mutable-copy.pycon Makefile                                               
	pygmentize -l pycon -o mutable-copy.tex mutable-copy.pycon

list.tex: list.pycon Makefile                                               
	pygmentize -l pycon -o list.tex list.pycon

dict.tex: dict.pycon Makefile                                               
	pygmentize -l pycon -o dict.tex dict.pycon

# Lekcja 2
if_statement.tex: if_statement.py Makefile                                               
	pygmentize -l py -o if_statement.tex if_statement.py

while_statement.tex: while_statement.py Makefile                                               
	pygmentize -l py -o while_statement.tex while_statement.py

for_statement.tex: for_statement.py Makefile                                               
	pygmentize -l py -o for_statement.tex for_statement.py
