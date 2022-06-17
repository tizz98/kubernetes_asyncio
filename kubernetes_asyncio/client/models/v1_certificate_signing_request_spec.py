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


class V1CertificateSigningRequestSpec(object):
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
        'expiration_seconds': 'int',
        'extra': 'dict(str, list[str])',
        'groups': 'list[str]',
        'request': 'str',
        'signer_name': 'str',
        'uid': 'str',
        'usages': 'list[str]',
        'username': 'str'
    }

    attribute_map = {
        'expiration_seconds': 'expirationSeconds',
        'extra': 'extra',
        'groups': 'groups',
        'request': 'request',
        'signer_name': 'signerName',
        'uid': 'uid',
        'usages': 'usages',
        'username': 'username'
    }

    def __init__(self, expiration_seconds=None, extra=None, groups=None, request=None, signer_name=None, uid=None, usages=None, username=None, local_vars_configuration=None):  # noqa: E501
        """V1CertificateSigningRequestSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._expiration_seconds = None
        self._extra = None
        self._groups = None
        self._request = None
        self._signer_name = None
        self._uid = None
        self._usages = None
        self._username = None
        self.discriminator = None

        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds
        if extra is not None:
            self.extra = extra
        if groups is not None:
            self.groups = groups
        self.request = request
        self.signer_name = signer_name
        if uid is not None:
            self.uid = uid
        if usages is not None:
            self.usages = usages
        if username is not None:
            self.username = username

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this V1CertificateSigningRequestSpec.  # noqa: E501

        expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer whose configured maximum is shorter than the requested duration   3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.  As of v1.22, this field is beta and is controlled via the CSRDuration feature gate.  # noqa: E501

        :return: The expiration_seconds of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this V1CertificateSigningRequestSpec.

        expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer whose configured maximum is shorter than the requested duration   3. Signer whose configured minimum is longer than the requested duration  The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.  As of v1.22, this field is beta and is controlled via the CSRDuration feature gate.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type expiration_seconds: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def extra(self):
        """Gets the extra of this V1CertificateSigningRequestSpec.  # noqa: E501

        extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :return: The extra of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this V1CertificateSigningRequestSpec.

        extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :param extra: The extra of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type extra: dict(str, list[str])
        """

        self._extra = extra

    @property
    def groups(self):
        """Gets the groups of this V1CertificateSigningRequestSpec.  # noqa: E501

        groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :return: The groups of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V1CertificateSigningRequestSpec.

        groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :param groups: The groups of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type groups: list[str]
        """

        self._groups = groups

    @property
    def request(self):
        """Gets the request of this V1CertificateSigningRequestSpec.  # noqa: E501

        request contains an x509 certificate signing request encoded in a \"CERTIFICATE REQUEST\" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.  # noqa: E501

        :return: The request of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this V1CertificateSigningRequestSpec.

        request contains an x509 certificate signing request encoded in a \"CERTIFICATE REQUEST\" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.  # noqa: E501

        :param request: The request of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type request: str
        """
        if self.local_vars_configuration.client_side_validation and request is None:  # noqa: E501
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                request is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', request)):  # noqa: E501
            raise ValueError(r"Invalid value for `request`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._request = request

    @property
    def signer_name(self):
        """Gets the signer_name of this V1CertificateSigningRequestSpec.  # noqa: E501

        signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a \"spec.signerName=NAME\" fieldSelector.  Well-known Kubernetes signers are:  1. \"kubernetes.io/kube-apiserver-client\": issues client certificates that can be used to authenticate to kube-apiserver.   Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the \"csrsigning\" controller in kube-controller-manager.  2. \"kubernetes.io/kube-apiserver-client-kubelet\": issues client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this signer can be auto-approved by the \"csrapproving\" controller in kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  3. \"kubernetes.io/kubelet-serving\" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects: and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.  4. Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not requests for CA certificates are allowed.  # noqa: E501

        :return: The signer_name of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._signer_name

    @signer_name.setter
    def signer_name(self, signer_name):
        """Sets the signer_name of this V1CertificateSigningRequestSpec.

        signerName indicates the requested signer, and is a qualified name.  List/watch requests for CertificateSigningRequests can filter on this field using a \"spec.signerName=NAME\" fieldSelector.  Well-known Kubernetes signers are:  1. \"kubernetes.io/kube-apiserver-client\": issues client certificates that can be used to authenticate to kube-apiserver.   Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the \"csrsigning\" controller in kube-controller-manager.  2. \"kubernetes.io/kube-apiserver-client-kubelet\": issues client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this signer can be auto-approved by the \"csrapproving\" controller in kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  3. \"kubernetes.io/kubelet-serving\" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the \"csrsigning\" controller in kube-controller-manager.  More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects: and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.  4. Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not requests for CA certificates are allowed.  # noqa: E501

        :param signer_name: The signer_name of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type signer_name: str
        """
        if self.local_vars_configuration.client_side_validation and signer_name is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_name`, must not be `None`")  # noqa: E501

        self._signer_name = signer_name

    @property
    def uid(self):
        """Gets the uid of this V1CertificateSigningRequestSpec.  # noqa: E501

        uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :return: The uid of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1CertificateSigningRequestSpec.

        uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :param uid: The uid of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type uid: str
        """

        self._uid = uid

    @property
    def usages(self):
        """Gets the usages of this V1CertificateSigningRequestSpec.  # noqa: E501

        usages specifies a set of key usages requested in the issued certificate.  Requests for TLS client certificates typically request: \"digital signature\", \"key encipherment\", \"client auth\".  Requests for TLS serving certificates typically request: \"key encipherment\", \"digital signature\", \"server auth\".  Valid values are:  \"signing\", \"digital signature\", \"content commitment\",  \"key encipherment\", \"key agreement\", \"data encipherment\",  \"cert sign\", \"crl sign\", \"encipher only\", \"decipher only\", \"any\",  \"server auth\", \"client auth\",  \"code signing\", \"email protection\", \"s/mime\",  \"ipsec end system\", \"ipsec tunnel\", \"ipsec user\",  \"timestamping\", \"ocsp signing\", \"microsoft sgc\", \"netscape sgc\"  # noqa: E501

        :return: The usages of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._usages

    @usages.setter
    def usages(self, usages):
        """Sets the usages of this V1CertificateSigningRequestSpec.

        usages specifies a set of key usages requested in the issued certificate.  Requests for TLS client certificates typically request: \"digital signature\", \"key encipherment\", \"client auth\".  Requests for TLS serving certificates typically request: \"key encipherment\", \"digital signature\", \"server auth\".  Valid values are:  \"signing\", \"digital signature\", \"content commitment\",  \"key encipherment\", \"key agreement\", \"data encipherment\",  \"cert sign\", \"crl sign\", \"encipher only\", \"decipher only\", \"any\",  \"server auth\", \"client auth\",  \"code signing\", \"email protection\", \"s/mime\",  \"ipsec end system\", \"ipsec tunnel\", \"ipsec user\",  \"timestamping\", \"ocsp signing\", \"microsoft sgc\", \"netscape sgc\"  # noqa: E501

        :param usages: The usages of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type usages: list[str]
        """

        self._usages = usages

    @property
    def username(self):
        """Gets the username of this V1CertificateSigningRequestSpec.  # noqa: E501

        username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :return: The username of this V1CertificateSigningRequestSpec.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1CertificateSigningRequestSpec.

        username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.  # noqa: E501

        :param username: The username of this V1CertificateSigningRequestSpec.  # noqa: E501
        :type username: str
        """

        self._username = username

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
        if not isinstance(other, V1CertificateSigningRequestSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CertificateSigningRequestSpec):
            return True

        return self.to_dict() != other.to_dict()
