# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2859
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class LegDefinition(object):
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
        'convention_name': 'FlowConventionName',
        'conventions': 'FlowConventions',
        'index_convention': 'IndexConvention',
        'index_convention_name': 'FlowConventionName',
        'notional_exchange_type': 'str',
        'pay_receive': 'str',
        'rate_or_spread': 'float',
        'reset_convention': 'str',
        'stub_type': 'str'
    }

    attribute_map = {
        'convention_name': 'conventionName',
        'conventions': 'conventions',
        'index_convention': 'indexConvention',
        'index_convention_name': 'indexConventionName',
        'notional_exchange_type': 'notionalExchangeType',
        'pay_receive': 'payReceive',
        'rate_or_spread': 'rateOrSpread',
        'reset_convention': 'resetConvention',
        'stub_type': 'stubType'
    }

    required_map = {
        'convention_name': 'optional',
        'conventions': 'optional',
        'index_convention': 'optional',
        'index_convention_name': 'optional',
        'notional_exchange_type': 'required',
        'pay_receive': 'required',
        'rate_or_spread': 'required',
        'reset_convention': 'optional',
        'stub_type': 'required'
    }

    def __init__(self, convention_name=None, conventions=None, index_convention=None, index_convention_name=None, notional_exchange_type=None, pay_receive=None, rate_or_spread=None, reset_convention=None, stub_type=None):  # noqa: E501
        """
        LegDefinition - a model defined in OpenAPI

        :param convention_name: 
        :type convention_name: lusid.FlowConventionName
        :param conventions: 
        :type conventions: lusid.FlowConventions
        :param index_convention: 
        :type index_convention: lusid.IndexConvention
        :param index_convention_name: 
        :type index_convention_name: lusid.FlowConventionName
        :param notional_exchange_type:  what type of notional exchange does the leg have  Supported string (enumeration) values are: [None, Initial, Final, Both]. (required)
        :type notional_exchange_type: str
        :param pay_receive:  Is the leg to be paid or received  Supported string (enumeration) values are: [NotDefined, Pay, Receive]. (required)
        :type pay_receive: str
        :param rate_or_spread:  Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg. (required)
        :type rate_or_spread: float
        :param reset_convention:  Control how resets are generated relative to swap payment convention(s).  Supported string (enumeration) values are: [InAdvance, InArrears].
        :type reset_convention: str
        :param stub_type:  If a stub is required should it be at the front or back of the leg.  Supported string (enumeration) values are: [Front, Back, Both]. (required)
        :type stub_type: str

        """  # noqa: E501

        self._convention_name = None
        self._conventions = None
        self._index_convention = None
        self._index_convention_name = None
        self._notional_exchange_type = None
        self._pay_receive = None
        self._rate_or_spread = None
        self._reset_convention = None
        self._stub_type = None
        self.discriminator = None

        if convention_name is not None:
            self.convention_name = convention_name
        if conventions is not None:
            self.conventions = conventions
        if index_convention is not None:
            self.index_convention = index_convention
        if index_convention_name is not None:
            self.index_convention_name = index_convention_name
        self.notional_exchange_type = notional_exchange_type
        self.pay_receive = pay_receive
        self.rate_or_spread = rate_or_spread
        self.reset_convention = reset_convention
        self.stub_type = stub_type

    @property
    def convention_name(self):
        """Gets the convention_name of this LegDefinition.  # noqa: E501


        :return: The convention_name of this LegDefinition.  # noqa: E501
        :rtype: FlowConventionName
        """
        return self._convention_name

    @convention_name.setter
    def convention_name(self, convention_name):
        """Sets the convention_name of this LegDefinition.


        :param convention_name: The convention_name of this LegDefinition.  # noqa: E501
        :type: FlowConventionName
        """

        self._convention_name = convention_name

    @property
    def conventions(self):
        """Gets the conventions of this LegDefinition.  # noqa: E501


        :return: The conventions of this LegDefinition.  # noqa: E501
        :rtype: FlowConventions
        """
        return self._conventions

    @conventions.setter
    def conventions(self, conventions):
        """Sets the conventions of this LegDefinition.


        :param conventions: The conventions of this LegDefinition.  # noqa: E501
        :type: FlowConventions
        """

        self._conventions = conventions

    @property
    def index_convention(self):
        """Gets the index_convention of this LegDefinition.  # noqa: E501


        :return: The index_convention of this LegDefinition.  # noqa: E501
        :rtype: IndexConvention
        """
        return self._index_convention

    @index_convention.setter
    def index_convention(self, index_convention):
        """Sets the index_convention of this LegDefinition.


        :param index_convention: The index_convention of this LegDefinition.  # noqa: E501
        :type: IndexConvention
        """

        self._index_convention = index_convention

    @property
    def index_convention_name(self):
        """Gets the index_convention_name of this LegDefinition.  # noqa: E501


        :return: The index_convention_name of this LegDefinition.  # noqa: E501
        :rtype: FlowConventionName
        """
        return self._index_convention_name

    @index_convention_name.setter
    def index_convention_name(self, index_convention_name):
        """Sets the index_convention_name of this LegDefinition.


        :param index_convention_name: The index_convention_name of this LegDefinition.  # noqa: E501
        :type: FlowConventionName
        """

        self._index_convention_name = index_convention_name

    @property
    def notional_exchange_type(self):
        """Gets the notional_exchange_type of this LegDefinition.  # noqa: E501

        what type of notional exchange does the leg have  Supported string (enumeration) values are: [None, Initial, Final, Both].  # noqa: E501

        :return: The notional_exchange_type of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._notional_exchange_type

    @notional_exchange_type.setter
    def notional_exchange_type(self, notional_exchange_type):
        """Sets the notional_exchange_type of this LegDefinition.

        what type of notional exchange does the leg have  Supported string (enumeration) values are: [None, Initial, Final, Both].  # noqa: E501

        :param notional_exchange_type: The notional_exchange_type of this LegDefinition.  # noqa: E501
        :type: str
        """
        if notional_exchange_type is None:
            raise ValueError("Invalid value for `notional_exchange_type`, must not be `None`")  # noqa: E501

        self._notional_exchange_type = notional_exchange_type

    @property
    def pay_receive(self):
        """Gets the pay_receive of this LegDefinition.  # noqa: E501

        Is the leg to be paid or received  Supported string (enumeration) values are: [NotDefined, Pay, Receive].  # noqa: E501

        :return: The pay_receive of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this LegDefinition.

        Is the leg to be paid or received  Supported string (enumeration) values are: [NotDefined, Pay, Receive].  # noqa: E501

        :param pay_receive: The pay_receive of this LegDefinition.  # noqa: E501
        :type: str
        """
        if pay_receive is None:
            raise ValueError("Invalid value for `pay_receive`, must not be `None`")  # noqa: E501

        self._pay_receive = pay_receive

    @property
    def rate_or_spread(self):
        """Gets the rate_or_spread of this LegDefinition.  # noqa: E501

        Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg.  # noqa: E501

        :return: The rate_or_spread of this LegDefinition.  # noqa: E501
        :rtype: float
        """
        return self._rate_or_spread

    @rate_or_spread.setter
    def rate_or_spread(self, rate_or_spread):
        """Sets the rate_or_spread of this LegDefinition.

        Is there either a fixed rate (non-zero) or spread to be paid over the value of the leg.  # noqa: E501

        :param rate_or_spread: The rate_or_spread of this LegDefinition.  # noqa: E501
        :type: float
        """
        if rate_or_spread is None:
            raise ValueError("Invalid value for `rate_or_spread`, must not be `None`")  # noqa: E501

        self._rate_or_spread = rate_or_spread

    @property
    def reset_convention(self):
        """Gets the reset_convention of this LegDefinition.  # noqa: E501

        Control how resets are generated relative to swap payment convention(s).  Supported string (enumeration) values are: [InAdvance, InArrears].  # noqa: E501

        :return: The reset_convention of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._reset_convention

    @reset_convention.setter
    def reset_convention(self, reset_convention):
        """Sets the reset_convention of this LegDefinition.

        Control how resets are generated relative to swap payment convention(s).  Supported string (enumeration) values are: [InAdvance, InArrears].  # noqa: E501

        :param reset_convention: The reset_convention of this LegDefinition.  # noqa: E501
        :type: str
        """

        self._reset_convention = reset_convention

    @property
    def stub_type(self):
        """Gets the stub_type of this LegDefinition.  # noqa: E501

        If a stub is required should it be at the front or back of the leg.  Supported string (enumeration) values are: [Front, Back, Both].  # noqa: E501

        :return: The stub_type of this LegDefinition.  # noqa: E501
        :rtype: str
        """
        return self._stub_type

    @stub_type.setter
    def stub_type(self, stub_type):
        """Sets the stub_type of this LegDefinition.

        If a stub is required should it be at the front or back of the leg.  Supported string (enumeration) values are: [Front, Back, Both].  # noqa: E501

        :param stub_type: The stub_type of this LegDefinition.  # noqa: E501
        :type: str
        """
        if stub_type is None:
            raise ValueError("Invalid value for `stub_type`, must not be `None`")  # noqa: E501

        self._stub_type = stub_type

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
        if not isinstance(other, LegDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
