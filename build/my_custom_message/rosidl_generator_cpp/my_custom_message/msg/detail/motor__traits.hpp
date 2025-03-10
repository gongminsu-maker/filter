// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_custom_message:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__TRAITS_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_custom_message/msg/detail/motor__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_custom_message
{

namespace msg
{

inline void to_flow_style_yaml(
  const Motor & msg,
  std::ostream & out)
{
  out << "{";
  // member: left_w
  {
    out << "left_w: ";
    rosidl_generator_traits::value_to_yaml(msg.left_w, out);
    out << ", ";
  }

  // member: right_w
  {
    out << "right_w: ";
    rosidl_generator_traits::value_to_yaml(msg.right_w, out);
    out << ", ";
  }

  // member: left_target_w
  {
    out << "left_target_w: ";
    rosidl_generator_traits::value_to_yaml(msg.left_target_w, out);
    out << ", ";
  }

  // member: right_target_w
  {
    out << "right_target_w: ";
    rosidl_generator_traits::value_to_yaml(msg.right_target_w, out);
    out << ", ";
  }

  // member: linear_vel
  {
    out << "linear_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_vel, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Motor & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: left_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_w: ";
    rosidl_generator_traits::value_to_yaml(msg.left_w, out);
    out << "\n";
  }

  // member: right_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_w: ";
    rosidl_generator_traits::value_to_yaml(msg.right_w, out);
    out << "\n";
  }

  // member: left_target_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_target_w: ";
    rosidl_generator_traits::value_to_yaml(msg.left_target_w, out);
    out << "\n";
  }

  // member: right_target_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_target_w: ";
    rosidl_generator_traits::value_to_yaml(msg.right_target_w, out);
    out << "\n";
  }

  // member: linear_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_vel, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Motor & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_custom_message

namespace rosidl_generator_traits
{

[[deprecated("use my_custom_message::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_custom_message::msg::Motor & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_custom_message::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_custom_message::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_custom_message::msg::Motor & msg)
{
  return my_custom_message::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_custom_message::msg::Motor>()
{
  return "my_custom_message::msg::Motor";
}

template<>
inline const char * name<my_custom_message::msg::Motor>()
{
  return "my_custom_message/msg/Motor";
}

template<>
struct has_fixed_size<my_custom_message::msg::Motor>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_custom_message::msg::Motor>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_custom_message::msg::Motor>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__TRAITS_HPP_
