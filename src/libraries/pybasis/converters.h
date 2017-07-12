#ifndef PYBASIS_CONVERTERS_H_
#define PYBASIS_CONVERTERS_H_

#include <boost/python.hpp>
#include <boost/iostreams/concepts.hpp>  // boost::iostreams::source
#include <boost/iostreams/stream.hpp>
#include <iostream>
#include <iosfwd> // std::streamsize

namespace pybasis {

// Type that implements the Boost.IOStream's Source concept for reading
// data from a Python object supporting read(size).
//
// Taken from https://stackoverflow.com/a/24984472 (Tanner Sansbury)
class PythonInputDevice
  : public boost::iostreams::source // Use convenience class.
{
public:

  explicit PythonInputDevice(boost::python::object object);
  std::streamsize read(char_type* buffer, std::streamsize buffer_size);

private:
  boost::python::object object_;
};

}  // namespace pybasis

#endif
