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

class UpsertRecipeRequest(object):
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
        'configuration_recipe': 'ConfigurationRecipe',
        'configuration_recipe_snippet': 'ConfigurationRecipeSnippet'
    }

    attribute_map = {
        'configuration_recipe': 'configurationRecipe',
        'configuration_recipe_snippet': 'configurationRecipeSnippet'
    }

    required_map = {
        'configuration_recipe': 'optional',
        'configuration_recipe_snippet': 'optional'
    }

    def __init__(self, configuration_recipe=None, configuration_recipe_snippet=None):  # noqa: E501
        """
        UpsertRecipeRequest - a model defined in OpenAPI

        :param configuration_recipe: 
        :type configuration_recipe: lusid.ConfigurationRecipe
        :param configuration_recipe_snippet: 
        :type configuration_recipe_snippet: lusid.ConfigurationRecipeSnippet

        """  # noqa: E501

        self._configuration_recipe = None
        self._configuration_recipe_snippet = None
        self.discriminator = None

        if configuration_recipe is not None:
            self.configuration_recipe = configuration_recipe
        if configuration_recipe_snippet is not None:
            self.configuration_recipe_snippet = configuration_recipe_snippet

    @property
    def configuration_recipe(self):
        """Gets the configuration_recipe of this UpsertRecipeRequest.  # noqa: E501


        :return: The configuration_recipe of this UpsertRecipeRequest.  # noqa: E501
        :rtype: ConfigurationRecipe
        """
        return self._configuration_recipe

    @configuration_recipe.setter
    def configuration_recipe(self, configuration_recipe):
        """Sets the configuration_recipe of this UpsertRecipeRequest.


        :param configuration_recipe: The configuration_recipe of this UpsertRecipeRequest.  # noqa: E501
        :type: ConfigurationRecipe
        """

        self._configuration_recipe = configuration_recipe

    @property
    def configuration_recipe_snippet(self):
        """Gets the configuration_recipe_snippet of this UpsertRecipeRequest.  # noqa: E501


        :return: The configuration_recipe_snippet of this UpsertRecipeRequest.  # noqa: E501
        :rtype: ConfigurationRecipeSnippet
        """
        return self._configuration_recipe_snippet

    @configuration_recipe_snippet.setter
    def configuration_recipe_snippet(self, configuration_recipe_snippet):
        """Sets the configuration_recipe_snippet of this UpsertRecipeRequest.


        :param configuration_recipe_snippet: The configuration_recipe_snippet of this UpsertRecipeRequest.  # noqa: E501
        :type: ConfigurationRecipeSnippet
        """

        self._configuration_recipe_snippet = configuration_recipe_snippet

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
        if not isinstance(other, UpsertRecipeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
