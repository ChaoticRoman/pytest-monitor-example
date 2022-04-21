# Pytest-monitor example

Pytest-monitor is a plugin for monitoring system resources consumption.

The aim of this example is to provide a simple dockerized application with
test suite that is analyzed by pytest-monitor.

The sample app is a converter from TWh/year to GW.

## Requirements

Docker and make are the only requirement, install these on Debian-like systems
with

```
sudo apt install docker.io make
```

## Testing

Test the application with

```
make test
```

Various metrics for whole test suite are provided using `/usr/bin/time -v` command.
One of the most useful metrics is "Maximum resident set size (kbytes)" for peak
memory usage.

## Interactive testing

Enter the container with

```
make interactive
```

and run the test suite using

```
pytest-3 tests
```

A sqlite3 database with test metrics is created under the name `.pymon`:

```
$ make interactive
root@33171639d7fc:/opt/pytest-monitor-example# ls .pymon
ls: cannot access '.pymon': No such file or directory
root@33171639d7fc:/opt/pytest-monitor-example# pytest-3 tests/
========================================================================================== test session starts ===========================================================================================
platform linux -- Python 3.9.2, pytest-6.0.2, py-1.10.0, pluggy-0.13.0
rootdir: /opt/pytest-monitor-example
plugins: monitor-1.6.3
collected 3 items

tests/test_float.py ...                                                                                                                                                                            [100%]

=========================================================================================== 3 passed in 0.02s ============================================================================================
root@33171639d7fc:/opt/pytest-monitor-example# ls .pymon
.pymon
```

There is a helper script to analyze restulting test metrics database, use it with

```
./testit
```

## Usage [Not implemented yet]

```
make run
```

Enter a value of yearly consumption in TWh and see the result. The application
either gives result for valid input, complains on invalid input or quits for
empty value.
