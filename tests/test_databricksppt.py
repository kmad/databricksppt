#!/usr/bin/env python

"""Tests for `databricksppt` package."""


import unittest
from click.testing import CliRunner

from databricksppt import databricksppt
from databricksppt import cli


class Testdatabricksppt(unittest.TestCase):
    """Tests for `databricksppt` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        pass
        # print(databricksppt.toPPT(""))

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'databricksppt.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
