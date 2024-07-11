#   Copyright 2024 The PyMC Labs Developers
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
This module exists to maintain the old API where experiment classes were defined in the
`causalpy.skl_experiments` namespace. They have moved to `causalpy.experiments` and
this module is a thin wrapper around the new classes to maintain backwards
compatibility. A deprication warning is delivered to the user. This module may be
removed in a future release.
"""

import warnings

from .experiments.diff_in_diff import (
    DifferenceInDifferences as NewDifferenceInDifferences,
)
from .experiments.prepostfit import (
    InterruptedTimeSeries as NewInterruptedTimeSeries,
)
from .experiments.prepostfit import (
    SyntheticControl as NewSyntheticControl,
)
from .experiments.regression_discontinuity import (
    RegressionDiscontinuity as NewRegressionDiscontinuity,
)

# Ensure deprecation warnings are always shown in Jupyter Notebooks
warnings.simplefilter("always", DeprecationWarning)


class SyntheticControl(NewSyntheticControl):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            """causalpy.skl_experiments.SyntheticControl is deprecated and will be removed in a future release. Please use causalpy.experiments.SyntheticControl instead.""",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)


class DifferenceInDifferences(NewDifferenceInDifferences):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            """causalpy.skl_experiments.DifferenceInDifferences is deprecated and will be removed in a future release. Please use causalpy.experiments.DifferenceInDifferences instead.""",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)


class InterruptedTimeSeries(NewInterruptedTimeSeries):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            """causalpy.skl_experiments.InterruptedTimeSeries is deprecated and will be removed in a future release. Please use causalpy.experiments.InterruptedTimeSeries instead.""",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)


class RegressionDiscontinuity(NewRegressionDiscontinuity):
    def __init__(self, *args, **kwargs):
        warnings.warn(
            """causalpy.skl_experiments.RegressionDiscontinuity is deprecated and will be removed in a future release. Please use causalpy.experiments.RegressionDiscontinuity instead.""",
            DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)
