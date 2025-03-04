// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_custom_message:msg/Motor.idl
// generated code does not contain a copyright notice
#include "my_custom_message/msg/detail/motor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
my_custom_message__msg__Motor__init(my_custom_message__msg__Motor * msg)
{
  if (!msg) {
    return false;
  }
  // left_w
  // right_w
  // linear_vel
  return true;
}

void
my_custom_message__msg__Motor__fini(my_custom_message__msg__Motor * msg)
{
  if (!msg) {
    return;
  }
  // left_w
  // right_w
  // linear_vel
}

bool
my_custom_message__msg__Motor__are_equal(const my_custom_message__msg__Motor * lhs, const my_custom_message__msg__Motor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // left_w
  if (lhs->left_w != rhs->left_w) {
    return false;
  }
  // right_w
  if (lhs->right_w != rhs->right_w) {
    return false;
  }
  // linear_vel
  if (lhs->linear_vel != rhs->linear_vel) {
    return false;
  }
  return true;
}

bool
my_custom_message__msg__Motor__copy(
  const my_custom_message__msg__Motor * input,
  my_custom_message__msg__Motor * output)
{
  if (!input || !output) {
    return false;
  }
  // left_w
  output->left_w = input->left_w;
  // right_w
  output->right_w = input->right_w;
  // linear_vel
  output->linear_vel = input->linear_vel;
  return true;
}

my_custom_message__msg__Motor *
my_custom_message__msg__Motor__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Motor * msg = (my_custom_message__msg__Motor *)allocator.allocate(sizeof(my_custom_message__msg__Motor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_custom_message__msg__Motor));
  bool success = my_custom_message__msg__Motor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_custom_message__msg__Motor__destroy(my_custom_message__msg__Motor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_custom_message__msg__Motor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_custom_message__msg__Motor__Sequence__init(my_custom_message__msg__Motor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Motor * data = NULL;

  if (size) {
    data = (my_custom_message__msg__Motor *)allocator.zero_allocate(size, sizeof(my_custom_message__msg__Motor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_custom_message__msg__Motor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_custom_message__msg__Motor__fini(&data[i - 1]);
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
my_custom_message__msg__Motor__Sequence__fini(my_custom_message__msg__Motor__Sequence * array)
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
      my_custom_message__msg__Motor__fini(&array->data[i]);
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

my_custom_message__msg__Motor__Sequence *
my_custom_message__msg__Motor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_custom_message__msg__Motor__Sequence * array = (my_custom_message__msg__Motor__Sequence *)allocator.allocate(sizeof(my_custom_message__msg__Motor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_custom_message__msg__Motor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_custom_message__msg__Motor__Sequence__destroy(my_custom_message__msg__Motor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_custom_message__msg__Motor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_custom_message__msg__Motor__Sequence__are_equal(const my_custom_message__msg__Motor__Sequence * lhs, const my_custom_message__msg__Motor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_custom_message__msg__Motor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_custom_message__msg__Motor__Sequence__copy(
  const my_custom_message__msg__Motor__Sequence * input,
  my_custom_message__msg__Motor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_custom_message__msg__Motor);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    my_custom_message__msg__Motor * data =
      (my_custom_message__msg__Motor *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_custom_message__msg__Motor__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          my_custom_message__msg__Motor__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_custom_message__msg__Motor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
