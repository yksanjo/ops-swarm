import importlib


def test_main_exists():
    mod = importlib.import_module("ops_swarm.cli")
    assert hasattr(mod, "main")
