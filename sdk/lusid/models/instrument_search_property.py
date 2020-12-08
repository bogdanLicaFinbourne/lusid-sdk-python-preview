# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2363
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class InstrumentSearchProperty(object):
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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    required_map = {
        'key': 'required',
        'value': 'required'
    }

    def __init__(self, key=None, value=None):  # noqa: E501
        """
        InstrumentSearchProperty - a model defined in OpenAPI

        :param key:  The property key of instrument property to search for. This will be from the 'Instrument' domain and will take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Isin' or 'Instrument/MyScope/AssetClass'. (required)
        :type key: str
        :param value:  The value of the property e.g. 'US0378331005' or 'Equity'. (required)
        :type value: str

        """  # noqa: E501

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        """Gets the key of this InstrumentSearchProperty.  # noqa: E501

        The property key of instrument property to search for. This will be from the 'Instrument' domain and will take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Isin' or 'Instrument/MyScope/AssetClass'.  # noqa: E501

        :return: The key of this InstrumentSearchProperty.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InstrumentSearchProperty.

        The property key of instrument property to search for. This will be from the 'Instrument' domain and will take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Isin' or 'Instrument/MyScope/AssetClass'.  # noqa: E501

        :param key: The key of this InstrumentSearchProperty.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this InstrumentSearchProperty.  # noqa: E501

        The value of the property e.g. 'US0378331005' or 'Equity'.  # noqa: E501

        :return: The value of this InstrumentSearchProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InstrumentSearchProperty.

        The value of the property e.g. 'US0378331005' or 'Equity'.  # noqa: E501

        :param value: The value of this InstrumentSearchProperty.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, InstrumentSearchProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
