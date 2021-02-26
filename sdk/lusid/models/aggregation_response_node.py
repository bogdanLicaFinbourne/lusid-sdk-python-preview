# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2655
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AggregationResponseNode(object):
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
        'key': 'AggregateSpec',
        'value': 'str',
        'depth': 'int',
        'properties': 'dict(str, object)',
        'children': 'list[AggregationResponseNode]'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'depth': 'depth',
        'properties': 'properties',
        'children': 'children'
    }

    required_map = {
        'key': 'optional',
        'value': 'optional',
        'depth': 'optional',
        'properties': 'optional',
        'children': 'optional'
    }

    def __init__(self, key=None, value=None, depth=None, properties=None, children=None):  # noqa: E501
        """
        AggregationResponseNode - a model defined in OpenAPI

        :param key: 
        :type key: lusid.AggregateSpec
        :param value: 
        :type value: str
        :param depth: 
        :type depth: int
        :param properties: 
        :type properties: dict(str, object)
        :param children: 
        :type children: list[lusid.AggregationResponseNode]

        """  # noqa: E501

        self._key = None
        self._value = None
        self._depth = None
        self._properties = None
        self._children = None
        self.discriminator = None

        if key is not None:
            self.key = key
        self.value = value
        if depth is not None:
            self.depth = depth
        self.properties = properties
        self.children = children

    @property
    def key(self):
        """Gets the key of this AggregationResponseNode.  # noqa: E501


        :return: The key of this AggregationResponseNode.  # noqa: E501
        :rtype: AggregateSpec
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AggregationResponseNode.


        :param key: The key of this AggregationResponseNode.  # noqa: E501
        :type: AggregateSpec
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this AggregationResponseNode.  # noqa: E501


        :return: The value of this AggregationResponseNode.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AggregationResponseNode.


        :param value: The value of this AggregationResponseNode.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def depth(self):
        """Gets the depth of this AggregationResponseNode.  # noqa: E501


        :return: The depth of this AggregationResponseNode.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this AggregationResponseNode.


        :param depth: The depth of this AggregationResponseNode.  # noqa: E501
        :type: int
        """

        self._depth = depth

    @property
    def properties(self):
        """Gets the properties of this AggregationResponseNode.  # noqa: E501


        :return: The properties of this AggregationResponseNode.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AggregationResponseNode.


        :param properties: The properties of this AggregationResponseNode.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def children(self):
        """Gets the children of this AggregationResponseNode.  # noqa: E501


        :return: The children of this AggregationResponseNode.  # noqa: E501
        :rtype: list[AggregationResponseNode]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this AggregationResponseNode.


        :param children: The children of this AggregationResponseNode.  # noqa: E501
        :type: list[AggregationResponseNode]
        """

        self._children = children

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
        if not isinstance(other, AggregationResponseNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
