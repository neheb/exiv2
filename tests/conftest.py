# -*- coding: utf-8 -*-

import os

import system_tests

_HERE = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption(
        "--suite-conf",
        action="store",
        default=None,
        help="Path to the test suite's configuration file (defaults to suite.conf)",
    )


def pytest_configure(config):
    """
    Configure the test suite before any test module is imported.

    The CaseMeta metaclass used by all system tests requires the substitution
    dictionary to be populated at class-definition time, so the suite must be
    configured before pytest starts collecting the test modules.
    """
    conf_file = config.getoption("--suite-conf") or os.path.join(_HERE, "suite.conf")
    verbose = config.getoption("verbose") if hasattr(config, "getoption") else 0
    system_tests.set_debug_mode("VERBOSE" in os.environ or bool(verbose))
    system_tests.configure_suite(conf_file)
