from __future__ import annotations

from enum import Enum
from typing import Any, Optional, Type, TypeVar

from sqlalchemy import Integer
from sqlalchemy.types import TypeDecorator

# Generic type var so the type checker knows which Enum subclass we’re dealing with
E = TypeVar("E", bound=Enum)


class EnumType(TypeDecorator):
    """
    SQLAlchemy type decorator that stores an :class:`enum.Enum` **as an INTEGER**
    in the database while exposing the original Enum instance in Python code.

    Parameters
    ----------
    enum_class : Type[E]
        The Enum subclass this column should serialize / deserialize.

    Examples
    --------
    >>> from enum import Enum
    >>> from sqlalchemy import Column
    >>>
    >>> class Status(Enum):
    ...     ACTIVE = 1
    ...     SUSPENDED = 2
    ...
    >>> status = Column(EnumType(enum_class=Status), nullable=False, default=Status.ACTIVE)

    Notes
    -----
    * `impl` is set to :class:`sqlalchemy.Integer` so the actual column type on the DB
      side is a plain INT.
    * `cache_ok = True` tells SQLAlchemy it’s safe to cache this type object.
    """

    impl = Integer
    cache_ok = True

    # ------------------------------------------------------------------ #
    # Construction                                                       #
    # ------------------------------------------------------------------ #
    def __init__(self, *, enum_class: Type[E], **kwargs: Any) -> None:
        """
        Parameters
        ----------
        enum_class : Type[E]
            Enum class to bind.
        **kwargs
            Forwarded to the TypeDecorator base class.

        Raises
        ------
        TypeError
            If *enum_class* is not a subclass of :class:`enum.Enum`.
        """
        if not (isinstance(enum_class, type) and issubclass(enum_class, Enum)):
            raise TypeError("enum_class must be a subclass of enum.Enum")
        self.enum_class: Type[E] = enum_class
        super().__init__(**kwargs)

    # ------------------------------------------------------------------ #
    # Bind parameter (Python ➜ DB)                                       #
    # ------------------------------------------------------------------ #
    def process_bind_param(self, value: Optional[E], dialect) -> Optional[int]:  # type: ignore[override]
        """
        Convert an Enum value into the integer that will be written to the DB.

        SQLAlchemy calls this right before an INSERT / UPDATE.

        Raises
        ------
        TypeError
            If *value* is not ``None`` and not an instance of *enum_class*.
        """
        if value is None:
            return None
        if not isinstance(value, self.enum_class):
            raise TypeError(f"Expected {self.enum_class.__name__}, got {type(value).__name__}")
        return int(value.value)

    # ------------------------------------------------------------------ #
    # Result processing (DB ➜ Python)                                    #
    # ------------------------------------------------------------------ #
    def process_result_value(self, value: Optional[int], dialect) -> Optional[E]:  # type: ignore[override]
        """
        Convert an integer fetched from the DB back into an Enum instance.

        SQLAlchemy calls this after a SELECT.

        Raises
        ------
        TypeError
            If *value* is not ``None`` and not an ``int``.
        ValueError
            If *value* is an int but not a valid member of *enum_class*.
        """
        if value is None:
            return None
        if not isinstance(value, int):
            raise TypeError(f"Expected int from database, got {type(value).__name__}")
        try:
            return self.enum_class(value)  # type: ignore[return-value]
        except ValueError as exc:
            raise ValueError(
                f"{value!r} is not a valid value for {self.enum_class.__name__}"
            ) from exc

    # ------------------------------------------------------------------ #
    # Convenience: nice repr for debugging                               #
    # ------------------------------------------------------------------ #
    def __repr__(self) -> str:  # pragma: no cover
        return f"EnumType({self.enum_class.__name__})"
