from ..tests import _asserts

HELP = """
Usage: conbench arrow-rust [OPTIONS]

  Record Arrow Rust micro benchmark results.

Options:
  --src-dir TEXT
  --commit TEXT
  --show-result BOOLEAN  [default: True]
  --show-output BOOLEAN  [default: False]
  --run-id TEXT          Group executions together with a run id.
  --run-name TEXT        Name of run (commit, pull request, etc).
  --help                 Show this message and exit.

"""


def test_cli():
    command = ["conbench", "arrow-rust", "--help"]
    _asserts.assert_cli(command, HELP)
