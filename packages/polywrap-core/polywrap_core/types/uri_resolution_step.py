"""This module contains the uri resolution step interface."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional

from polywrap_result import Result

from .uri import Uri


@dataclass(slots=True, kw_only=True)
class IUriResolutionStep:
    """Represents a single step in the resolution of a uri.

    Attributes:
        source_uri: The uri that was resolved.
        result: The result of the resolution.
        description: A description of the resolution step.
        sub_history: A list of sub steps that were taken to resolve the uri.
    """

    source_uri: Uri
    result: Result[Any]
    description: Optional[str] = None
    sub_history: Optional[List["IUriResolutionStep"]] = None
