from models import Staff


class StaffTranslator:
    def to_document(self, model: Staff) -> dict[str, list[str]]:
        return {
            "directors": model.directors,
            "actors": model.actors,
            "producers": model.producers,
            "dubbing_directors": model.dubbing_directors,
            "dubbing_actors": model.dubbing_actors,
            "screenwriters": model.screenwriters,
            "operators": model.operators,
            "composers": model.composers,
            "artists": model.artists,
            "editors": model.editors,
        }

    def from_document(self, document: dict[str, list[str]]) -> Staff:
        staff = Staff()
        staff.directors = document.get("directors", [])
        staff.actors = document.get("actors", [])
        staff.producers = document.get("producers", [])
        staff.dubbing_directors = document.get("dubbing_directors", [])
        staff.dubbing_actors = document.get("dubbing_actors", [])
        staff.screenwriters = document.get("screenwriters", [])
        staff.operators = document.get("operators", [])
        staff.composers = document.get("composers", [])
        staff.artists = document.get("artists", [])
        staff.editors = document.get("editors", [])
        return staff
