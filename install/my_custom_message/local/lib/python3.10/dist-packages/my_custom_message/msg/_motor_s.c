// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from my_custom_message:msg/Motor.idl
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
#include "my_custom_message/msg/detail/motor__struct.h"
#include "my_custom_message/msg/detail/motor__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_custom_message__msg__motor__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[35];
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
    assert(strncmp("my_custom_message.msg._motor.Motor", full_classname_dest, 34) == 0);
  }
  my_custom_message__msg__Motor * ros_message = _ros_message;
  {  // left_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // left_target_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_target_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->left_target_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // right_target_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_target_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->right_target_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // linear_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "linear_vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->linear_vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_custom_message__msg__motor__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Motor */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_custom_message.msg._motor");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Motor");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_custom_message__msg__Motor * ros_message = (my_custom_message__msg__Motor *)raw_ros_message;
  {  // left_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // left_target_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->left_target_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_target_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_target_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->right_target_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_target_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // linear_vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->linear_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "linear_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
