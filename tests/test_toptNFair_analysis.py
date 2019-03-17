import numpy as np
import pandas as pd

from pytest import approx

from lenskit.metrics.topnFair import * 
from lenskit import topnFair  
import lk_test_utils as lktu 

def test_run_one():
    rla = topnFair.FairRecListAnalysis()
    rla.add_metric('rND')

    recs = pd.DataFrame({'user': 1, 'item': [2] 'Action': [0]})
    #truth = pd.DataFrame({'user': 1, 'item': [1, 2, 3], 'rating': [3.0, 5.0, 4.0]})

    res = rla.compute(recs, truth)

    assert res.index.name == 'user'
    assert res.index.is_unique

    assert len(res) == 1
    assert all(res.index == 1)
    assert all(res.precision == 1.0)
    assert res.recall.values == approx(1/3)