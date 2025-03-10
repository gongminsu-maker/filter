# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_custom_message:msg/Motor.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Motor(type):
    """Metaclass of message 'Motor'."""

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
                'my_custom_message.msg.Motor')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__motor
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__motor
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__motor
            cls._TYPE_SUPPORT = module.type_support_msg__msg__motor
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__motor

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Motor(metaclass=Metaclass_Motor):
    """Message class 'Motor'."""

    __slots__ = [
        '_left_w',
        '_right_w',
        '_left_target_w',
        '_right_target_w',
        '_linear_vel',
    ]

    _fields_and_field_types = {
        'left_w': 'float',
        'right_w': 'float',
        'left_target_w': 'float',
        'right_target_w': 'float',
        'linear_vel': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.left_w = kwargs.get('left_w', float())
        self.right_w = kwargs.get('right_w', float())
        self.left_target_w = kwargs.get('left_target_w', float())
        self.right_target_w = kwargs.get('right_target_w', float())
        self.linear_vel = kwargs.get('linear_vel', float())

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
        if self.left_w != other.left_w:
            return False
        if self.right_w != other.right_w:
            return False
        if self.left_target_w != other.left_target_w:
            return False
        if self.right_target_w != other.right_target_w:
            return False
        if self.linear_vel != other.linear_vel:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def left_w(self):
        """Message field 'left_w'."""
        return self._left_w

    @left_w.setter
    def left_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_w = value

    @builtins.property
    def right_w(self):
        """Message field 'right_w'."""
        return self._right_w

    @right_w.setter
    def right_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_w = value

    @builtins.property
    def left_target_w(self):
        """Message field 'left_target_w'."""
        return self._left_target_w

    @left_target_w.setter
    def left_target_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'left_target_w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'left_target_w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._left_target_w = value

    @builtins.property
    def right_target_w(self):
        """Message field 'right_target_w'."""
        return self._right_target_w

    @right_target_w.setter
    def right_target_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'right_target_w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'right_target_w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._right_target_w = value

    @builtins.property
    def linear_vel(self):
        """Message field 'linear_vel'."""
        return self._linear_vel

    @linear_vel.setter
    def linear_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear_vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'linear_vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._linear_vel = value
