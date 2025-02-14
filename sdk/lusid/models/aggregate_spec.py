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

class AggregateSpec(object):
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
        'key': 'str',
        'op': 'str'
    }

    attribute_map = {
        'key': 'key',
        'op': 'op'
    }

    required_map = {
        'key': 'required',
        'op': 'required'
    }

    def __init__(self, key=None, op=None):  # noqa: E501
        """
        AggregateSpec - a model defined in OpenAPI

        :param key:  The key that uniquely identifies a queryable address in Lusid. (required)
        :type key: str
        :param op:  The available values are: Sum, Proportion, Average, Count, Min, Max, Value (required)
        :type op: str

        """  # noqa: E501

        self._key = None
        self._op = None
        self.discriminator = None

        self.key = key
        self.op = op

    @property
    def key(self):
        """Gets the key of this AggregateSpec.  # noqa: E501

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :return: The key of this AggregateSpec.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AggregateSpec.

        The key that uniquely identifies a queryable address in Lusid.  # noqa: E501

        :param key: The key of this AggregateSpec.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def op(self):
        """Gets the op of this AggregateSpec.  # noqa: E501

        The available values are: Sum, Proportion, Average, Count, Min, Max, Value  # noqa: E501

        :return: The op of this AggregateSpec.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this AggregateSpec.

        The available values are: Sum, Proportion, Average, Count, Min, Max, Value  # noqa: E501

        :param op: The op of this AggregateSpec.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["Sum", "Proportion", "Average", "Count", "Min", "Max", "Value"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

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
        if not isinstance(other, AggregateSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
