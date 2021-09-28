"""Tests all examples in the ../examples folder
with all the solvers available"""
from glob import glob
from os.path import join
import types
import importlib.machinery
import pytest
from cpmpy import *

EXAMPLES = glob(join("..", "examples", "*.py")) + glob(join(".", "examples", "*.py"))

@pytest.mark.parametrize("example", EXAMPLES)
def test_examples(example):
    """Loads example files and executes with default solver

class TestExamples(unittest.TestCase):

    Args:
        example ([string]): Loaded with parametrized example filename
    """
    loader = importlib.machinery.SourceFileLoader("example", example)
    mod = types.ModuleType(loader.name)
    loader.exec_module(mod)
    
    # run again with minizinc, if installed on system
    mzn_slv = SolverLookup.lookup('minizinc')
    if mzn_slv.supported():
        # temporarily brute-force overwrite SolverLookup.base_solvers
        f = SolverLookup.base_solvers
        try:
            SolverLookup.base_solvers = lambda: [('minizinc', mzn_slv)]
            loader.exec_module(mod)
        finally:
            SolverLookup.base_solvers = f
