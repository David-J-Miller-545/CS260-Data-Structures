prob1 : concatListDriver.py concatLists.py cell.py
	python3 -c "import concatListDriver; concatListDriver.prob1()"

prob2 : concatListDriver.py concatLists.py cell.py
	python3 -c "import concatListDriver; concatListDriver.prob2()"

time : concatListDriver.py concatLists.py cell.py 
	python3 -c "import concatListDriver; concatListDriver.time()" && gnuplot < instructions.gnuplot

view : concatLists.py
	less -x4 concatLists.py
