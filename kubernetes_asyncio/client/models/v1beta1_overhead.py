# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.23.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1beta1Overhead(object):
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
    """
    openapi_types = {
        'pod_fixed': 'dict(str, str)'
    }

    attribute_map = {
        'pod_fixed': 'podFixed'
    }

    def __init__(self, pod_fixed=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1Overhead - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._pod_fixed = None
        self.discriminator = None

        if pod_fixed is not None:
            self.pod_fixed = pod_fixed

    @property
    def pod_fixed(self):
        """Gets the pod_fixed of this V1beta1Overhead.  # noqa: E501

        PodFixed represents the fixed resource overhead associated with running a pod.  # noqa: E501

        :return: The pod_fixed of this V1beta1Overhead.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pod_fixed

    @pod_fixed.setter
    def pod_fixed(self, pod_fixed):
        """Sets the pod_fixed of this V1beta1Overhead.

        PodFixed represents the fixed resource overhead associated with running a pod.  # noqa: E501

        :param pod_fixed: The pod_fixed of this V1beta1Overhead.  # noqa: E501
        :type pod_fixed: dict(str, str)
        """

        self._pod_fixed = pod_fixed

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1Overhead):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1Overhead):
            return True

        return self.to_dict() != other.to_dict()
