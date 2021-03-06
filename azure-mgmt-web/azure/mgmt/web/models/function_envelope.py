# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class FunctionEnvelope(ProxyOnlyResource):
    """Web Job Information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar function_envelope_name: Function name.
    :vartype function_envelope_name: str
    :ivar function_app_id: Function App ID.
    :vartype function_app_id: str
    :param script_root_path_href: Script root path URI.
    :type script_root_path_href: str
    :param script_href: Script URI.
    :type script_href: str
    :param config_href: Config URI.
    :type config_href: str
    :param secrets_file_href: Secrets file URI.
    :type secrets_file_href: str
    :param href: Function URI.
    :type href: str
    :param config: Config information.
    :type config: object
    :param files: File list.
    :type files: dict
    :param test_data: Test data used when testing via the Azure Portal.
    :type test_data: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'function_envelope_name': {'readonly': True},
        'function_app_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'function_envelope_name': {'key': 'properties.name', 'type': 'str'},
        'function_app_id': {'key': 'properties.functionAppId', 'type': 'str'},
        'script_root_path_href': {'key': 'properties.scriptRootPathHref', 'type': 'str'},
        'script_href': {'key': 'properties.scriptHref', 'type': 'str'},
        'config_href': {'key': 'properties.configHref', 'type': 'str'},
        'secrets_file_href': {'key': 'properties.secretsFileHref', 'type': 'str'},
        'href': {'key': 'properties.href', 'type': 'str'},
        'config': {'key': 'properties.config', 'type': 'object'},
        'files': {'key': 'properties.files', 'type': '{str}'},
        'test_data': {'key': 'properties.testData', 'type': 'str'},
    }

    def __init__(self, kind=None, script_root_path_href=None, script_href=None, config_href=None, secrets_file_href=None, href=None, config=None, files=None, test_data=None):
        super(FunctionEnvelope, self).__init__(kind=kind)
        self.function_envelope_name = None
        self.function_app_id = None
        self.script_root_path_href = script_root_path_href
        self.script_href = script_href
        self.config_href = config_href
        self.secrets_file_href = secrets_file_href
        self.href = href
        self.config = config
        self.files = files
        self.test_data = test_data
