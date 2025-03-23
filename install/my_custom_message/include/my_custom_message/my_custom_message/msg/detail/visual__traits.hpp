// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_custom_message:msg/Visual.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__TRAITS_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_custom_message/msg/detail/visual__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_custom_message
{

namespace msg
{

inline void to_flow_style_yaml(
  const Visual & msg,
  std::ostream & out)
{
  out << "{";
  // member: yaw_odom
  {
    out << "yaw_odom: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_odom, out);
    out << ", ";
  }

  // member: yaw_imu
  {
    out << "yaw_imu: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_imu, out);
    out << ", ";
  }

  // member: yaw_filter
  {
    out << "yaw_filter: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_filter, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Visual & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: yaw_odom
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_odom: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_odom, out);
    out << "\n";
  }

  // member: yaw_imu
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_imu: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_imu, out);
    out << "\n";
  }

  // member: yaw_filter
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_filter: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_filter, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Visual & msg, bool use_flow_style = false)
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
  const my_custom_message::msg::Visual & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_custom_message::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_custom_message::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_custom_message::msg::Visual & msg)
{
  return my_custom_message::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_custom_message::msg::Visual>()
{
  return "my_custom_message::msg::Visual";
}

template<>
inline const char * name<my_custom_message::msg::Visual>()
{
  return "my_custom_message/msg/Visual";
}

template<>
struct has_fixed_size<my_custom_message::msg::Visual>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_custom_message::msg::Visual>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_custom_message::msg::Visual>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__TRAITS_HPP_
