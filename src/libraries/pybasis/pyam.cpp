#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "am/halfint.h"

#include "pybasis/pyam.h"

namespace py = pybind11;

PYBIND11_MODULE(pyam, pyam_m) {
  py::class_<HalfInt>(pyam_m, "HalfInt")
    .def(py::init<int,int>())
    .def(py::init<int>())
    .def("TwiceValue", &HalfInt::TwiceValue)
    .def("IsInteger", &HalfInt::IsInteger)
    .def("__str__", &HalfInt::Str)
    .def("__repr__", &HalfInt::Str)
  ;

  py::implicitly_convertible<float,HalfInt>();
}
