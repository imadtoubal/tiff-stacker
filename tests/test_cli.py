import pytest
from click.testing import CliRunner

from stiff import cli


@pytest.fixture
def runner():
  return CliRunner()


def test_cli(runner):  # pylint: disable=redefined-outer-name
  result = runner.invoke(cli.main)
  assert result.exit_code == 0
  assert not result.exception
  assert result.output.strip() == 'Hello, world.'


def test_cli_with_option(runner):  # pylint: disable=redefined-outer-name
  result = runner.invoke(cli.main, ['--as-cowboy'])
  assert not result.exception
  assert result.exit_code == 0
  assert result.output.strip() == 'Howdy, world.'


def test_cli_with_arg(runner):  # pylint: disable=redefined-outer-name
  result = runner.invoke(cli.main, ['Imad'])
  assert result.exit_code == 0
  assert not result.exception
  assert result.output.strip() == 'Hello, Imad.'
