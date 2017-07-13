#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "pybasis/py_nlj_orbital.h"
#include "pybasis/py_m_scheme.h"

#include "pybasis/pybasis.h"

namespace py = pybind11;

namespace pybasis {

PYBIND11_MODULE(pybasis, pybasis_m) {
  // initialize nlj_orbital submodule
  auto py_nlj_orbital_m = pybasis_m.def_submodule("nlj_orbital");
  init_orbital_nlj(py_nlj_orbital_m);

  // initialize m_scheme submodule
  auto py_m_scheme_m = pybasis_m.def_submodule("m_scheme");
  init_m_scheme(py_m_scheme_m);
}

}  // namespace pybasis
