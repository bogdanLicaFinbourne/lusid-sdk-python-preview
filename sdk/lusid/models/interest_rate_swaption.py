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

class InterestRateSwaption(object):
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
        'start_date': 'datetime',
        'pay_or_receive_fixed': 'str',
        'delivery_method': 'str',
        'swap': 'InterestRateSwap',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'pay_or_receive_fixed': 'payOrReceiveFixed',
        'delivery_method': 'deliveryMethod',
        'swap': 'swap',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'pay_or_receive_fixed': 'required',
        'delivery_method': 'required',
        'swap': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, pay_or_receive_fixed=None, delivery_method=None, swap=None, instrument_type=None):  # noqa: E501
        """
        InterestRateSwaption - a model defined in OpenAPI

        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param pay_or_receive_fixed:  The available values are: NotDefined, Pay, Receive (required)
        :type pay_or_receive_fixed: str
        :param delivery_method:  The available values are: Cash, Physical (required)
        :type delivery_method: str
        :param swap:  (required)
        :type swap: lusid.InterestRateSwap
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket (required)
        :type instrument_type: str

        """  # noqa: E501

        self._start_date = None
        self._pay_or_receive_fixed = None
        self._delivery_method = None
        self._swap = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.pay_or_receive_fixed = pay_or_receive_fixed
        self.delivery_method = delivery_method
        self.swap = swap
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this InterestRateSwaption.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this InterestRateSwaption.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InterestRateSwaption.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this InterestRateSwaption.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def pay_or_receive_fixed(self):
        """Gets the pay_or_receive_fixed of this InterestRateSwaption.  # noqa: E501

        The available values are: NotDefined, Pay, Receive  # noqa: E501

        :return: The pay_or_receive_fixed of this InterestRateSwaption.  # noqa: E501
        :rtype: str
        """
        return self._pay_or_receive_fixed

    @pay_or_receive_fixed.setter
    def pay_or_receive_fixed(self, pay_or_receive_fixed):
        """Sets the pay_or_receive_fixed of this InterestRateSwaption.

        The available values are: NotDefined, Pay, Receive  # noqa: E501

        :param pay_or_receive_fixed: The pay_or_receive_fixed of this InterestRateSwaption.  # noqa: E501
        :type: str
        """
        if pay_or_receive_fixed is None:
            raise ValueError("Invalid value for `pay_or_receive_fixed`, must not be `None`")  # noqa: E501
        allowed_values = ["NotDefined", "Pay", "Receive"]  # noqa: E501
        if pay_or_receive_fixed not in allowed_values:
            raise ValueError(
                "Invalid value for `pay_or_receive_fixed` ({0}), must be one of {1}"  # noqa: E501
                .format(pay_or_receive_fixed, allowed_values)
            )

        self._pay_or_receive_fixed = pay_or_receive_fixed

    @property
    def delivery_method(self):
        """Gets the delivery_method of this InterestRateSwaption.  # noqa: E501

        The available values are: Cash, Physical  # noqa: E501

        :return: The delivery_method of this InterestRateSwaption.  # noqa: E501
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this InterestRateSwaption.

        The available values are: Cash, Physical  # noqa: E501

        :param delivery_method: The delivery_method of this InterestRateSwaption.  # noqa: E501
        :type: str
        """
        if delivery_method is None:
            raise ValueError("Invalid value for `delivery_method`, must not be `None`")  # noqa: E501
        allowed_values = ["Cash", "Physical"]  # noqa: E501
        if delivery_method not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_method` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_method, allowed_values)
            )

        self._delivery_method = delivery_method

    @property
    def swap(self):
        """Gets the swap of this InterestRateSwaption.  # noqa: E501


        :return: The swap of this InterestRateSwaption.  # noqa: E501
        :rtype: InterestRateSwap
        """
        return self._swap

    @swap.setter
    def swap(self, swap):
        """Sets the swap of this InterestRateSwaption.


        :param swap: The swap of this InterestRateSwaption.  # noqa: E501
        :type: InterestRateSwap
        """
        if swap is None:
            raise ValueError("Invalid value for `swap`, must not be `None`")  # noqa: E501

        self._swap = swap

    @property
    def instrument_type(self):
        """Gets the instrument_type of this InterestRateSwaption.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket  # noqa: E501

        :return: The instrument_type of this InterestRateSwaption.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this InterestRateSwaption.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CashSettled, CdsIndex, Basket  # noqa: E501

        :param instrument_type: The instrument_type of this InterestRateSwaption.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashflowLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CashSettled", "CdsIndex", "Basket"]  # noqa: E501
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, InterestRateSwaption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
