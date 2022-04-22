from typing import Optional


class Staff:
    def __init__(self):
        self.directors: Optional[list[str]] = None
        self.actors: Optional[list[str]] = None
        self.producers: Optional[list[str]] = None
        self.dubbing_directors: Optional[list[str]] = None
        self.dubbing_actors: Optional[list[str]] = None
        self.screenwriters: Optional[list[str]] = None
        self.operators: Optional[list[str]] = None
        self.composers: Optional[list[str]] = None
        self.artists: Optional[list[str]] = None
        self.editors: Optional[list[str]] = None

    @staticmethod
    def from_attrs(attrs: dict[str, list]) -> "Staff":
        model = Staff()
        model.directors = attrs.get("directors", [])
        model.actors = attrs.get("actors", [])
        model.producers = attrs.get("producers", [])
        model.dubbing_actors = attrs.get("dubbing_actors", [])
        model.dubbing_actors = attrs.get("dubbing_actors", [])
        model.screenwriters = attrs.get("screenwriters", [])
        model.operators = attrs.get("operators", [])
        model.composers = attrs.get("composers", [])
        model.artists = attrs.get("artists", [])
        model.editors = attrs.get("editors", [])
        return model
