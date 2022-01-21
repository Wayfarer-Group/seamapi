# TODO this file should eventually be generated by looking at openapi.json

import abc
from typing import List, Optional, Union, Dict, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json

DeviceId = str
AcceptedProvider = str  # e.g. august or noiseaware


@dataclass_json
@dataclass
class Device:
    device_id: DeviceId
    device_type: str
    location: Optional[Dict[str, Any]]
    properties: Dict[str, Any]


@dataclass_json
@dataclass
class ActionAttempt:
    action_attempt_id: str
    status: str


@dataclass_json
@dataclass
class Workspace:
    workspace_id: str
    name: str
    is_sandbox: bool


@dataclass_json
@dataclass
class ConnectWebview:
    connect_webview_id: str
    status: str
    url: str
    login_successful: bool
    third_party_account_id: Optional[str]


@dataclass_json
@dataclass
class AccessCode:
    access_code_id: str
    type: str
    code: str
    name: Optional[str] = ""


class AbstractLocks(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Device]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, device: Union[DeviceId, Device]) -> Device:
        raise NotImplementedError

    @abc.abstractmethod
    def lock_door(self, device: Union[DeviceId, Device]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def unlock_door(self, device: Union[DeviceId, Device]) -> None:
        raise NotImplementedError


class AbstractAccessCodes(abc.ABC):
    @abc.abstractmethod
    def list(self, device: Union[DeviceId, Device]) -> List[AccessCode]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, device: Union[DeviceId, Device], name: str, code: str) -> None:
        raise NotImplementedError


class AbstractActionAttempt(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[ActionAttempt]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, workspace_id: Optional[str] = None) -> ActionAttempt:
        raise NotImplementedError


class AbstractDevices(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Device]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, device: Union[DeviceId, Device]) -> Device:
        raise NotImplementedError


class AbstractWorkspaces(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Workspace]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, workspace_id: Optional[str] = None) -> Workspace:
        raise NotImplementedError

    @abc.abstractmethod
    def reset_sandbox(
        self, workspace_id: Optional[str] = None, sandbox_type: Optional[str] = None
    ) -> None:
        raise NotImplementedError


class AbstractConnectWebviews(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[ConnectWebview]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, connect_webview_id: str) -> ConnectWebview:
        raise NotImplementedError

    @abc.abstractmethod
    def create(
        self, accepted_providers: Optional[List[AcceptedProvider]] = None
    ) -> ConnectWebview:
        raise NotImplementedError


@dataclass
class AbstractSeam(abc.ABC):
    api_key: str
    api_url: str

    workspaces: AbstractWorkspaces
    connect_webviews: AbstractConnectWebviews
    locks: AbstractLocks
    devices: AbstractDevices
    access_codes: AbstractAccessCodes

    @abc.abstractmethod
    def __init__(self, api_key: Optional[str] = None):
        raise NotImplementedError
