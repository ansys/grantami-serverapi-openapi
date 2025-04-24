# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from enum import Enum
import types

import ansys.grantami.serverapi_openapi.models as models
import pytest

ALL_MODELS = {
    k: v
    for k, v in models.__dict__.items()
    if isinstance(v, type) and k not in ("ModelBase", "Unset_Type") and not issubclass(v, Enum)
}
POLYMORPHIC_MODELS = {
    k: v for k, v in ALL_MODELS.items() if "discriminator_value_class_map" in v.__dict__
}
MONOMORPHIC_MODELS = {k: v for k, v in ALL_MODELS.items() if k not in POLYMORPHIC_MODELS.keys()}


@pytest.mark.parametrize("cls", ALL_MODELS.values())
def test_get_real_child_model_method_exists(cls):
    assert isinstance(cls.get_real_child_model, types.MethodType)


@pytest.mark.parametrize("cls", POLYMORPHIC_MODELS.values())
def test_get_real_child_model_returns_correct_class_name(cls):
    for value, sub_cls in cls.discriminator_value_class_map.items():
        discriminator_property = cls._get_discriminator_field_name()
        sub_cls_name = cls.get_real_child_model({discriminator_property: value})
        assert sub_cls_name == sub_cls.rsplit("/", 1)[-1]


@pytest.mark.parametrize("cls", POLYMORPHIC_MODELS.values())
def test_polymorphic_child_class_exists(cls):
    for sub_cls in cls.discriminator_value_class_map.values():
        sub_cls_name = sub_cls.rsplit("/", 1)[-1]
        assert sub_cls_name in ALL_MODELS.keys()


@pytest.mark.parametrize("cls", MONOMORPHIC_MODELS.values())
def test_monomorphic_model_raises_notimplemented(cls):
    with pytest.raises(NotImplementedError):
        cls.get_real_child_model({})
