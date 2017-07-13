#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "pybasis/py_nlj_orbital.h"

#include "pybasis/pybasis.h"

namespace py = pybind11;

namespace pybasis {

PYBIND11_MODULE(pybasis, pybasis_m) {
  auto py_nlj_orbital_m = pybasis_m.def_submodule("nlj_orbital");
  init_orbital_nlj(py_nlj_orbital_m);
}

}  // namespace pybasis
