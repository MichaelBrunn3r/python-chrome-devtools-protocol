# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Storage (experimental)

from __future__ import annotations
from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing


class StorageType(enum.Enum):
    '''
    Enum of possible storage types.
    '''
    APPCACHE = "appcache"
    COOKIES = "cookies"
    FILE_SYSTEMS = "file_systems"
    INDEXEDDB = "indexeddb"
    LOCAL_STORAGE = "local_storage"
    SHADER_CACHE = "shader_cache"
    WEBSQL = "websql"
    SERVICE_WORKERS = "service_workers"
    CACHE_STORAGE = "cache_storage"
    ALL_ = "all"
    OTHER = "other"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> StorageType:
        return cls(json)


@dataclass
class UsageForType:
    '''
    Usage for a storage type.
    '''
    #: Name of storage type.
    storage_type: StorageType

    #: Storage usage (bytes).
    usage: float

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['storageType'] = self.storage_type.to_json()
        json['usage'] = self.usage
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> UsageForType:
        return cls(
            storage_type=StorageType.from_json(json['storageType']),
            usage=float(json['usage']),
        )


def clear_data_for_origin(
        origin: str,
        storage_types: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Clears storage for origin.

    :param origin: Security origin.
    :param storage_types: Comma separated list of StorageType to clear.
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    params['storageTypes'] = storage_types
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.clearDataForOrigin',
        'params': params,
    }
    json = yield cmd_dict


def get_usage_and_quota(
        origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.Tuple[float, float, typing.List[UsageForType]]]:
    '''
    Returns usage and quota in bytes.

    :param origin: Security origin.
    :returns: A tuple with the following items:

        0. **usage** – Storage usage (bytes).
        1. **quota** – Storage quota (bytes).
        2. **usageBreakdown** – Storage usage per type (bytes).
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.getUsageAndQuota',
        'params': params,
    }
    json = yield cmd_dict
    return (
        float(json['usage']),
        float(json['quota']),
        [UsageForType.from_json(i) for i in json['usageBreakdown']]
    )


def track_cache_storage_for_origin(
        origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Registers origin to be notified when an update occurs to its cache storage list.

    :param origin: Security origin.
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.trackCacheStorageForOrigin',
        'params': params,
    }
    json = yield cmd_dict


def track_indexed_db_for_origin(
        origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Registers origin to be notified when an update occurs to its IndexedDB.

    :param origin: Security origin.
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.trackIndexedDBForOrigin',
        'params': params,
    }
    json = yield cmd_dict


def untrack_cache_storage_for_origin(
        origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Unregisters origin from receiving notifications for cache storage.

    :param origin: Security origin.
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.untrackCacheStorageForOrigin',
        'params': params,
    }
    json = yield cmd_dict


def untrack_indexed_db_for_origin(
        origin: str
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Unregisters origin from receiving notifications for IndexedDB.

    :param origin: Security origin.
    '''
    params: T_JSON_DICT = dict()
    params['origin'] = origin
    cmd_dict: T_JSON_DICT = {
        'method': 'Storage.untrackIndexedDBForOrigin',
        'params': params,
    }
    json = yield cmd_dict


@event_class('Storage.cacheStorageContentUpdated')
@dataclass
class CacheStorageContentUpdated:
    '''
    A cache's contents have been modified.
    '''
    #: Origin to update.
    origin: str
    #: Name of cache in origin.
    cache_name: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CacheStorageContentUpdated:
        return cls(
            origin=str(json['origin']),
            cache_name=str(json['cacheName'])
        )


@event_class('Storage.cacheStorageListUpdated')
@dataclass
class CacheStorageListUpdated:
    '''
    A cache has been added/deleted.
    '''
    #: Origin to update.
    origin: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> CacheStorageListUpdated:
        return cls(
            origin=str(json['origin'])
        )


@event_class('Storage.indexedDBContentUpdated')
@dataclass
class IndexedDBContentUpdated:
    '''
    The origin's IndexedDB object store has been modified.
    '''
    #: Origin to update.
    origin: str
    #: Database to update.
    database_name: str
    #: ObjectStore to update.
    object_store_name: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> IndexedDBContentUpdated:
        return cls(
            origin=str(json['origin']),
            database_name=str(json['databaseName']),
            object_store_name=str(json['objectStoreName'])
        )


@event_class('Storage.indexedDBListUpdated')
@dataclass
class IndexedDBListUpdated:
    '''
    The origin's IndexedDB database list has been modified.
    '''
    #: Origin to update.
    origin: str

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> IndexedDBListUpdated:
        return cls(
            origin=str(json['origin'])
        )
