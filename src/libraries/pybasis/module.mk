$(eval $(begin-module))

################################################################
# unit definitions
################################################################

# module_units_h :=
module_units_cpp-h := py_nlj_orbital pybasis pyam converters
module_units_cpp-h += py_m_scheme
# module_units_f :=
# module_programs_cpp :=
# module_programs_f :=
# module_generated :=

################################################################
# library creation flag
################################################################

$(eval $(library))
$(eval $(shared-library))

libraries/pybasis/libpybasis.so: libraries/basis/libbasis.a libraries/am/libam.a libraries/mcutils/libmcutils.a libraries/cppformat/libcppformat.a

$(eval $(end-module))
