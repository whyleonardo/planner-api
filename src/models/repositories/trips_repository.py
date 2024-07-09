from typing import Dict
from sqlite3 import Connection


class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_trip(self, trips__infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
              INSERT INTO trips
                  (id, destination, start_date, end_date, owner_name, owner_email)
              VALUES
                  (?, ?, ?, ?, ?, ?)    
            """,
            (
                trips__infos["id"],
                trips__infos["destination"],
                trips__infos["start_date"],
                trips__infos["end_date"],
                trips__infos["owner_name"],
                trips__infos["owner_email"],
            ),
        )
        self.__conn.commit()
