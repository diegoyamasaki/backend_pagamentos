from infra.database.conection import Session_Local


class Db:
    def get_db(self):
        return Session_Local()
