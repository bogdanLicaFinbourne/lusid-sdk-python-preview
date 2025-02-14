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

class InstrumentMatch(object):
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
        'mastered_instruments': 'list[InstrumentDefinition]',
        'external_instruments': 'list[InstrumentDefinition]'
    }

    attribute_map = {
        'mastered_instruments': 'masteredInstruments',
        'external_instruments': 'externalInstruments'
    }

    required_map = {
        'mastered_instruments': 'optional',
        'external_instruments': 'optional'
    }

    def __init__(self, mastered_instruments=None, external_instruments=None):  # noqa: E501
        """
        InstrumentMatch - a model defined in OpenAPI

        :param mastered_instruments:  The collection of instruments found by the search which have been mastered within LUSID.
        :type mastered_instruments: list[lusid.InstrumentDefinition]
        :param external_instruments:  The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI.
        :type external_instruments: list[lusid.InstrumentDefinition]

        """  # noqa: E501

        self._mastered_instruments = None
        self._external_instruments = None
        self.discriminator = None

        self.mastered_instruments = mastered_instruments
        self.external_instruments = external_instruments

    @property
    def mastered_instruments(self):
        """Gets the mastered_instruments of this InstrumentMatch.  # noqa: E501

        The collection of instruments found by the search which have been mastered within LUSID.  # noqa: E501

        :return: The mastered_instruments of this InstrumentMatch.  # noqa: E501
        :rtype: list[InstrumentDefinition]
        """
        return self._mastered_instruments

    @mastered_instruments.setter
    def mastered_instruments(self, mastered_instruments):
        """Sets the mastered_instruments of this InstrumentMatch.

        The collection of instruments found by the search which have been mastered within LUSID.  # noqa: E501

        :param mastered_instruments: The mastered_instruments of this InstrumentMatch.  # noqa: E501
        :type: list[InstrumentDefinition]
        """

        self._mastered_instruments = mastered_instruments

    @property
    def external_instruments(self):
        """Gets the external_instruments of this InstrumentMatch.  # noqa: E501

        The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI.  # noqa: E501

        :return: The external_instruments of this InstrumentMatch.  # noqa: E501
        :rtype: list[InstrumentDefinition]
        """
        return self._external_instruments

    @external_instruments.setter
    def external_instruments(self, external_instruments):
        """Sets the external_instruments of this InstrumentMatch.

        The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI.  # noqa: E501

        :param external_instruments: The external_instruments of this InstrumentMatch.  # noqa: E501
        :type: list[InstrumentDefinition]
        """

        self._external_instruments = external_instruments

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
        if not isinstance(other, InstrumentMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
