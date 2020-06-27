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


class V1ContainerStatus(object):
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
        'image': 'str',
        'image_id': 'str',
        'last_state': 'V1ContainerState',
        'name': 'str',
        'ready': 'bool',
        'restart_count': 'int',
        'started': 'bool',
        'state': 'V1ContainerState'
    }

    attribute_map = {
        'container_id': 'containerID',
        'image': 'image',
        'image_id': 'imageID',
        'last_state': 'lastState',
        'name': 'name',
        'ready': 'ready',
        'restart_count': 'restartCount',
        'started': 'started',
        'state': 'state'
    }

    def __init__(self, container_id=None, image=None, image_id=None, last_state=None, name=None, ready=None, restart_count=None, started=None, state=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_id = None
        self._image = None
        self._image_id = None
        self._last_state = None
        self._name = None
        self._ready = None
        self._restart_count = None
        self._started = None
        self._state = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        self.image = image
        self.image_id = image_id
        if last_state is not None:
            self.last_state = last_state
        self.name = name
        self.ready = ready
        self.restart_count = restart_count
        if started is not None:
            self.started = started
        if state is not None:
            self.state = state

    @property
    def container_id(self):
        """Gets the container_id of this V1ContainerStatus.  # noqa: E501

        Container's ID in the format 'docker://<container_id>'.  # noqa: E501

        :return: The container_id of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this V1ContainerStatus.

        Container's ID in the format 'docker://<container_id>'.  # noqa: E501

        :param container_id: The container_id of this V1ContainerStatus.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def image(self):
        """Gets the image of this V1ContainerStatus.  # noqa: E501

        The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images  # noqa: E501

        :return: The image of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1ContainerStatus.

        The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images  # noqa: E501

        :param image: The image of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image is None:  # noqa: E501
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def image_id(self):
        """Gets the image_id of this V1ContainerStatus.  # noqa: E501

        ImageID of the container's image.  # noqa: E501

        :return: The image_id of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this V1ContainerStatus.

        ImageID of the container's image.  # noqa: E501

        :param image_id: The image_id of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def last_state(self):
        """Gets the last_state of this V1ContainerStatus.  # noqa: E501


        :return: The last_state of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ContainerState
        """
        return self._last_state

    @last_state.setter
    def last_state(self, last_state):
        """Sets the last_state of this V1ContainerStatus.


        :param last_state: The last_state of this V1ContainerStatus.  # noqa: E501
        :type: V1ContainerState
        """

        self._last_state = last_state

    @property
    def name(self):
        """Gets the name of this V1ContainerStatus.  # noqa: E501

        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.  # noqa: E501

        :return: The name of this V1ContainerStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ContainerStatus.

        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.  # noqa: E501

        :param name: The name of this V1ContainerStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ready(self):
        """Gets the ready of this V1ContainerStatus.  # noqa: E501

        Specifies whether the container has passed its readiness probe.  # noqa: E501

        :return: The ready of this V1ContainerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1ContainerStatus.

        Specifies whether the container has passed its readiness probe.  # noqa: E501

        :param ready: The ready of this V1ContainerStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ready is None:  # noqa: E501
            raise ValueError("Invalid value for `ready`, must not be `None`")  # noqa: E501

        self._ready = ready

    @property
    def restart_count(self):
        """Gets the restart_count of this V1ContainerStatus.  # noqa: E501

        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.  # noqa: E501

        :return: The restart_count of this V1ContainerStatus.  # noqa: E501
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """Sets the restart_count of this V1ContainerStatus.

        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.  # noqa: E501

        :param restart_count: The restart_count of this V1ContainerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and restart_count is None:  # noqa: E501
            raise ValueError("Invalid value for `restart_count`, must not be `None`")  # noqa: E501

        self._restart_count = restart_count

    @property
    def started(self):
        """Gets the started of this V1ContainerStatus.  # noqa: E501

        Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined.  # noqa: E501

        :return: The started of this V1ContainerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this V1ContainerStatus.

        Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined.  # noqa: E501

        :param started: The started of this V1ContainerStatus.  # noqa: E501
        :type: bool
        """

        self._started = started

    @property
    def state(self):
        """Gets the state of this V1ContainerStatus.  # noqa: E501


        :return: The state of this V1ContainerStatus.  # noqa: E501
        :rtype: V1ContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1ContainerStatus.


        :param state: The state of this V1ContainerStatus.  # noqa: E501
        :type: V1ContainerState
        """

        self._state = state

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
        if not isinstance(other, V1ContainerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerStatus):
            return True

        return self.to_dict() != other.to_dict()
