# coding: utf-8

"""
    Quetzal API

    Quetzal: an API to manage data files and their associated metadata.  # noqa: E501

    OpenAPI spec version: 0.5.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BaseMetadata(object):
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
        'checksum': 'str',
        'date': 'str',
        'filename': 'str',
        'id': 'str',
        'path': 'str',
        'size': 'int',
        'state': 'str',
        'url': 'str'
    }

    attribute_map = {
        'checksum': 'checksum',
        'date': 'date',
        'filename': 'filename',
        'id': 'id',
        'path': 'path',
        'size': 'size',
        'state': 'state',
        'url': 'url'
    }

    def __init__(self, checksum=None, date=None, filename=None, id=None, path=None, size=None, state=None, url=None):  # noqa: E501
        """BaseMetadata - a model defined in OpenAPI"""  # noqa: E501

        self._checksum = None
        self._date = None
        self._filename = None
        self._id = None
        self._path = None
        self._size = None
        self._state = None
        self._url = None
        self.discriminator = None

        self.checksum = checksum
        self.date = date
        self.filename = filename
        self.id = id
        self.path = path
        self.size = size
        self.state = state
        self.url = url

    @property
    def checksum(self):
        """Gets the checksum of this BaseMetadata.  # noqa: E501

        MD5 checksum of the file in hexadecimal string.  # noqa: E501

        :return: The checksum of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this BaseMetadata.

        MD5 checksum of the file in hexadecimal string.  # noqa: E501

        :param checksum: The checksum of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

    @property
    def date(self):
        """Gets the date of this BaseMetadata.  # noqa: E501

        Date when this file was uploaded to Quetzal.  # noqa: E501

        :return: The date of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BaseMetadata.

        Date when this file was uploaded to Quetzal.  # noqa: E501

        :param date: The date of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def filename(self):
        """Gets the filename of this BaseMetadata.  # noqa: E501

        File name. This does not include its path.  # noqa: E501

        :return: The filename of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BaseMetadata.

        File name. This does not include its path.  # noqa: E501

        :param filename: The filename of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def id(self):
        """Gets the id of this BaseMetadata.  # noqa: E501

        File identifier.  # noqa: E501

        :return: The id of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseMetadata.

        File identifier.  # noqa: E501

        :param id: The id of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def path(self):
        """Gets the path of this BaseMetadata.  # noqa: E501

        Path of the file.  # noqa: E501

        :return: The path of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BaseMetadata.

        Path of the file.  # noqa: E501

        :param path: The path of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this BaseMetadata.  # noqa: E501

        File size in bytes.  # noqa: E501

        :return: The size of this BaseMetadata.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BaseMetadata.

        File size in bytes.  # noqa: E501

        :param size: The size of this BaseMetadata.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def state(self):
        """Gets the state of this BaseMetadata.  # noqa: E501

        File status.  # noqa: E501

        :return: The state of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BaseMetadata.

        File status.  # noqa: E501

        :param state: The state of this BaseMetadata.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["READY", "TEMPORARY", "DELETED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def url(self):
        """Gets the url of this BaseMetadata.  # noqa: E501

        File URL on Quetzal's data bucket.  # noqa: E501

        :return: The url of this BaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BaseMetadata.

        File URL on Quetzal's data bucket.  # noqa: E501

        :param url: The url of this BaseMetadata.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, BaseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
