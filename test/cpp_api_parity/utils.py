from collections import namedtuple

TorchNNModuleTestParams = namedtuple(
    'TorchNNModuleTestParams',
    [
        'module_name',
        'module_variant_name',
        'test_instance',
        'cpp_constructor_args',
        'arg_dict',
        'has_parity',
        'device',
        'cpp_tmp_folder',
    ]
)

TorchNNFunctionalTestParams = namedtuple(
    'TorchNNFunctionalTestParams',
    [
        'functional_variant_name',
        'test_instance',
        'cpp_constructor',
        'cpp_constructor_args',
        'arg_dict',
        'has_parity',
        'device',
        'cpp_tmp_folder',
    ]
)

CppArg = namedtuple('CppArg', ['name', 'value'])