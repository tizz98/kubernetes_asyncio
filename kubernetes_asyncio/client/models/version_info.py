# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class VersionInfo(object):
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
        'build_date': 'str',
        'compiler': 'str',
        'git_commit': 'str',
        'git_tree_state': 'str',
        'git_version': 'str',
        'go_version': 'str',
        'major': 'str',
        'minor': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'build_date': 'buildDate',
        'compiler': 'compiler',
        'git_commit': 'gitCommit',
        'git_tree_state': 'gitTreeState',
        'git_version': 'gitVersion',
        'go_version': 'goVersion',
        'major': 'major',
        'minor': 'minor',
        'platform': 'platform'
    }

    def __init__(self, build_date=None, compiler=None, git_commit=None, git_tree_state=None, git_version=None, go_version=None, major=None, minor=None, platform=None, local_vars_configuration=None):  # noqa: E501
        """VersionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_date = None
        self._compiler = None
        self._git_commit = None
        self._git_tree_state = None
        self._git_version = None
        self._go_version = None
        self._major = None
        self._minor = None
        self._platform = None
        self.discriminator = None

        self.build_date = build_date
        self.compiler = compiler
        self.git_commit = git_commit
        self.git_tree_state = git_tree_state
        self.git_version = git_version
        self.go_version = go_version
        self.major = major
        self.minor = minor
        self.platform = platform

    @property
    def build_date(self):
        """Gets the build_date of this VersionInfo.  # noqa: E501


        :return: The build_date of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._build_date

    @build_date.setter
    def build_date(self, build_date):
        """Sets the build_date of this VersionInfo.


        :param build_date: The build_date of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and build_date is None:  # noqa: E501
            raise ValueError("Invalid value for `build_date`, must not be `None`")  # noqa: E501

        self._build_date = build_date

    @property
    def compiler(self):
        """Gets the compiler of this VersionInfo.  # noqa: E501


        :return: The compiler of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._compiler

    @compiler.setter
    def compiler(self, compiler):
        """Sets the compiler of this VersionInfo.


        :param compiler: The compiler of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and compiler is None:  # noqa: E501
            raise ValueError("Invalid value for `compiler`, must not be `None`")  # noqa: E501

        self._compiler = compiler

    @property
    def git_commit(self):
        """Gets the git_commit of this VersionInfo.  # noqa: E501


        :return: The git_commit of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this VersionInfo.


        :param git_commit: The git_commit of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and git_commit is None:  # noqa: E501
            raise ValueError("Invalid value for `git_commit`, must not be `None`")  # noqa: E501

        self._git_commit = git_commit

    @property
    def git_tree_state(self):
        """Gets the git_tree_state of this VersionInfo.  # noqa: E501


        :return: The git_tree_state of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._git_tree_state

    @git_tree_state.setter
    def git_tree_state(self, git_tree_state):
        """Sets the git_tree_state of this VersionInfo.


        :param git_tree_state: The git_tree_state of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and git_tree_state is None:  # noqa: E501
            raise ValueError("Invalid value for `git_tree_state`, must not be `None`")  # noqa: E501

        self._git_tree_state = git_tree_state

    @property
    def git_version(self):
        """Gets the git_version of this VersionInfo.  # noqa: E501


        :return: The git_version of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._git_version

    @git_version.setter
    def git_version(self, git_version):
        """Sets the git_version of this VersionInfo.


        :param git_version: The git_version of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and git_version is None:  # noqa: E501
            raise ValueError("Invalid value for `git_version`, must not be `None`")  # noqa: E501

        self._git_version = git_version

    @property
    def go_version(self):
        """Gets the go_version of this VersionInfo.  # noqa: E501


        :return: The go_version of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._go_version

    @go_version.setter
    def go_version(self, go_version):
        """Sets the go_version of this VersionInfo.


        :param go_version: The go_version of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and go_version is None:  # noqa: E501
            raise ValueError("Invalid value for `go_version`, must not be `None`")  # noqa: E501

        self._go_version = go_version

    @property
    def major(self):
        """Gets the major of this VersionInfo.  # noqa: E501


        :return: The major of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this VersionInfo.


        :param major: The major of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and major is None:  # noqa: E501
            raise ValueError("Invalid value for `major`, must not be `None`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this VersionInfo.  # noqa: E501


        :return: The minor of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this VersionInfo.


        :param minor: The minor of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and minor is None:  # noqa: E501
            raise ValueError("Invalid value for `minor`, must not be `None`")  # noqa: E501

        self._minor = minor

    @property
    def platform(self):
        """Gets the platform of this VersionInfo.  # noqa: E501


        :return: The platform of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this VersionInfo.


        :param platform: The platform of this VersionInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

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
        if not isinstance(other, VersionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VersionInfo):
            return True

        return self.to_dict() != other.to_dict()
