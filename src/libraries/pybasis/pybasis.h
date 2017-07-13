#ifndef PYBASIS_PYBASIS_H_
#define PYBASIS_PYBASIS_H_

#include <pybind11/pybind11.h>
#include "basis/basis.h"

namespace py = pybind11;

template <typename tSubspaceLabelsType, typename tStateLabelsType>
  void InitBaseSubspace(py::module &module, const char *name)
{
  typedef basis::BaseSubspace<tSubspaceLabelsType, tStateLabelsType> base;
  py::class_<base>(module, name)
    .def("labels",&base::labels)
    .def("GetStateLabels",&base::GetStateLabels)
    .def("ContainsState",&base::ContainsState)
    .def("LookUpStateIndex",&base::LookUpStateIndex)
    .def("size",&base::size)
  ;
}

template <typename tSubspaceType>
  void InitBaseState(py::module &module, const char *name)
{
  typedef basis::BaseState<tSubspaceType> base;
  py::class_<base>(module, name)
    .def("labels",&base::labels)
    .def("index",&base::index)
  ;
}

template <typename tSubspaceType>
  void InitBaseSpace(py::module &module, const char *name)
{
  typedef basis::BaseSpace<tSubspaceType> base;
  py::class_<base>(module, name)
    .def("ContainsSubspace",&base::ContainsSubspace)
    .def("LookUpSubspaceIndex",&base::LookUpSubspaceIndex)
    .def("LookUpSubspace",&base::LookUpSubspace)
    .def("GetSubspace",&base::GetSubspace)
    .def("size",&base::size)
    .def("Dimension",&base::Dimension)
  ;
}
#endif
