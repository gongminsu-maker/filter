// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_custom_message:msg/Visual.idl
// generated code does not contain a copyright notice
#include "my_custom_message/msg/detail/visual__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
my_custom_message__msg__Visual__init(my_custom_message__msg__Visual * msg)
{
  if (!msg) {
    return false;
  }
  // yaw_odom
  // yaw_imu
  // yaw_filter
  return true;
}

void
my_custom_message__msg__Visual__fini(my_custom_message__msg__Visual * msg)
{
  if (!msg) {
    return;
  }
  // yaw_odom
  // yaw_imu
  // yaw_filter
}

bool
my_custom_message__msg__Visual__are_equal(const my_custom_message__msg__Visual * lhs, const my_custom_message__msg__Visual * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // yaw_odom
  if (lhs->yaw_odom != rhs->yaw_odom) {
    return false;
  }
  // yaw_imu
  if (lhs->yaw_imu != rhs->yaw_imu) {
    return false;
  }
  // yaw_filter
  if (lhs->yaw_filter != rhs->yaw_filter) {
    return false;
  }
  return true;
}

bool
my_custom_message__msg__Visual__copy(
  const my_custom_message__msg__Visual * input,
  my_custom_message__msg__Visual * output)
{
  if (!input || !output) {
    return false;
  }
  // yaw_odom
  output->yaw_odom = input->yaw_odom;
  // yaw_imu
  output->yaw_imu = input->yaw_imu;
  // yaw_filter
  output->yaw_filter = input->yaw_filter;
  return true;
}

my_custom_message__msg__Visual *
my_custom_message__msg__Visual__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Visual * msg = (my_custom_message__msg__Visual *)allocator.allocate(sizeof(my_custom_message__msg__Visual), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_custom_message__msg__Visual));
  bool success = my_custom_message__msg__Visual__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_custom_message__msg__Visual__destroy(my_custom_message__msg__Visual * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_custom_message__msg__Visual__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_custom_message__msg__Visual__Sequence__init(my_custom_message__msg__Visual__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Visual * data = NULL;

  if (size) {
    data = (my_custom_message__msg__Visual *)allocator.zero_allocate(size, sizeof(my_custom_message__msg__Visual), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_custom_message__msg__Visual__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_custom_message__msg__Visual__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
my_custom_message__msg__Visual__Sequence__fini(my_custom_message__msg__Visual__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      my_custom_message__msg__Visual__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

my_custom_message__msg__Visual__Sequence *
my_custom_message__msg__Visual__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Visual__Sequence * array = (my_custom_message__msg__Visual__Sequence *)allocator.allocate(sizeof(my_custom_message__msg__Visual__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_custom_message__msg__Visual__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_custom_message__msg__Visual__Sequence__destroy(my_custom_message__msg__Visual__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_custom_message__msg__Visual__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_custom_message__msg__Visual__Sequence__are_equal(const my_custom_message__msg__Visual__Sequence * lhs, const my_custom_message__msg__Visual__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_custom_message__msg__Visual__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_custom_message__msg__Visual__Sequence__copy(
  const my_custom_message__msg__Visual__Sequence * input,
  my_custom_message__msg__Visual__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_custom_message__msg__Visual);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    my_custom_message__msg__Visual * data =
      (my_custom_message__msg__Visual *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_custom_message__msg__Visual__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          my_custom_message__msg__Visual__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_custom_message__msg__Visual__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
