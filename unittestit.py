#!/usr/bin/env python3
import unittest
import memory_profiler


def process_suite(suite):
    tests = collect_tests(suite)

    results = [process_test(test) for test in tests]

    results.sort(key=lambda r: r["max_usage"], reverse=True)

    for r in results:
        print(f"{str(r['suite']):72s} {r['max_usage']:8.2f} MB")


def collect_tests(suite):
    single_test_suites = []

    if hasattr(suite, '__iter__'):
        for x in suite:
            single_test_suites += collect_tests(x)
    else:
        single_test_suites.append(suite)

    return single_test_suites


def process_test(suite):
    suite.setUpClass()
    m = memory_profiler.memory_usage(
        (lambda: suite.run(), (), {}), max_usage=True)[0]
    suite.tearDownClass()
    return {"suite": suite, "max_usage": m}


if __name__ == "__main__":
    process_suite(unittest.defaultTestLoader.discover('tests'))
