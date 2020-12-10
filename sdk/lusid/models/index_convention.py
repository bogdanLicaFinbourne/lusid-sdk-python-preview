# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2380
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class IndexConvention(object):
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
        'fixing_reference': 'str',
        'publication_day_lag': 'int',
        'payment_tenor': 'str',
        'day_count_convention': 'str',
        'currency': 'str',
        'scope': 'str',
        'code': 'str'
    }

    attribute_map = {
        'fixing_reference': 'fixingReference',
        'publication_day_lag': 'publicationDayLag',
        'payment_tenor': 'paymentTenor',
        'day_count_convention': 'dayCountConvention',
        'currency': 'currency',
        'scope': 'scope',
        'code': 'code'
    }

    required_map = {
        'fixing_reference': 'required',
        'publication_day_lag': 'required',
        'payment_tenor': 'required',
        'day_count_convention': 'required',
        'currency': 'required',
        'scope': 'optional',
        'code': 'optional'
    }

    def __init__(self, fixing_reference=None, publication_day_lag=None, payment_tenor=None, day_count_convention=None, currency=None, scope=None, code=None):  # noqa: E501
        """
        IndexConvention - a model defined in OpenAPI

        :param fixing_reference:  The reference rate name for fixings (required)
        :type fixing_reference: str
        :param publication_day_lag:  Number of days between spot and publication of the rate. (required)
        :type publication_day_lag: int
        :param payment_tenor:  The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year. (required)
        :type payment_tenor: str
        :param day_count_convention:  when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year              and difference between them. (required)
        :type day_count_convention: str
        :param currency:  Currency of the index convention. (required)
        :type currency: str
        :param scope:  The scope used when updating or inserting the convention.
        :type scope: str
        :param code:  The code of the convention.
        :type code: str

        """  # noqa: E501

        self._fixing_reference = None
        self._publication_day_lag = None
        self._payment_tenor = None
        self._day_count_convention = None
        self._currency = None
        self._scope = None
        self._code = None
        self.discriminator = None

        self.fixing_reference = fixing_reference
        self.publication_day_lag = publication_day_lag
        self.payment_tenor = payment_tenor
        self.day_count_convention = day_count_convention
        self.currency = currency
        self.scope = scope
        self.code = code

    @property
    def fixing_reference(self):
        """Gets the fixing_reference of this IndexConvention.  # noqa: E501

        The reference rate name for fixings  # noqa: E501

        :return: The fixing_reference of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._fixing_reference

    @fixing_reference.setter
    def fixing_reference(self, fixing_reference):
        """Sets the fixing_reference of this IndexConvention.

        The reference rate name for fixings  # noqa: E501

        :param fixing_reference: The fixing_reference of this IndexConvention.  # noqa: E501
        :type: str
        """
        if fixing_reference is None:
            raise ValueError("Invalid value for `fixing_reference`, must not be `None`")  # noqa: E501

        self._fixing_reference = fixing_reference

    @property
    def publication_day_lag(self):
        """Gets the publication_day_lag of this IndexConvention.  # noqa: E501

        Number of days between spot and publication of the rate.  # noqa: E501

        :return: The publication_day_lag of this IndexConvention.  # noqa: E501
        :rtype: int
        """
        return self._publication_day_lag

    @publication_day_lag.setter
    def publication_day_lag(self, publication_day_lag):
        """Sets the publication_day_lag of this IndexConvention.

        Number of days between spot and publication of the rate.  # noqa: E501

        :param publication_day_lag: The publication_day_lag of this IndexConvention.  # noqa: E501
        :type: int
        """
        if publication_day_lag is None:
            raise ValueError("Invalid value for `publication_day_lag`, must not be `None`")  # noqa: E501

        self._publication_day_lag = publication_day_lag

    @property
    def payment_tenor(self):
        """Gets the payment_tenor of this IndexConvention.  # noqa: E501

        The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.  # noqa: E501

        :return: The payment_tenor of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._payment_tenor

    @payment_tenor.setter
    def payment_tenor(self, payment_tenor):
        """Sets the payment_tenor of this IndexConvention.

        The tenor of the payment. For an OIS index this is always 1 day. For other indices, e.g. LIBOR it will have a variable tenor typically between 1 day and 1 year.  # noqa: E501

        :param payment_tenor: The payment_tenor of this IndexConvention.  # noqa: E501
        :type: str
        """
        if payment_tenor is None:
            raise ValueError("Invalid value for `payment_tenor`, must not be `None`")  # noqa: E501

        self._payment_tenor = payment_tenor

    @property
    def day_count_convention(self):
        """Gets the day_count_convention of this IndexConvention.  # noqa: E501

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year              and difference between them.  # noqa: E501

        :return: The day_count_convention of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._day_count_convention

    @day_count_convention.setter
    def day_count_convention(self, day_count_convention):
        """Sets the day_count_convention of this IndexConvention.

        when calculating the fraction of a year between two dates, what convention is used to represent the number of days in a year              and difference between them.  # noqa: E501

        :param day_count_convention: The day_count_convention of this IndexConvention.  # noqa: E501
        :type: str
        """
        if day_count_convention is None:
            raise ValueError("Invalid value for `day_count_convention`, must not be `None`")  # noqa: E501

        self._day_count_convention = day_count_convention

    @property
    def currency(self):
        """Gets the currency of this IndexConvention.  # noqa: E501

        Currency of the index convention.  # noqa: E501

        :return: The currency of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this IndexConvention.

        Currency of the index convention.  # noqa: E501

        :param currency: The currency of this IndexConvention.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def scope(self):
        """Gets the scope of this IndexConvention.  # noqa: E501

        The scope used when updating or inserting the convention.  # noqa: E501

        :return: The scope of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this IndexConvention.

        The scope used when updating or inserting the convention.  # noqa: E501

        :param scope: The scope of this IndexConvention.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this IndexConvention.  # noqa: E501

        The code of the convention.  # noqa: E501

        :return: The code of this IndexConvention.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this IndexConvention.

        The code of the convention.  # noqa: E501

        :param code: The code of this IndexConvention.  # noqa: E501
        :type: str
        """

        self._code = code

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
        if not isinstance(other, IndexConvention):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
