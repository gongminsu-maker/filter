// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_custom_message:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__BUILDER_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_custom_message/msg/detail/motor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_custom_message
{

namespace msg
{

namespace builder
{

class Init_Motor_linear_vel
{
public:
  explicit Init_Motor_linear_vel(::my_custom_message::msg::Motor & msg)
  : msg_(msg)
  {}
  ::my_custom_message::msg::Motor linear_vel(::my_custom_message::msg::Motor::_linear_vel_type arg)
  {
    msg_.linear_vel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_custom_message::msg::Motor msg_;
};

class Init_Motor_right_w
{
public:
  explicit Init_Motor_right_w(::my_custom_message::msg::Motor & msg)
  : msg_(msg)
  {}
  Init_Motor_linear_vel right_w(::my_custom_message::msg::Motor::_right_w_type arg)
  {
    msg_.right_w = std::move(arg);
    return Init_Motor_linear_vel(msg_);
  }

private:
  ::my_custom_message::msg::Motor msg_;
};

class Init_Motor_left_w
{
public:
  Init_Motor_left_w()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Motor_right_w left_w(::my_custom_message::msg::Motor::_left_w_type arg)
  {
    msg_.left_w = std::move(arg);
    return Init_Motor_right_w(msg_);
  }

private:
  ::my_custom_message::msg::Motor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_custom_message::msg::Motor>()
{
  return my_custom_message::msg::builder::Init_Motor_left_w();
}

}  // namespace my_custom_message

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__BUILDER_HPP_
