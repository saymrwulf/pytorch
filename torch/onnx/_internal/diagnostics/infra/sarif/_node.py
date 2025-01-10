# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import List, Optional

from torch.onnx._internal.diagnostics.infra.sarif import (
    _location,
    _message,
    _node,
    _property_bag,
)


@dataclasses.dataclass
class Node(object):
    """Represents a node in a graph."""

    id: str = dataclasses.field(metadata={"schema_property_name": "id"})
    children: Optional[list[_node.Node]] = dataclasses.field(
        default=None, metadata={"schema_property_name": "children"}
    )
    label: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "label"}
    )
    location: Optional[_location.Location] = dataclasses.field(
        default=None, metadata={"schema_property_name": "location"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )


# flake8: noqa
