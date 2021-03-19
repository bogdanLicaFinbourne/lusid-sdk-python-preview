# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2777
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Portfolio(object):
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
        'href': 'str',
        'id': 'ResourceId',
        'type': 'str',
        'display_name': 'str',
        'description': 'str',
        'created': 'datetime',
        'parent_portfolio_id': 'ResourceId',
        'version': 'Version',
        'is_derived': 'bool',
        'base_currency': 'str',
        'properties': 'dict(str, ModelProperty)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'type': 'type',
        'display_name': 'displayName',
        'description': 'description',
        'created': 'created',
        'parent_portfolio_id': 'parentPortfolioId',
        'version': 'version',
        'is_derived': 'isDerived',
        'base_currency': 'baseCurrency',
        'properties': 'properties',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'type': 'required',
        'display_name': 'required',
        'description': 'optional',
        'created': 'required',
        'parent_portfolio_id': 'optional',
        'version': 'optional',
        'is_derived': 'optional',
        'base_currency': 'optional',
        'properties': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, type=None, display_name=None, description=None, created=None, parent_portfolio_id=None, version=None, is_derived=None, base_currency=None, properties=None, links=None):  # noqa: E501
        """
        Portfolio - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param type:  The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction (required)
        :type type: str
        :param display_name:  The name of the portfolio. (required)
        :type display_name: str
        :param description:  The long form description of the portfolio.
        :type description: str
        :param created:  The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. (required)
        :type created: datetime
        :param parent_portfolio_id: 
        :type parent_portfolio_id: lusid.ResourceId
        :param version: 
        :type version: lusid.Version
        :param is_derived:  Whether or not this is a derived portfolio.
        :type is_derived: bool
        :param base_currency:  The base currency of the portfolio. This will be an empty string for reference portfolios.
        :type base_currency: str
        :param properties:  The requested portfolio properties. These will be from the 'Portfolio' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._id = None
        self._type = None
        self._display_name = None
        self._description = None
        self._created = None
        self._parent_portfolio_id = None
        self._version = None
        self._is_derived = None
        self._base_currency = None
        self._properties = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.type = type
        self.display_name = display_name
        self.description = description
        self.created = created
        if parent_portfolio_id is not None:
            self.parent_portfolio_id = parent_portfolio_id
        if version is not None:
            self.version = version
        if is_derived is not None:
            self.is_derived = is_derived
        self.base_currency = base_currency
        self.properties = properties
        self.links = links

    @property
    def href(self):
        """Gets the href of this Portfolio.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Portfolio.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Portfolio.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Portfolio.  # noqa: E501


        :return: The id of this Portfolio.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Portfolio.


        :param id: The id of this Portfolio.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Portfolio.  # noqa: E501

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :return: The type of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Portfolio.

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :param type: The type of this Portfolio.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Transaction", "Reference", "DerivedTransaction"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this Portfolio.  # noqa: E501

        The name of the portfolio.  # noqa: E501

        :return: The display_name of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Portfolio.

        The name of the portfolio.  # noqa: E501

        :param display_name: The display_name of this Portfolio.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Portfolio.  # noqa: E501

        The long form description of the portfolio.  # noqa: E501

        :return: The description of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Portfolio.

        The long form description of the portfolio.  # noqa: E501

        :param description: The description of this Portfolio.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this Portfolio.  # noqa: E501

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :return: The created of this Portfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Portfolio.

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :param created: The created of this Portfolio.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def parent_portfolio_id(self):
        """Gets the parent_portfolio_id of this Portfolio.  # noqa: E501


        :return: The parent_portfolio_id of this Portfolio.  # noqa: E501
        :rtype: ResourceId
        """
        return self._parent_portfolio_id

    @parent_portfolio_id.setter
    def parent_portfolio_id(self, parent_portfolio_id):
        """Sets the parent_portfolio_id of this Portfolio.


        :param parent_portfolio_id: The parent_portfolio_id of this Portfolio.  # noqa: E501
        :type: ResourceId
        """

        self._parent_portfolio_id = parent_portfolio_id

    @property
    def version(self):
        """Gets the version of this Portfolio.  # noqa: E501


        :return: The version of this Portfolio.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Portfolio.


        :param version: The version of this Portfolio.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def is_derived(self):
        """Gets the is_derived of this Portfolio.  # noqa: E501

        Whether or not this is a derived portfolio.  # noqa: E501

        :return: The is_derived of this Portfolio.  # noqa: E501
        :rtype: bool
        """
        return self._is_derived

    @is_derived.setter
    def is_derived(self, is_derived):
        """Sets the is_derived of this Portfolio.

        Whether or not this is a derived portfolio.  # noqa: E501

        :param is_derived: The is_derived of this Portfolio.  # noqa: E501
        :type: bool
        """

        self._is_derived = is_derived

    @property
    def base_currency(self):
        """Gets the base_currency of this Portfolio.  # noqa: E501

        The base currency of the portfolio. This will be an empty string for reference portfolios.  # noqa: E501

        :return: The base_currency of this Portfolio.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this Portfolio.

        The base currency of the portfolio. This will be an empty string for reference portfolios.  # noqa: E501

        :param base_currency: The base_currency of this Portfolio.  # noqa: E501
        :type: str
        """

        self._base_currency = base_currency

    @property
    def properties(self):
        """Gets the properties of this Portfolio.  # noqa: E501

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :return: The properties of this Portfolio.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Portfolio.

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :param properties: The properties of this Portfolio.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

    @property
    def links(self):
        """Gets the links of this Portfolio.  # noqa: E501


        :return: The links of this Portfolio.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Portfolio.


        :param links: The links of this Portfolio.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, Portfolio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
