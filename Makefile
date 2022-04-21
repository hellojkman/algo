main :
	python3 test.py < test.in > result.out
test :
	python3 test.py < test.in > result.out
	diff -r test.out result.out