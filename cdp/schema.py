# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Schema

from __future__ import annotations
from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing


@dataclass
class Domain:
    '''
    Description of the protocol domain.
    '''
    #: Domain name.
    name: str

    #: Domain version.
    version: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['name'] = self.name
        json['version'] = self.version
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> Domain:
        return cls(
            name=str(json['name']),
            version=str(json['version']),
        )


def get_domains() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,typing.List[Domain]]:
    '''
    Returns supported domains.

    :returns: List of supported domains.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'Schema.getDomains',
    }
    json = yield cmd_dict
    return [Domain.from_json(i) for i in json['domains']]
