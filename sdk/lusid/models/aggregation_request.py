# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2691
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AggregationRequest(object):
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
        'recipe_id': 'ResourceId',
        'inline_recipe': 'ConfigurationRecipe',
        'as_at': 'datetime',
        'effective_from': 'str',
        'effective_at': 'str',
        'metrics': 'list[AggregateSpec]',
        'group_by': 'list[str]',
        'filters': 'list[PropertyFilter]',
        'limit': 'int',
        'sort': 'list[OrderBySpec]',
        'report_ccy': 'str',
        'portfolio_identifier_code': 'str'
    }

    attribute_map = {
        'recipe_id': 'recipeId',
        'inline_recipe': 'inlineRecipe',
        'as_at': 'asAt',
        'effective_from': 'effectiveFrom',
        'effective_at': 'effectiveAt',
        'metrics': 'metrics',
        'group_by': 'groupBy',
        'filters': 'filters',
        'limit': 'limit',
        'sort': 'sort',
        'report_ccy': 'reportCcy',
        'portfolio_identifier_code': 'portfolioIdentifierCode'
    }

    required_map = {
        'recipe_id': 'optional',
        'inline_recipe': 'optional',
        'as_at': 'optional',
        'effective_from': 'optional',
        'effective_at': 'required',
        'metrics': 'required',
        'group_by': 'optional',
        'filters': 'optional',
        'limit': 'optional',
        'sort': 'optional',
        'report_ccy': 'optional',
        'portfolio_identifier_code': 'optional'
    }

    def __init__(self, recipe_id=None, inline_recipe=None, as_at=None, effective_from=None, effective_at=None, metrics=None, group_by=None, filters=None, limit=None, sort=None, report_ccy=None, portfolio_identifier_code=None):  # noqa: E501
        """
        AggregationRequest - a model defined in OpenAPI

        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param inline_recipe: 
        :type inline_recipe: lusid.ConfigurationRecipe
        :param as_at:  The asAt date to use
        :type as_at: datetime
        :param effective_from:  If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each date that is a business day in the given range.
        :type effective_from: str
        :param effective_at:  The market data time, i.e. the time to run the aggregation request effective of. (required)
        :type effective_at: str
        :param metrics:  The set of specifications for items to calculate or retrieve during the aggregation and present in the results.  This is logically equivalent to the set of operations in a Sql select statement  select [operation1(field1), operation2(field2), ... ] from results (required)
        :type metrics: list[lusid.AggregateSpec]
        :param group_by:  The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.
        :type group_by: list[str]
        :param filters:  A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.
        :type filters: list[lusid.PropertyFilter]
        :param limit:  limit the results to a particular number of values.
        :type limit: int
        :param sort:  A (possibly empty/null) set of specifications for how to order the results.
        :type sort: list[lusid.OrderBySpec]
        :param report_ccy:  Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.
        :type report_ccy: str
        :param portfolio_identifier_code:  String identifier for portfolio e.g. \"SinglePortfolio\" and \"GroupPortfolio\"
        :type portfolio_identifier_code: str

        """  # noqa: E501

        self._recipe_id = None
        self._inline_recipe = None
        self._as_at = None
        self._effective_from = None
        self._effective_at = None
        self._metrics = None
        self._group_by = None
        self._filters = None
        self._limit = None
        self._sort = None
        self._report_ccy = None
        self._portfolio_identifier_code = None
        self.discriminator = None

        if recipe_id is not None:
            self.recipe_id = recipe_id
        if inline_recipe is not None:
            self.inline_recipe = inline_recipe
        self.as_at = as_at
        self.effective_from = effective_from
        self.effective_at = effective_at
        self.metrics = metrics
        self.group_by = group_by
        self.filters = filters
        self.limit = limit
        self.sort = sort
        self.report_ccy = report_ccy
        self.portfolio_identifier_code = portfolio_identifier_code

    @property
    def recipe_id(self):
        """Gets the recipe_id of this AggregationRequest.  # noqa: E501


        :return: The recipe_id of this AggregationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this AggregationRequest.


        :param recipe_id: The recipe_id of this AggregationRequest.  # noqa: E501
        :type: ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def inline_recipe(self):
        """Gets the inline_recipe of this AggregationRequest.  # noqa: E501


        :return: The inline_recipe of this AggregationRequest.  # noqa: E501
        :rtype: ConfigurationRecipe
        """
        return self._inline_recipe

    @inline_recipe.setter
    def inline_recipe(self, inline_recipe):
        """Sets the inline_recipe of this AggregationRequest.


        :param inline_recipe: The inline_recipe of this AggregationRequest.  # noqa: E501
        :type: ConfigurationRecipe
        """

        self._inline_recipe = inline_recipe

    @property
    def as_at(self):
        """Gets the as_at of this AggregationRequest.  # noqa: E501

        The asAt date to use  # noqa: E501

        :return: The as_at of this AggregationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this AggregationRequest.

        The asAt date to use  # noqa: E501

        :param as_at: The as_at of this AggregationRequest.  # noqa: E501
        :type: datetime
        """

        self._as_at = as_at

    @property
    def effective_from(self):
        """Gets the effective_from of this AggregationRequest.  # noqa: E501

        If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each date that is a business day in the given range.  # noqa: E501

        :return: The effective_from of this AggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this AggregationRequest.

        If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each date that is a business day in the given range.  # noqa: E501

        :param effective_from: The effective_from of this AggregationRequest.  # noqa: E501
        :type: str
        """

        self._effective_from = effective_from

    @property
    def effective_at(self):
        """Gets the effective_at of this AggregationRequest.  # noqa: E501

        The market data time, i.e. the time to run the aggregation request effective of.  # noqa: E501

        :return: The effective_at of this AggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this AggregationRequest.

        The market data time, i.e. the time to run the aggregation request effective of.  # noqa: E501

        :param effective_at: The effective_at of this AggregationRequest.  # noqa: E501
        :type: str
        """
        if effective_at is None:
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def metrics(self):
        """Gets the metrics of this AggregationRequest.  # noqa: E501

        The set of specifications for items to calculate or retrieve during the aggregation and present in the results.  This is logically equivalent to the set of operations in a Sql select statement  select [operation1(field1), operation2(field2), ... ] from results  # noqa: E501

        :return: The metrics of this AggregationRequest.  # noqa: E501
        :rtype: list[AggregateSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AggregationRequest.

        The set of specifications for items to calculate or retrieve during the aggregation and present in the results.  This is logically equivalent to the set of operations in a Sql select statement  select [operation1(field1), operation2(field2), ... ] from results  # noqa: E501

        :param metrics: The metrics of this AggregationRequest.  # noqa: E501
        :type: list[AggregateSpec]
        """
        if metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def group_by(self):
        """Gets the group_by of this AggregationRequest.  # noqa: E501

        The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.  # noqa: E501

        :return: The group_by of this AggregationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this AggregationRequest.

        The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.  # noqa: E501

        :param group_by: The group_by of this AggregationRequest.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def filters(self):
        """Gets the filters of this AggregationRequest.  # noqa: E501

        A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.  # noqa: E501

        :return: The filters of this AggregationRequest.  # noqa: E501
        :rtype: list[PropertyFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AggregationRequest.

        A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.  # noqa: E501

        :param filters: The filters of this AggregationRequest.  # noqa: E501
        :type: list[PropertyFilter]
        """

        self._filters = filters

    @property
    def limit(self):
        """Gets the limit of this AggregationRequest.  # noqa: E501

        limit the results to a particular number of values.  # noqa: E501

        :return: The limit of this AggregationRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AggregationRequest.

        limit the results to a particular number of values.  # noqa: E501

        :param limit: The limit of this AggregationRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this AggregationRequest.  # noqa: E501

        A (possibly empty/null) set of specifications for how to order the results.  # noqa: E501

        :return: The sort of this AggregationRequest.  # noqa: E501
        :rtype: list[OrderBySpec]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this AggregationRequest.

        A (possibly empty/null) set of specifications for how to order the results.  # noqa: E501

        :param sort: The sort of this AggregationRequest.  # noqa: E501
        :type: list[OrderBySpec]
        """

        self._sort = sort

    @property
    def report_ccy(self):
        """Gets the report_ccy of this AggregationRequest.  # noqa: E501

        Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.  # noqa: E501

        :return: The report_ccy of this AggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_ccy

    @report_ccy.setter
    def report_ccy(self, report_ccy):
        """Sets the report_ccy of this AggregationRequest.

        Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.  # noqa: E501

        :param report_ccy: The report_ccy of this AggregationRequest.  # noqa: E501
        :type: str
        """

        self._report_ccy = report_ccy

    @property
    def portfolio_identifier_code(self):
        """Gets the portfolio_identifier_code of this AggregationRequest.  # noqa: E501

        String identifier for portfolio e.g. \"SinglePortfolio\" and \"GroupPortfolio\"  # noqa: E501

        :return: The portfolio_identifier_code of this AggregationRequest.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_identifier_code

    @portfolio_identifier_code.setter
    def portfolio_identifier_code(self, portfolio_identifier_code):
        """Sets the portfolio_identifier_code of this AggregationRequest.

        String identifier for portfolio e.g. \"SinglePortfolio\" and \"GroupPortfolio\"  # noqa: E501

        :param portfolio_identifier_code: The portfolio_identifier_code of this AggregationRequest.  # noqa: E501
        :type: str
        """

        self._portfolio_identifier_code = portfolio_identifier_code

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
        if not isinstance(other, AggregationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
