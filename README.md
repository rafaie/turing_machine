# Turing machine

The code is implemented in Python 3.

## How to run
### Method 1
Call "turing.py" with the arguments. It's the list of arguments supported by the application:

```
> python turing.py -h
usage: turing.py [-h] [-mt MAX_TRANSITIONS] [-f] [-v] init_string

positional arguments:
  init_string           define init_string string

optional arguments:
  -h, --help            show this help message and exit
  -mt MAX_TRANSITIONS, --max_transitions MAX_TRANSITIONS
                        define the max_transitions
  -f, --file            define a file path includes init_string
  -v, --verbose         Show more details
```

Example 1:
```
python3 turing.py -f testcase6.txt
```

Example 2:
```
python3 turing.py "#q0,a->qa,a,R#q0,a->q1,a,R#q0,b->q1,b,R#q0,_->q1,_,R#q1,b->q1,b,R#q1,_->q1,_,R#q1,a->qr,a,R#q1,b->qr,b,R##ab#"
```

### Method 2
It is easier method to run it over all the test-cases:
```
./run_tests.sh
```
