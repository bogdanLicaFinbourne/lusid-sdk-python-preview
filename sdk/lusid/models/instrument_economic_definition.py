# coding: utf-8

"""
    LUSID API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.10.1383
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InstrumentEconomicDefinition(object):
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
        'instrument_format': 'str',
        'content': 'str'
    }

    attribute_map = {
        'instrument_format': 'instrumentFormat',
        'content': 'content'
    }

    required_map = {
        'instrument_format': 'required',
        'content': 'required'
    }

    def __init__(self, instrument_format=None, content=None):  # noqa: E501
        """
        InstrumentEconomicDefinition - a model defined in OpenAPI

        :param instrument_format:  The format of the expanded definition. (required)
        :type instrument_format: str
        :param content:  The content of the expanded definition. There is no validation on the format of this. (required)
        :type content: str

        """  # noqa: E501

        self._instrument_format = None
        self._content = None
        self.discriminator = None

        self.instrument_format = instrument_format
        self.content = content

    @property
    def instrument_format(self):
        """Gets the instrument_format of this InstrumentEconomicDefinition.  # noqa: E501

        The format of the expanded definition.  # noqa: E501

        :return: The instrument_format of this InstrumentEconomicDefinition.  # noqa: E501
        :rtype: str
        """
        return self._instrument_format

    @instrument_format.setter
    def instrument_format(self, instrument_format):
        """Sets the instrument_format of this InstrumentEconomicDefinition.

        The format of the expanded definition.  # noqa: E501

        :param instrument_format: The instrument_format of this InstrumentEconomicDefinition.  # noqa: E501
        :type: str
        """
        if instrument_format is None:
            raise ValueError("Invalid value for `instrument_format`, must not be `None`")  # noqa: E501

        self._instrument_format = instrument_format

    @property
    def content(self):
        """Gets the content of this InstrumentEconomicDefinition.  # noqa: E501

        The content of the expanded definition. There is no validation on the format of this.  # noqa: E501

        :return: The content of this InstrumentEconomicDefinition.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InstrumentEconomicDefinition.

        The content of the expanded definition. There is no validation on the format of this.  # noqa: E501

        :param content: The content of this InstrumentEconomicDefinition.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, InstrumentEconomicDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
