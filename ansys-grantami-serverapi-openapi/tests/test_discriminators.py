import types
import inspect
import pytest
import ansys.grantami.serverapi_openapi.models as models


ALL_MODELS = {
    k: v for k, v in models.__dict__.items() if isinstance(v, type) and k != "ModelBase"
}
POLYMORPHIC_MODELS = {
    k: v for k, v in ALL_MODELS.items() if "discriminator_value_class_map" in v.__dict__
}
MONOMORPHIC_MODELS = {
    k: v for k, v in ALL_MODELS.items() if k not in POLYMORPHIC_MODELS.keys()
}


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
    kwargs = {}
    for param in inspect.getfullargspec(cls.__init__).kwonlyargs:
        kwargs[param] = f"{param}Value"

    with pytest.raises(NotImplementedError):
        cls(**kwargs).get_real_child_model({})
