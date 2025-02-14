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

class CorporateActionTransitionComponent(object):
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
        'instrument_identifiers': 'dict(str, str)',
        'instrument_uid': 'str',
        'units_factor': 'float',
        'cost_factor': 'float'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_uid': 'instrumentUid',
        'units_factor': 'unitsFactor',
        'cost_factor': 'costFactor'
    }

    required_map = {
        'instrument_identifiers': 'required',
        'instrument_uid': 'required',
        'units_factor': 'required',
        'cost_factor': 'required'
    }

    def __init__(self, instrument_identifiers=None, instrument_uid=None, units_factor=None, cost_factor=None):  # noqa: E501
        """
        CorporateActionTransitionComponent - a model defined in OpenAPI

        :param instrument_identifiers:  Unique instrument identifiers (required)
        :type instrument_identifiers: dict(str, str)
        :param instrument_uid:  LUSID's internal unique instrument identifier, resolved from the instrument identifiers (required)
        :type instrument_uid: str
        :param units_factor:  (required)
        :type units_factor: float
        :param cost_factor:  (required)
        :type cost_factor: float

        """  # noqa: E501

        self._instrument_identifiers = None
        self._instrument_uid = None
        self._units_factor = None
        self._cost_factor = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.instrument_uid = instrument_uid
        self.units_factor = units_factor
        self.cost_factor = cost_factor

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this CorporateActionTransitionComponent.  # noqa: E501

        Unique instrument identifiers  # noqa: E501

        :return: The instrument_identifiers of this CorporateActionTransitionComponent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this CorporateActionTransitionComponent.

        Unique instrument identifiers  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this CorporateActionTransitionComponent.  # noqa: E501
        :type: dict(str, str)
        """
        if instrument_identifiers is None:
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this CorporateActionTransitionComponent.  # noqa: E501

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :return: The instrument_uid of this CorporateActionTransitionComponent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this CorporateActionTransitionComponent.

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :param instrument_uid: The instrument_uid of this CorporateActionTransitionComponent.  # noqa: E501
        :type: str
        """
        if instrument_uid is None:
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def units_factor(self):
        """Gets the units_factor of this CorporateActionTransitionComponent.  # noqa: E501


        :return: The units_factor of this CorporateActionTransitionComponent.  # noqa: E501
        :rtype: float
        """
        return self._units_factor

    @units_factor.setter
    def units_factor(self, units_factor):
        """Sets the units_factor of this CorporateActionTransitionComponent.


        :param units_factor: The units_factor of this CorporateActionTransitionComponent.  # noqa: E501
        :type: float
        """
        if units_factor is None:
            raise ValueError("Invalid value for `units_factor`, must not be `None`")  # noqa: E501

        self._units_factor = units_factor

    @property
    def cost_factor(self):
        """Gets the cost_factor of this CorporateActionTransitionComponent.  # noqa: E501


        :return: The cost_factor of this CorporateActionTransitionComponent.  # noqa: E501
        :rtype: float
        """
        return self._cost_factor

    @cost_factor.setter
    def cost_factor(self, cost_factor):
        """Sets the cost_factor of this CorporateActionTransitionComponent.


        :param cost_factor: The cost_factor of this CorporateActionTransitionComponent.  # noqa: E501
        :type: float
        """
        if cost_factor is None:
            raise ValueError("Invalid value for `cost_factor`, must not be `None`")  # noqa: E501

        self._cost_factor = cost_factor

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
        if not isinstance(other, CorporateActionTransitionComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
