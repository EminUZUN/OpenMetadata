#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Custom types' registry for easy access
without having an import mess
"""
import sqlalchemy

from metadata.orm_profiler.orm.types.hex_byte_string import HexByteString
from metadata.orm_profiler.orm.types.uuid import UUIDString
from metadata.orm_profiler.registry import TypeRegistry


class CustomTypes(TypeRegistry):
    BYTES = HexByteString
    UUID = UUIDString


# Numeric types in SQLAlchemy
SQLALCHEMY_NUMERIC = {
    sqlalchemy.Integer,
    sqlalchemy.INTEGER,
    sqlalchemy.SMALLINT,
    sqlalchemy.INT,
    sqlalchemy.BIGINT,
    sqlalchemy.FLOAT,
    sqlalchemy.DECIMAL,
    sqlalchemy.NUMERIC,
}

# Sometimes we want to skip types for computing metrics.
# If the type is NULL, then we won't run the metric execution
# in the profiler.
# Note that not mapped types are set to NULL by default.
NOT_COMPUTE = {
    sqlalchemy.types.NullType,
    sqlalchemy.ARRAY,
}