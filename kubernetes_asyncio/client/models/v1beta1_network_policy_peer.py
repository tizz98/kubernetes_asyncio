# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1beta1NetworkPolicyPeer(object):
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
        'ip_block': 'V1beta1IPBlock',
        'namespace_selector': 'V1LabelSelector',
        'pod_selector': 'V1LabelSelector'
    }

    attribute_map = {
        'ip_block': 'ipBlock',
        'namespace_selector': 'namespaceSelector',
        'pod_selector': 'podSelector'
    }

    def __init__(self, ip_block=None, namespace_selector=None, pod_selector=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1NetworkPolicyPeer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip_block = None
        self._namespace_selector = None
        self._pod_selector = None
        self.discriminator = None

        if ip_block is not None:
            self.ip_block = ip_block
        if namespace_selector is not None:
            self.namespace_selector = namespace_selector
        if pod_selector is not None:
            self.pod_selector = pod_selector

    @property
    def ip_block(self):
        """Gets the ip_block of this V1beta1NetworkPolicyPeer.  # noqa: E501


        :return: The ip_block of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :rtype: V1beta1IPBlock
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        """Sets the ip_block of this V1beta1NetworkPolicyPeer.


        :param ip_block: The ip_block of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :type: V1beta1IPBlock
        """

        self._ip_block = ip_block

    @property
    def namespace_selector(self):
        """Gets the namespace_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501


        :return: The namespace_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """Sets the namespace_selector of this V1beta1NetworkPolicyPeer.


        :param namespace_selector: The namespace_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def pod_selector(self):
        """Gets the pod_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501


        :return: The pod_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        """Sets the pod_selector of this V1beta1NetworkPolicyPeer.


        :param pod_selector: The pod_selector of this V1beta1NetworkPolicyPeer.  # noqa: E501
        :type: V1LabelSelector
        """

        self._pod_selector = pod_selector

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
        if not isinstance(other, V1beta1NetworkPolicyPeer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1NetworkPolicyPeer):
            return True

        return self.to_dict() != other.to_dict()
