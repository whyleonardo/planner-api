from typing import Dict, List, Tuple
from sqlite3 import Connection


class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_infos: Dict) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
              INSERT INTO links
                  (id, trip_id, link)
              VALUES
                  (?, ?, ?)
            """,
            (link_infos["id"], link_infos["trip_id"], link_infos["link"]),
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id):
        cursor = self.__conn.cursor()
        cursor.execute("""SELECT * FROM links WHERE trip_id = ?""", (trip_id,))
        trip = cursor.fetchall()
        return trip
