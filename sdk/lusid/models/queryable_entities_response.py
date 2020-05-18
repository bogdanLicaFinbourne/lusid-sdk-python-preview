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

class QueryableEntitiesResponse(object):
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
        'address_keys': 'list[str]',
        'descriptions': 'list[str]',
        'definitions': 'list[AggregationResult]'
    }

    attribute_map = {
        'address_keys': 'addressKeys',
        'descriptions': 'descriptions',
        'definitions': 'definitions'
    }

    required_map = {
        'address_keys': 'optional',
        'descriptions': 'optional',
        'definitions': 'optional'
    }

    def __init__(self, address_keys=None, descriptions=None, definitions=None):  # noqa: E501
        """
        QueryableEntitiesResponse - a model defined in OpenAPI

        :param address_keys:  The set of addresses that can be accessed via (an aggregation) query.
        :type address_keys: list[str]
        :param descriptions:  The descriptions for each address key to explain exactly what they are and mean.
        :type descriptions: list[str]
        :param definitions:  The definitions of the the results returned for a given key with information on whether it is scaled with quantity of holdings and what type it is.
        :type definitions: list[lusid.AggregationResult]

        """  # noqa: E501

        self._address_keys = None
        self._descriptions = None
        self._definitions = None
        self.discriminator = None

        if address_keys is not None:
            self.address_keys = address_keys
        if descriptions is not None:
            self.descriptions = descriptions
        if definitions is not None:
            self.definitions = definitions

    @property
    def address_keys(self):
        """Gets the address_keys of this QueryableEntitiesResponse.  # noqa: E501

        The set of addresses that can be accessed via (an aggregation) query.  # noqa: E501

        :return: The address_keys of this QueryableEntitiesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_keys

    @address_keys.setter
    def address_keys(self, address_keys):
        """Sets the address_keys of this QueryableEntitiesResponse.

        The set of addresses that can be accessed via (an aggregation) query.  # noqa: E501

        :param address_keys: The address_keys of this QueryableEntitiesResponse.  # noqa: E501
        :type: list[str]
        """

        self._address_keys = address_keys

    @property
    def descriptions(self):
        """Gets the descriptions of this QueryableEntitiesResponse.  # noqa: E501

        The descriptions for each address key to explain exactly what they are and mean.  # noqa: E501

        :return: The descriptions of this QueryableEntitiesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, descriptions):
        """Sets the descriptions of this QueryableEntitiesResponse.

        The descriptions for each address key to explain exactly what they are and mean.  # noqa: E501

        :param descriptions: The descriptions of this QueryableEntitiesResponse.  # noqa: E501
        :type: list[str]
        """

        self._descriptions = descriptions

    @property
    def definitions(self):
        """Gets the definitions of this QueryableEntitiesResponse.  # noqa: E501

        The definitions of the the results returned for a given key with information on whether it is scaled with quantity of holdings and what type it is.  # noqa: E501

        :return: The definitions of this QueryableEntitiesResponse.  # noqa: E501
        :rtype: list[AggregationResult]
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """Sets the definitions of this QueryableEntitiesResponse.

        The definitions of the the results returned for a given key with information on whether it is scaled with quantity of holdings and what type it is.  # noqa: E501

        :param definitions: The definitions of this QueryableEntitiesResponse.  # noqa: E501
        :type: list[AggregationResult]
        """

        self._definitions = definitions

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
        if not isinstance(other, QueryableEntitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
