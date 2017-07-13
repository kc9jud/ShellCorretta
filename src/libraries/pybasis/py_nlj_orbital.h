#ifndef PYBASIS_NLJ_ORBITAL_H_
#define PYBASIS_NLJ_ORBITAL_H_

#include <pybind11/pybind11.h>
namespace py = pybind11;

namespace pybasis {
  void init_orbital_nlj(py::module &module);
}

#endif
