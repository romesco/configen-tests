# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any
from typing import Tuple


@dataclass
class ConfigenTestConf:
    _target_: str = "configen_tests.utils.data.dataset.ConfigenTest"
    a: int = 1
    b: Any = MISSING  # Tensor
    c: Tuple[int] = MISSING


@dataclass
class DatasetConf:
    _target_: str = "configen_tests.utils.data.dataset.Dataset"
    args: Any = MISSING
    kwds: Any = MISSING


@dataclass
class IterableDatasetConf:
    _target_: str = "configen_tests.utils.data.dataset.IterableDataset"
    args: Any = MISSING
    kwds: Any = MISSING


@dataclass
class TensorDatasetConf:
    _target_: str = "configen_tests.utils.data.dataset.TensorDataset"
    tensors: Any = MISSING  # Tensor


@dataclass
class ConcatDatasetConf:
    _target_: str = "configen_tests.utils.data.dataset.ConcatDataset"
    args: Any = MISSING
    kwds: Any = MISSING
