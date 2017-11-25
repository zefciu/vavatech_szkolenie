lekcja1.pdf: lekcja1.latex styles.tex console.tex script.tex literals.tex operators.tex assignment.tex
	latex -output-format pdf lekcja1.latex

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
