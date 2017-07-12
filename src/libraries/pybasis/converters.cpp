#include <boost/iostreams/concepts.hpp>  // boost::iostreams::source
#include <boost/iostreams/stream.hpp>
#include <iostream>
#include <algorithm> // std::copy
#include <iosfwd> // std::streamsize

#include "converters.h"

namespace py = boost::python;

namespace pybasis {
// Type that implements the Boost.IOStream's Source concept for reading
// data from a Python object supporting read(size).
//
// Taken from https://stackoverflow.com/a/24984472 (Tanner Sansbury)
PythonInputDevice::PythonInputDevice(py::object object)
  : object_(object)
{}

std::streamsize PythonInputDevice::read(char_type* buffer, std::streamsize buffer_size)
{
  // Read data through the Python object's API.  The following is
  // is equivalent to:
  //   data = object_.read(buffer_size)
  py::object py_data = object_.attr("read")(buffer_size);
  std::string data = py::extract<std::string>(py_data);

  // If the string is empty, then EOF has been reached.
  if (data.empty())
  {
    return -1; // Indicate end-of-sequence, per Source concept.
  }

  // Otherwise, copy data into the buffer.
  copy(data.begin(), data.end(), buffer);
  return data.size();
}

}  // namespace pybasis
