// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from my_custom_message:msg/Visual.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "my_custom_message/msg/detail/visual__struct.h"
#include "my_custom_message/msg/detail/visual__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_custom_message__msg__visual__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[37];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("my_custom_message.msg._visual.Visual", full_classname_dest, 36) == 0);
  }
  my_custom_message__msg__Visual * ros_message = _ros_message;
  {  // yaw_odom
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_odom");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_odom = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_imu
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_imu");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_imu = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_filter
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_filter");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_filter = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_custom_message__msg__visual__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Visual */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_custom_message.msg._visual");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Visual");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_custom_message__msg__Visual * ros_message = (my_custom_message__msg__Visual *)raw_ros_message;
  {  // yaw_odom
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_odom);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_odom", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_imu
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_imu);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_imu", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_filter
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_filter);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_filter", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
