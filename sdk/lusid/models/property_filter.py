# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2863
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PropertyFilter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'left': 'str',
        'operator': 'str',
        'right': 'object',
        'right_operand_type': 'str'
    }

    attribute_map = {
        'left': 'left',
        'operator': 'operator',
        'right': 'right',
        'right_operand_type': 'rightOperandType'
    }

    required_map = {
        'left': 'optional',
        'operator': 'optional',
        'right': 'optional',
        'right_operand_type': 'optional'
    }

    def __init__(self, left=None, operator=None, right=None, right_operand_type=None):  # noqa: E501
        """
        PropertyFilter - a model defined in OpenAPI

        :param left:  The key that uniquely identifies a queryable address in Lusid.
        :type left: str
        :param operator:  The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In
        :type operator: str
        :param right: 
        :type right: object
        :param right_operand_type:  The available values are: Absolute, Property
        :type right_operand_type: str

        """  # noqa: E501

        self._left = None
        self._operator = None
        self._right = None
        self._right_operand_type = None
        self.discriminator = None

        self.left = left
        if operator is not None:
            self.operator = operator
        self.right = right
        if right_operand_type is not None:
            self.right_operand_type = right_operand_type

    @property
    def left(self):
        """Gets the left of this PropertyFilter.  # noqa: E501

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :return: The left of this PropertyFilter.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this PropertyFilter.

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :param left: The left of this PropertyFilter.  # noqa: E501
        :type: str
        """

        self._left = left

    @property
    def operator(self):
        """Gets the operator of this PropertyFilter.  # noqa: E501

        The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In  # noqa: E501

        :return: The operator of this PropertyFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PropertyFilter.

        The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In  # noqa: E501

        :param operator: The operator of this PropertyFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["Equals", "NotEquals", "GreaterThan", "GreaterThanOrEqualTo", "LessThan", "LessThanOrEqualTo", "In"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def right(self):
        """Gets the right of this PropertyFilter.  # noqa: E501


        :return: The right of this PropertyFilter.  # noqa: E501
        :rtype: object
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this PropertyFilter.


        :param right: The right of this PropertyFilter.  # noqa: E501
        :type: object
        """

        self._right = right

    @property
    def right_operand_type(self):
        """Gets the right_operand_type of this PropertyFilter.  # noqa: E501

        The available values are: Absolute, Property  # noqa: E501

        :return: The right_operand_type of this PropertyFilter.  # noqa: E501
        :rtype: str
        """
        return self._right_operand_type

    @right_operand_type.setter
    def right_operand_type(self, right_operand_type):
        """Sets the right_operand_type of this PropertyFilter.

        The available values are: Absolute, Property  # noqa: E501

        :param right_operand_type: The right_operand_type of this PropertyFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["Absolute", "Property"]  # noqa: E501
        if right_operand_type not in allowed_values:
            raise ValueError(
                "Invalid value for `right_operand_type` ({0}), must be one of {1}"  # noqa: E501
                .format(right_operand_type, allowed_values)
            )

        self._right_operand_type = right_operand_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertyFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
