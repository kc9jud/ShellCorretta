#include <iostream>
#include <string>
#include <sstream>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "basis/nlj_orbital.h"
#include "am/halfint.h"
#include "pybasis/converters.h"

namespace py = pybind11;

namespace pybasis {

std::vector<basis::OrbitalPNInfo> ParseOrbitalPNStreamWrapper(py::object& object, bool standalone) {
  PythonStreamBuf buf(object);
  std::istream input(&buf);
  return basis::ParseOrbitalPNStream(input, standalone);
}

PYBIND11_MODULE(pybasis, pybasis_m) {
  py::enum_<basis::OrbitalSpeciesPN>(pybasis_m, "OrbitalSpeciesPN")
    .value("kP", basis::OrbitalSpeciesPN::kP)
    .value("kN", basis::OrbitalSpeciesPN::kN)
  ;

  py::class_<basis::OrbitalPNInfo>(pybasis_m, "OrbitalPNInfo")
    .def(py::init<>())
    .def(py::init<basis::OrbitalSpeciesPN,int,int,HalfInt,double>())
    .def("__str__", [](const basis::OrbitalPNInfo &a) {
        std::ostringstream str;
        str << a;
        return str.str();
      }, py::is_operator())
    .def_readonly("orbital_species",&basis::OrbitalPNInfo::orbital_species)
    .def_readonly("n",&basis::OrbitalPNInfo::n)
    .def_readonly("l",&basis::OrbitalPNInfo::l)
    .def_readonly("j",&basis::OrbitalPNInfo::j)
    .def_readonly("weight",&basis::OrbitalPNInfo::weight)
    .def("Key",&basis::OrbitalPNInfo::Key)
  ;

  pybasis_m.def("ParseOrbitalPNStream", ParseOrbitalPNStreamWrapper);
  pybasis_m.def("OrbitalDefinitionStr", basis::OrbitalDefinitionStr);

}

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

}  // namespace pybasis
