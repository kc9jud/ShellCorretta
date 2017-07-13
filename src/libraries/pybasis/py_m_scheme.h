#ifndef PYBASIS_M_SCHEME_H_
#define PYBASIS_M_SCHEME_H_

#include <pybind11/pybind11.h>
namespace py = pybind11;

namespace pybasis {
  void init_m_scheme(py::module &module);
}

#endif
