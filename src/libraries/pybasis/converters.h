#ifndef PYBASIS_CONVERTERS_H_
#define PYBASIS_CONVERTERS_H_

#include <streambuf>
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace pybasis {

namespace py = pybind11;

// Type that implements the Boost.IOStream's Source concept for reading
// data from a Python object supporting read(size).
//
// Taken from https://stackoverflow.com/a/24984472 (Tanner Sansbury)
class PythonStreamBuf : public std::streambuf
{
public:

  explicit PythonStreamBuf(py::object object, std::size_t buff_sz = 256, std::size_t put_back = 8);

private:
  int_type underflow();
  PythonStreamBuf(const PythonStreamBuf&);
  PythonStreamBuf& operator=(const PythonStreamBuf&);

  py::object object_;
  const std::size_t put_back_;
  std::vector<char> buffer_;
};

}  // namespace pybasis

#endif
