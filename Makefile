default:
	pdflatex bbz_fonll.tex
	pdflatex bbz_fonll.tex
	bibtex bbz_fonll
	bibtex bbz_fonll
	pdflatex bbz_fonll.tex
	pdflatex bbz_fonll.tex

clean:
	rm -rf *~ *.aux *.dvi *.log *.pdf.pdf *.toc *.blg *.out 
