// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_custom_message:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_custom_message__msg__Motor __attribute__((deprecated))
#else
# define DEPRECATED__my_custom_message__msg__Motor __declspec(deprecated)
#endif

namespace my_custom_message
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Motor_
{
  using Type = Motor_<ContainerAllocator>;

  explicit Motor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_w = 0.0f;
      this->right_w = 0.0f;
      this->linear_vel = 0.0f;
    }
  }

  explicit Motor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_w = 0.0f;
      this->right_w = 0.0f;
      this->linear_vel = 0.0f;
    }
  }

  // field types and members
  using _left_w_type =
    float;
  _left_w_type left_w;
  using _right_w_type =
    float;
  _right_w_type right_w;
  using _linear_vel_type =
    float;
  _linear_vel_type linear_vel;

  // setters for named parameter idiom
  Type & set__left_w(
    const float & _arg)
  {
    this->left_w = _arg;
    return *this;
  }
  Type & set__right_w(
    const float & _arg)
  {
    this->right_w = _arg;
    return *this;
  }
  Type & set__linear_vel(
    const float & _arg)
  {
    this->linear_vel = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_custom_message::msg::Motor_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_custom_message::msg::Motor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_custom_message::msg::Motor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_custom_message::msg::Motor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_custom_message::msg::Motor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_custom_message::msg::Motor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_custom_message::msg::Motor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_custom_message::msg::Motor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_custom_message::msg::Motor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_custom_message::msg::Motor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_custom_message__msg__Motor
    std::shared_ptr<my_custom_message::msg::Motor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_custom_message__msg__Motor
    std::shared_ptr<my_custom_message::msg::Motor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Motor_ & other) const
  {
    if (this->left_w != other.left_w) {
      return false;
    }
    if (this->right_w != other.right_w) {
      return false;
    }
    if (this->linear_vel != other.linear_vel) {
      return false;
    }
    return true;
  }
  bool operator!=(const Motor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Motor_

// alias to use template instance with default allocator
using Motor =
  my_custom_message::msg::Motor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_custom_message

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__MOTOR__STRUCT_HPP_
