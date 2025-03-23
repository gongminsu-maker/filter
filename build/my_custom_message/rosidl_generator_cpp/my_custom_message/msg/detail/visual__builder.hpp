// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_custom_message:msg/Visual.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__BUILDER_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_custom_message/msg/detail/visual__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_custom_message
{

namespace msg
{

namespace builder
{

class Init_Visual_yaw_filter
{
public:
  explicit Init_Visual_yaw_filter(::my_custom_message::msg::Visual & msg)
  : msg_(msg)
  {}
  ::my_custom_message::msg::Visual yaw_filter(::my_custom_message::msg::Visual::_yaw_filter_type arg)
  {
    msg_.yaw_filter = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_custom_message::msg::Visual msg_;
};

class Init_Visual_yaw_imu
{
public:
  explicit Init_Visual_yaw_imu(::my_custom_message::msg::Visual & msg)
  : msg_(msg)
  {}
  Init_Visual_yaw_filter yaw_imu(::my_custom_message::msg::Visual::_yaw_imu_type arg)
  {
    msg_.yaw_imu = std::move(arg);
    return Init_Visual_yaw_filter(msg_);
  }

private:
  ::my_custom_message::msg::Visual msg_;
};

class Init_Visual_yaw_odom
{
public:
  Init_Visual_yaw_odom()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Visual_yaw_imu yaw_odom(::my_custom_message::msg::Visual::_yaw_odom_type arg)
  {
    msg_.yaw_odom = std::move(arg);
    return Init_Visual_yaw_imu(msg_);
  }

private:
  ::my_custom_message::msg::Visual msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_custom_message::msg::Visual>()
{
  return my_custom_message::msg::builder::Init_Visual_yaw_odom();
}

}  // namespace my_custom_message

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__BUILDER_HPP_
