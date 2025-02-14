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

class PropertyDomain(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NOTDEFINED = "NotDefined"
    TRANSACTION = "Transaction"
    PORTFOLIO = "Portfolio"
    HOLDING = "Holding"
    REFERENCEHOLDING = "ReferenceHolding"
    TRANSACTIONCONFIGURATION = "TransactionConfiguration"
    INSTRUMENT = "Instrument"
    CUTLABELDEFINITION = "CutLabelDefinition"
    ANALYTIC = "Analytic"
    PORTFOLIOGROUP = "PortfolioGroup"
    PERSON = "Person"
    ACCESSMETADATA = "AccessMetadata"
    ORDER = "Order"
    UNITRESULT = "UnitResult"
    MARKETDATA = "MarketData"
    CONFIGURATIONRECIPE = "ConfigurationRecipe"
    ALLOCATION = "Allocation"
    CALENDAR = "Calendar"
    LEGALENTITY = "LegalEntity"

    allowable_values = [NOTDEFINED, TRANSACTION, PORTFOLIO, HOLDING, REFERENCEHOLDING, TRANSACTIONCONFIGURATION, INSTRUMENT, CUTLABELDEFINITION, ANALYTIC, PORTFOLIOGROUP, PERSON, ACCESSMETADATA, ORDER, UNITRESULT, MARKETDATA, CONFIGURATIONRECIPE, ALLOCATION, CALENDAR, LEGALENTITY]  # noqa: E501

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
    }

    attribute_map = {
    }

    required_map = {
    }

    def __init__(self):  # noqa: E501
        """
        PropertyDomain - a model defined in OpenAPI


        """  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, PropertyDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
