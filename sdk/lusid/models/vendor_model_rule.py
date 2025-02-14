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

class VendorModelRule(object):
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
        'supplier': 'str',
        'model_name': 'str',
        'instrument_type': 'str',
        'parameters': 'str'
    }

    attribute_map = {
        'supplier': 'supplier',
        'model_name': 'modelName',
        'instrument_type': 'instrumentType',
        'parameters': 'parameters'
    }

    required_map = {
        'supplier': 'required',
        'model_name': 'required',
        'instrument_type': 'required',
        'parameters': 'required'
    }

    def __init__(self, supplier=None, model_name=None, instrument_type=None, parameters=None):  # noqa: E501
        """
        VendorModelRule - a model defined in OpenAPI

        :param supplier:  The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds (required)
        :type supplier: str
        :param model_name:  The vendor library model name (required)
        :type model_name: str
        :param instrument_type:  The vendor library instrument type (required)
        :type instrument_type: str
        :param parameters:  The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood. (required)
        :type parameters: str

        """  # noqa: E501

        self._supplier = None
        self._model_name = None
        self._instrument_type = None
        self._parameters = None
        self.discriminator = None

        self.supplier = supplier
        self.model_name = model_name
        self.instrument_type = instrument_type
        self.parameters = parameters

    @property
    def supplier(self):
        """Gets the supplier of this VendorModelRule.  # noqa: E501

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds  # noqa: E501

        :return: The supplier of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this VendorModelRule.

        The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds  # noqa: E501

        :param supplier: The supplier of this VendorModelRule.  # noqa: E501
        :type: str
        """
        if supplier is None:
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501
        allowed_values = ["Lusid", "RefinitivQps", "RefinitivTracsWeb", "VolMaster", "IsdaCds"]  # noqa: E501
        if supplier not in allowed_values:
            raise ValueError(
                "Invalid value for `supplier` ({0}), must be one of {1}"  # noqa: E501
                .format(supplier, allowed_values)
            )

        self._supplier = supplier

    @property
    def model_name(self):
        """Gets the model_name of this VendorModelRule.  # noqa: E501

        The vendor library model name  # noqa: E501

        :return: The model_name of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this VendorModelRule.

        The vendor library model name  # noqa: E501

        :param model_name: The model_name of this VendorModelRule.  # noqa: E501
        :type: str
        """
        if model_name is None:
            raise ValueError("Invalid value for `model_name`, must not be `None`")  # noqa: E501

        self._model_name = model_name

    @property
    def instrument_type(self):
        """Gets the instrument_type of this VendorModelRule.  # noqa: E501

        The vendor library instrument type  # noqa: E501

        :return: The instrument_type of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this VendorModelRule.

        The vendor library instrument type  # noqa: E501

        :param instrument_type: The instrument_type of this VendorModelRule.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501

        self._instrument_type = instrument_type

    @property
    def parameters(self):
        """Gets the parameters of this VendorModelRule.  # noqa: E501

        The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.  # noqa: E501

        :return: The parameters of this VendorModelRule.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this VendorModelRule.

        The set of opaque model parameters, provided as a Json object, that is a string object which will internally be converted to a dictionary of string to object.  Note that this is not intended as the final form of this object. It will be replaced with a more structured object as the set of parameters that are possible is  better understood.  # noqa: E501

        :param parameters: The parameters of this VendorModelRule.  # noqa: E501
        :type: str
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, VendorModelRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
