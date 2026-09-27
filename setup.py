from pybind_setup_ext import cpp_ext, setup, update_submodule

update_submodule('headers', force=True, remote=True)

kw = {
    'include_dirs': ["headers"]
}

setup(

    cpp_ext(
        "hwlib/hardware.cpp", **kw, 
        platforms = ['win32'],
    ),

    cpp_ext(
        "hwlib/hardware.cpp", **kw, 
        platforms = ['linux', 'darwin'],
        extra_objects = [
            "headers/hwinfo/*.a",
            "headers/pciutils/*.a",
        ],
        extra_link_args = ["-lz", "-lresolv"],
    ),

)

