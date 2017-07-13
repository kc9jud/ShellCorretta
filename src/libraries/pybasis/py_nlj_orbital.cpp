/****************************************************************
  py_nlj_orbital.cpp

  Patrick J. Fasano
  University of Notre Dame
  European Centre for Theoretical Studies
    in Nuclear Physics and Related Areas

****************************************************************/


#include <iostream>
#include <string>
#include <sstream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "basis/nlj_orbital.h"
#include "pybasis/converters.h"

#include "pybasis/py_nlj_orbital.h"

namespace pybasis {

std::vector<basis::OrbitalPNInfo> ParseOrbitalPNStreamWrapper(py::object& object, bool standalone) {
  PythonStreamBuf buf(object);
  std::istream input(&buf);
  return basis::ParseOrbitalPNStream(input, standalone);
}

void init_orbital_nlj(py::module &module) {
  py::enum_<basis::OrbitalSpeciesPN>(module, "OrbitalSpeciesPN")
    .value("kP", basis::OrbitalSpeciesPN::kP)
    .value("kN", basis::OrbitalSpeciesPN::kN)
  ;

  py::class_<basis::OrbitalPNInfo>(module, "OrbitalPNInfo")
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

  module.def("ParseOrbitalPNStream", ParseOrbitalPNStreamWrapper);
  module.def("OrbitalDefinitionStr", basis::OrbitalDefinitionStr);
}

}  // namespace pybasis
