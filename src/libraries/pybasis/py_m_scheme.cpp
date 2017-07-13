/****************************************************************
  py_m_scheme.cpp

  Patrick J. Fasano
  University of Notre Dame
  European Centre for Theoretical Studies
    in Nuclear Physics and Related Areas

****************************************************************/


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/operators.h>

#include "basis/basis.h"
#include "basis/m_scheme.h"
#include "pybasis/pybasis.h"

#include "pybasis/py_m_scheme.h"
namespace py = pybind11;

namespace pybasis {
  void init_m_scheme(py::module &module) {
    InitBaseSubspace<basis::SingleParticleSubspacePNLabels,basis::SingleParticleStatePNLabels>(module, "BaseSingleParticleSubspacePN");
    py::class_<basis::SingleParticleSubspacePN,
          basis::BaseSubspace<basis::SingleParticleSubspacePNLabels,basis::SingleParticleStatePNLabels>
          >(module, "SingleParticleSubspacePN")
      .def(py::init<>())
      .def(py::init<const basis::OrbitalSubspacePN&>())
      .def(py::init<basis::OrbitalSpeciesPN, const std::vector<basis::OrbitalPNInfo>&>())
      .def("__str__", &basis::SingleParticleSubspacePN::LabelStr)
      .def("orbital_species",&basis::SingleParticleSubspacePN::orbital_species)
      .def("Tz",&basis::SingleParticleSubspacePN::Tz)
      .def("is_oscillator_like",&basis::SingleParticleSubspacePN::is_oscillator_like)
      .def("weight_max",&basis::SingleParticleSubspacePN::weight_max)
      .def("Nmax",&basis::SingleParticleSubspacePN::Nmax)
      .def("DebugStr",&basis::SingleParticleSubspacePN::DebugStr)
    ;

    InitBaseState<basis::SingleParticleSubspacePN>(module, "BaseSingleParticleStatePN");
    py::class_<basis::SingleParticleStatePN, basis::BaseState<basis::SingleParticleSubspacePN>>(module, "SingleParticleStatePN")
      .def(py::init<const basis::SingleParticleSubspacePN&, int>())
      .def(py::init<const basis::SingleParticleSubspacePN&, const basis::SingleParticleStatePNLabels&>())
      .def("__str__", &basis::SingleParticleStatePN::LabelStr)
      .def("orbital_species",&basis::SingleParticleStatePN::orbital_species)
      .def("Tz",&basis::SingleParticleStatePN::Tz)
      .def("n",&basis::SingleParticleStatePN::n)
      .def("l",&basis::SingleParticleStatePN::l)
      .def("j",&basis::SingleParticleStatePN::j)
      .def("m",&basis::SingleParticleStatePN::m)
      .def("g",&basis::SingleParticleStatePN::g)
      .def("full_labels",&basis::SingleParticleStatePN::full_labels)
      .def("weight",&basis::SingleParticleStatePN::weight)
      .def("N",&basis::SingleParticleStatePN::N)
    ;

    InitBaseSpace<basis::SingleParticleSubspacePN>(module, "BaseSingleParticleSpacePN");
    py::class_<basis::SingleParticleSpacePN, basis::BaseSpace<basis::SingleParticleSubspacePN>>(module, "SingleParticleSpacePN")
      .def(py::init<>())
      .def(py::init<const basis::OrbitalSpacePN&>())
      .def(py::init<const std::vector<basis::OrbitalPNInfo>&>())
      .def("weight_max",&basis::SingleParticleSpacePN::weight_max)
      .def("is_oscillator_like",&basis::SingleParticleSpacePN::is_oscillator_like)
      .def("Nmax",&basis::SingleParticleSpacePN::Nmax)
      .def("DebugStr",&basis::SingleParticleSpacePN::DebugStr)
    ;

  }

}  // namespace pybasis
