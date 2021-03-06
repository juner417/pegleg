# Copyright 2018 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO(felipemonteiro): This pattern below should be swapped out for click
# context passing but will require a somewhat heavy code refactor. See:
# http://click.pocoo.org/5/commands/#nested-handling-and-contexts

import os

from pegleg.engine import exceptions
from pegleg.engine import secrets

try:
    if GLOBAL_CONTEXT:
        pass
except NameError:
    GLOBAL_CONTEXT = {
        'site_repo': './',
        'extra_repos': [],
        'clone_path': None,
        'site_path': 'site',
        'site_rev': None,
        'type_path': 'type',
        'passphrase': None,
        'salt': None,
        'global_passphrase': None,
        'global_salt': None,
        'salt_min_length': 24,
        'passphrase_min_length': 24,
        'default_umask': 0o027,
        'decrypt_repos': False
    }


def set_umask():
    """Set the umask for Pegleg to use when creating files/folders."""
    os.umask(GLOBAL_CONTEXT['default_umask'])


def get_site_repo():
    """Get the primary site repository specified via ``-r`` CLI flag."""
    return GLOBAL_CONTEXT['site_repo']


def set_site_repo(r):
    """Set the primary site repository."""
    GLOBAL_CONTEXT['site_repo'] = r.rstrip('/') + '/'


def get_clone_path():
    """Get specified clone path (corresponds to ``-p`` CLI flag)."""
    return GLOBAL_CONTEXT['clone_path']


def set_clone_path(p):
    """Set specified clone path (corresponds to ``-p`` CLI flag)."""
    GLOBAL_CONTEXT['clone_path'] = p


def get_site_rev():
    """Get site revision derived from the site repo URL/path, if provided."""
    return GLOBAL_CONTEXT['site_rev']


def set_site_rev(r):
    """Set site revision derived from the site repo URL/path."""
    GLOBAL_CONTEXT['site_rev'] = r


def get_extra_repo_overrides():
    """Get extra repository overrides specified via ``-e`` CLI flag."""
    return GLOBAL_CONTEXT.get('extra_repo_overrides', [])


def set_extra_repo_overrides(r):
    """Set extra repository overrides.

    .. note:: Only CLI should call this.
    """
    GLOBAL_CONTEXT['extra_repo_overrides'] = r


def set_repo_key(k):
    """Set additional repository key, like extra metadata to track."""
    GLOBAL_CONTEXT['repo_key'] = k


def get_repo_key():
    """Get additional repository key."""
    return GLOBAL_CONTEXT.get('repo_key', None)


def set_repo_username(u):
    """Set repo username for SSH auth, corresponds to ``-u`` CLI flag."""
    GLOBAL_CONTEXT['repo_username'] = u


def get_repo_username():
    """Get repo username for SSH auth."""
    return GLOBAL_CONTEXT.get('repo_username', None)


def set_extra_repo_list(a):
    """Set the extra repository list to be used by ``pegleg.engine``."""
    GLOBAL_CONTEXT['extra_repos'] = [r.rstrip('/') + '/' for r in a]


def get_extra_repo_list():
    """Get the extra repository list.

    .. note::

        Use this instead of ``get_extra_repo_overrides`` as it handles
        both overrides and site-definition.yaml defaults.
    """
    return GLOBAL_CONTEXT['extra_repos']


def add_extra_repo(a):
    """Add an extra repo to the extra repository list."""
    GLOBAL_CONTEXT['extra_repos'].append(a.rstrip('/') + '/')


def each_extra_repo():
    """Iterate over each extra repo."""
    for a in GLOBAL_CONTEXT['extra_repos']:
        yield a


def all_repos():
    """Return the primary site repo, in addition to all extra ones."""
    repos = [get_site_repo()]
    repos.extend(get_extra_repo_list())
    return repos


def get_rel_site_path():
    """Get the relative site path name, default is "site"."""
    return GLOBAL_CONTEXT.get('site_path', 'site')


def set_rel_site_path(p):
    """Set the relative site path name."""
    p = p or 'site'
    GLOBAL_CONTEXT['site_path'] = p


def get_rel_type_path():
    """Get the relative type path name, default is "type"."""
    return GLOBAL_CONTEXT.get('type_path', 'type')


def set_rel_type_path(p):
    """Set the relative type path name."""
    p = p or 'type'
    GLOBAL_CONTEXT['type_path'] = p


def set_passphrase():
    """Set the passphrase for encryption and decryption."""

    passphrase = os.environ.get('PEGLEG_PASSPHRASE')
    if not passphrase:
        raise exceptions.PassphraseNotFoundException()
    elif len(passphrase) < GLOBAL_CONTEXT['passphrase_min_length']:
        raise exceptions.PassphraseInsufficientLengthException()

    GLOBAL_CONTEXT['passphrase'] = passphrase.encode()


def get_passphrase():
    """Get the passphrase for encryption and decryption."""
    return GLOBAL_CONTEXT['passphrase']


def set_salt():
    """Set the salt for encryption and decryption."""

    salt = os.environ.get('PEGLEG_SALT')
    if not salt:
        raise exceptions.SaltNotFoundException()
    elif len(salt) < GLOBAL_CONTEXT['salt_min_length']:
        raise exceptions.SaltInsufficientLengthException()

    GLOBAL_CONTEXT['salt'] = salt.encode()


def get_salt():
    """Get the salt for encryption and decryption."""
    return GLOBAL_CONTEXT['salt']


def set_global_enc_keys(site_name):
    """Get the global salt and passphrase for encryption."""
    GLOBAL_CONTEXT['global_passphrase'], GLOBAL_CONTEXT['global_salt'] = \
        secrets.get_global_creds(site_name)


def get_global_passphrase():
    """Get the global passphrase for encryption and decryption."""
    return GLOBAL_CONTEXT['global_passphrase']


def get_global_salt():
    """Get the global salt for encryption and decryption."""
    return GLOBAL_CONTEXT['global_salt']


def set_decrypt_repos(decrypt_repos=False):
    GLOBAL_CONTEXT['decrypt_repos'] = decrypt_repos


def get_decrypt_repos():
    return GLOBAL_CONTEXT['decrypt_repos']
