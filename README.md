# Pytest-monitor example

Pytest-monitor is a plugin for monitoring system resources consumption.

The aim of this example is to provide a simple dockerized application with
test suite that is analyzed by pytest-monitor.

The sample app is a converter from TWh/year to GW.

## Requirements

Docker is the only requirement, install it on Debian-like systems with

```
sudo apt install docker.io
```

## Testing

```
make test
```

## Usage

```
make run
```

Enter a value of yearly consumption in TWh and see the result. The application
either gives result for valid input, complains on invalid input or quits for
empty value.
