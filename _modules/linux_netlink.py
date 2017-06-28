# -*- coding: utf-8 -*-

import re


def ls(regex=r'^[a-z0-9]+$'):
    """
    Provide a list of network interfaces.
    """
    _lo_re = re.compile(r'^lo$')
    _alphanum_re = re.compile(regex)

    def _filter(interface):
        return _alphanum_re.match(interface) and not _lo_re.match(interface)

    return filter(_filter, __salt__['grains.get']('ip_interfaces', {}).keys())
