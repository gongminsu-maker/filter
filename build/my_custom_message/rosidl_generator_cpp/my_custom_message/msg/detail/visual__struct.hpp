// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_custom_message:msg/Visual.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__STRUCT_HPP_
#define MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_custom_message__msg__Visual __attribute__((deprecated))
#else
# define DEPRECATED__my_custom_message__msg__Visual __declspec(deprecated)
#endif

namespace my_custom_message
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Visual_
{
  using Type = Visual_<ContainerAllocator>;

  explicit Visual_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->yaw_odom = 0.0f;
      this->yaw_imu = 0.0f;
      this->yaw_filter = 0.0f;
    }
  }

  explicit Visual_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->yaw_odom = 0.0f;
      this->yaw_imu = 0.0f;
      this->yaw_filter = 0.0f;
    }
  }

  // field types and members
  using _yaw_odom_type =
    float;
  _yaw_odom_type yaw_odom;
  using _yaw_imu_type =
    float;
  _yaw_imu_type yaw_imu;
  using _yaw_filter_type =
    float;
  _yaw_filter_type yaw_filter;

  // setters for named parameter idiom
  Type & set__yaw_odom(
    const float & _arg)
  {
    this->yaw_odom = _arg;
    return *this;
  }
  Type & set__yaw_imu(
    const float & _arg)
  {
    this->yaw_imu = _arg;
    return *this;
  }
  Type & set__yaw_filter(
    const float & _arg)
  {
    this->yaw_filter = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_custom_message::msg::Visual_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_custom_message::msg::Visual_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_custom_message::msg::Visual_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_custom_message::msg::Visual_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_custom_message::msg::Visual_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_custom_message::msg::Visual_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_custom_message::msg::Visual_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_custom_message::msg::Visual_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_custom_message::msg::Visual_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_custom_message::msg::Visual_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_custom_message__msg__Visual
    std::shared_ptr<my_custom_message::msg::Visual_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_custom_message__msg__Visual
    std::shared_ptr<my_custom_message::msg::Visual_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Visual_ & other) const
  {
    if (this->yaw_odom != other.yaw_odom) {
      return false;
    }
    if (this->yaw_imu != other.yaw_imu) {
      return false;
    }
    if (this->yaw_filter != other.yaw_filter) {
      return false;
    }
    return true;
  }
  bool operator!=(const Visual_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Visual_

// alias to use template instance with default allocator
using Visual =
  my_custom_message::msg::Visual_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_custom_message

#endif  // MY_CUSTOM_MESSAGE__MSG__DETAIL__VISUAL__STRUCT_HPP_
