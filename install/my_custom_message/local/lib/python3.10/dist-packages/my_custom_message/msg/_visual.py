# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_custom_message:msg/Visual.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Visual(type):
    """Metaclass of message 'Visual'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_custom_message')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_custom_message.msg.Visual')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__visual
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__visual
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__visual
            cls._TYPE_SUPPORT = module.type_support_msg__msg__visual
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__visual

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Visual(metaclass=Metaclass_Visual):
    """Message class 'Visual'."""

    __slots__ = [
        '_yaw_odom',
        '_yaw_imu',
        '_yaw_filter',
    ]

    _fields_and_field_types = {
        'yaw_odom': 'float',
        'yaw_imu': 'float',
        'yaw_filter': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.yaw_odom = kwargs.get('yaw_odom', float())
        self.yaw_imu = kwargs.get('yaw_imu', float())
        self.yaw_filter = kwargs.get('yaw_filter', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.yaw_odom != other.yaw_odom:
            return False
        if self.yaw_imu != other.yaw_imu:
            return False
        if self.yaw_filter != other.yaw_filter:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def yaw_odom(self):
        """Message field 'yaw_odom'."""
        return self._yaw_odom

    @yaw_odom.setter
    def yaw_odom(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_odom' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_odom' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_odom = value

    @builtins.property
    def yaw_imu(self):
        """Message field 'yaw_imu'."""
        return self._yaw_imu

    @yaw_imu.setter
    def yaw_imu(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_imu' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_imu' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_imu = value

    @builtins.property
    def yaw_filter(self):
        """Message field 'yaw_filter'."""
        return self._yaw_filter

    @yaw_filter.setter
    def yaw_filter(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_filter' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_filter' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_filter = value
