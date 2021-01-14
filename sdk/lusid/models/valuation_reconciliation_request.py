# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2475
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ValuationReconciliationRequest(object):
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
        'portfolio_id': 'ResourceId',
        'aggregation': 'AggregationRequest'
    }

    attribute_map = {
        'portfolio_id': 'portfolioId',
        'aggregation': 'aggregation'
    }

    required_map = {
        'portfolio_id': 'required',
        'aggregation': 'required'
    }

    def __init__(self, portfolio_id=None, aggregation=None):  # noqa: E501
        """
        ValuationReconciliationRequest - a model defined in OpenAPI

        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param aggregation:  (required)
        :type aggregation: lusid.AggregationRequest

        """  # noqa: E501

        self._portfolio_id = None
        self._aggregation = None
        self.discriminator = None

        self.portfolio_id = portfolio_id
        self.aggregation = aggregation

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this ValuationReconciliationRequest.  # noqa: E501


        :return: The portfolio_id of this ValuationReconciliationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this ValuationReconciliationRequest.


        :param portfolio_id: The portfolio_id of this ValuationReconciliationRequest.  # noqa: E501
        :type: ResourceId
        """
        if portfolio_id is None:
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def aggregation(self):
        """Gets the aggregation of this ValuationReconciliationRequest.  # noqa: E501


        :return: The aggregation of this ValuationReconciliationRequest.  # noqa: E501
        :rtype: AggregationRequest
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this ValuationReconciliationRequest.


        :param aggregation: The aggregation of this ValuationReconciliationRequest.  # noqa: E501
        :type: AggregationRequest
        """
        if aggregation is None:
            raise ValueError("Invalid value for `aggregation`, must not be `None`")  # noqa: E501

        self._aggregation = aggregation

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
        if not isinstance(other, ValuationReconciliationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
