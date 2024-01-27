from uuid import uuid4


class Object:
    def __init__(self, id: str = uuid4()) -> None:
        self._id = id

    def __str__(self) -> str:
        return self._id

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Object):
            return False
        return self._id == __value.id

    def __hash__(self) -> int:
        return hash(self._id)

    @property
    def id(self) -> str:
        return self._id
