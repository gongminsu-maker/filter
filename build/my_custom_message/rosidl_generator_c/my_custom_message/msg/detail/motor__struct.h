// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_custom_message:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_H_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Motor in the package my_custom_message.
typedef struct my_custom_message__msg__Motor
{
  float left_w;
  float right_w;
  float linear_vel;
} my_custom_message__msg__Motor;

// Struct for a sequence of my_custom_message__msg__Motor.
typedef struct my_custom_message__msg__Motor__Sequence
{
  my_custom_message__msg__Motor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_custom_message__msg__Motor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_H_
