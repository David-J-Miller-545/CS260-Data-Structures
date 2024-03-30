PY = python3

prob1 : prob1.py
	$(PY) prob1.py $(arg)

view1 : prob1.py
	less -x4 prob1.py

prob2 : prob2.py
	$(PY) prob2.py $(arg)

view2 : prob2.py
	less -x4 prob2.py

prob3 : prob3.py
	$(PY) prob3.py && gnuplot < instructions.gnuplot