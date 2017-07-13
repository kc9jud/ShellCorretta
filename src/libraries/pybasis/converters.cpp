#include <streambuf>
#include <algorithm> // std::copy
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "converters.h"

namespace py = pybind11;

namespace pybasis {
// Type that implements the Boost.IOStream's Source concept for reading
// data from a Python object supporting read(size).
//
// Taken from https://stackoverflow.com/a/24984472 (Tanner Sansbury)
PythonStreamBuf::PythonStreamBuf(py::object object, size_t buff_sz, size_t put_back) :
  object_(object),
  put_back_(std::max(put_back, size_t(1))),
  buffer_(std::max(buff_sz, put_back_) + put_back_)
{
  char *end = &buffer_.front() + buffer_.size();
  setg(end, end, end);
}

std::streambuf::int_type PythonStreamBuf::underflow() {
  if (gptr() < egptr()) // buffer not exhausted
        return traits_type::to_int_type(*gptr());

  char *base = &buffer_.front();
  char *start = base;

  if (eback() == base) // true when this isn't the first fill
  {
    // Make arrangements for putback characters
    std::memmove(base, egptr() - put_back_, put_back_);
    start += put_back_;
  }

  // Read data through the Python object's API.  The following is
  // is equivalent to:
  //   data = object_.read(buffer_size)
  py::object py_data = object_.attr("read")(buffer_.size() - (start - base));
  std::string data = py::cast<std::string>(py_data);

  // If the string is empty, then EOF has been reached.
  if (data.empty())
  {
    return traits_type::eof();
  }

  // Otherwise, copy data into the buffer.
  size_t n = data.size();
  copy(data.begin(), data.end(), start);

  // Set buffer pointers
  setg(base, start, start + n);
  return traits_type::to_int_type(*gptr());
}

}  // namespace pybasis
