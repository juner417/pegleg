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

SCHEMA_STORAGE_POLICY_MISMATCH_FLAG = 'P001'
REPOS_MISSING_DIRECTORIES_FLAG = 'P003'
DECKHAND_DUPLICATE_SCHEMA = 'P004'
DECKHAND_RENDER_EXCEPTION = 'P005'
FILE_MISSING_YAML_DOCUMENT_HEADER = 'P006'
FILE_CONTAINS_INVALID_YAML = 'P007'
DOCUMENT_LAYER_MISMATCH = 'P008'
SECRET_NOT_ENCRYPTED_POLICY = 'P009'  # nosec (alexanderhughes)

ALL_CODES = (
    SCHEMA_STORAGE_POLICY_MISMATCH_FLAG,
    REPOS_MISSING_DIRECTORIES_FLAG,
    DECKHAND_DUPLICATE_SCHEMA,
    DECKHAND_RENDER_EXCEPTION,
    FILE_MISSING_YAML_DOCUMENT_HEADER,
    FILE_CONTAINS_INVALID_YAML,
    DOCUMENT_LAYER_MISMATCH,
    SECRET_NOT_ENCRYPTED_POLICY,
)
