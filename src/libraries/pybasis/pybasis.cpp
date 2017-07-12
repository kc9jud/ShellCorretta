#include <boost/python.hpp>
#include <boost/python/enum.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/iostreams/stream.hpp>
#include "pybasis.h"

#include "basis/nlj_orbital.h"
#include "am/halfint.h"
#include "pybasis/converters.h"

namespace py = boost::python;

namespace pybasis {

std::vector<basis::OrbitalPNInfo> ParseOrbitalPNStreamWrapper(py::object& object, bool standalone) {
  boost::iostreams::stream<PythonInputDevice> input(object);
  return basis::ParseOrbitalPNStream(input, standalone);
}

BOOST_PYTHON_MODULE(pybasis) {
  py::enum_<basis::OrbitalSpeciesPN>("OrbitalSpeciesPN")
    .value("kP", basis::OrbitalSpeciesPN::kP)
    .value("kN", basis::OrbitalSpeciesPN::kN)
  ;

  py::class_<basis::OrbitalPNInfo>("OrbitalPNInfo")
    .def(py::init<basis::OrbitalSpeciesPN,int,int,HalfInt,double>())
    .def(str(py::self))
    .def_readonly("orbital_species",&basis::OrbitalPNInfo::orbital_species)
    .def_readonly("n",&basis::OrbitalPNInfo::n)
    .def_readonly("l",&basis::OrbitalPNInfo::l)
    .def_readonly("j",&basis::OrbitalPNInfo::j)
    .def_readonly("weight",&basis::OrbitalPNInfo::weight)
  ;

  py::def("ParseOrbitalPNStream", ParseOrbitalPNStreamWrapper);
  py::def("OrbitalDefinitionStr", basis::OrbitalDefinitionStr);

  py::class_< std::vector<basis::OrbitalPNInfo> >("OrbitalPNInfoVec")
    .def(py::vector_indexing_suite< std::vector<basis::OrbitalPNInfo> >())
  ;
}

BOOST_PYTHON_MODULE(pyam) {
  py::class_<HalfInt>("HalfInt")
    .def(py::init<int,int>())
    .def(py::init<int>())
    .def(float_(py::self))
    .def("TwiceValue", &HalfInt::TwiceValue)
    .def("IsInteger", &HalfInt::IsInteger)
  ;

  py::implicitly_convertible<int,HalfInt>();
  py::implicitly_convertible<HalfInt,int>();
}

}  // namespace pybasis
