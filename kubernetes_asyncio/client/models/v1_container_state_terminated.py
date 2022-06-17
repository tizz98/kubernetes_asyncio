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


class V1ContainerStateTerminated(object):
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
        'container_id': 'str',
        'exit_code': 'int',
        'finished_at': 'datetime',
        'message': 'str',
        'reason': 'str',
        'signal': 'int',
        'started_at': 'datetime'
    }

    attribute_map = {
        'container_id': 'containerID',
        'exit_code': 'exitCode',
        'finished_at': 'finishedAt',
        'message': 'message',
        'reason': 'reason',
        'signal': 'signal',
        'started_at': 'startedAt'
    }

    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None, started_at=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerStateTerminated - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._container_id = None
        self._exit_code = None
        self._finished_at = None
        self._message = None
        self._reason = None
        self._signal = None
        self._started_at = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        self.exit_code = exit_code
        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if signal is not None:
            self.signal = signal
        if started_at is not None:
            self.started_at = started_at

    @property
    def container_id(self):
        """Gets the container_id of this V1ContainerStateTerminated.  # noqa: E501

        Container's ID in the format 'docker://<container_id>'  # noqa: E501

        :return: The container_id of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this V1ContainerStateTerminated.

        Container's ID in the format 'docker://<container_id>'  # noqa: E501

        :param container_id: The container_id of this V1ContainerStateTerminated.  # noqa: E501
        :type container_id: str
        """

        self._container_id = container_id

    @property
    def exit_code(self):
        """Gets the exit_code of this V1ContainerStateTerminated.  # noqa: E501

        Exit status from the last termination of the container  # noqa: E501

        :return: The exit_code of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this V1ContainerStateTerminated.

        Exit status from the last termination of the container  # noqa: E501

        :param exit_code: The exit_code of this V1ContainerStateTerminated.  # noqa: E501
        :type exit_code: int
        """
        if self.local_vars_configuration.client_side_validation and exit_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exit_code`, must not be `None`")  # noqa: E501

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """Gets the finished_at of this V1ContainerStateTerminated.  # noqa: E501

        Time at which the container last terminated  # noqa: E501

        :return: The finished_at of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1ContainerStateTerminated.

        Time at which the container last terminated  # noqa: E501

        :param finished_at: The finished_at of this V1ContainerStateTerminated.  # noqa: E501
        :type finished_at: datetime
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this V1ContainerStateTerminated.  # noqa: E501

        Message regarding the last termination of the container  # noqa: E501

        :return: The message of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1ContainerStateTerminated.

        Message regarding the last termination of the container  # noqa: E501

        :param message: The message of this V1ContainerStateTerminated.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this V1ContainerStateTerminated.  # noqa: E501

        (brief) reason from the last termination of the container  # noqa: E501

        :return: The reason of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1ContainerStateTerminated.

        (brief) reason from the last termination of the container  # noqa: E501

        :param reason: The reason of this V1ContainerStateTerminated.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def signal(self):
        """Gets the signal of this V1ContainerStateTerminated.  # noqa: E501

        Signal from the last termination of the container  # noqa: E501

        :return: The signal of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """Sets the signal of this V1ContainerStateTerminated.

        Signal from the last termination of the container  # noqa: E501

        :param signal: The signal of this V1ContainerStateTerminated.  # noqa: E501
        :type signal: int
        """

        self._signal = signal

    @property
    def started_at(self):
        """Gets the started_at of this V1ContainerStateTerminated.  # noqa: E501

        Time at which previous execution of the container started  # noqa: E501

        :return: The started_at of this V1ContainerStateTerminated.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1ContainerStateTerminated.

        Time at which previous execution of the container started  # noqa: E501

        :param started_at: The started_at of this V1ContainerStateTerminated.  # noqa: E501
        :type started_at: datetime
        """

        self._started_at = started_at

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
        if not isinstance(other, V1ContainerStateTerminated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerStateTerminated):
            return True

        return self.to_dict() != other.to_dict()
