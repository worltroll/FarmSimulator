import sqlite3


class DBManager:
    def __init__(self):
        self.con = sqlite3.connect('leaderboard.db')
        self.cur = self.con.cursor()
        self.init_db()
        self.tables = {
            0: 'easy',
            1: 'advanced',
            2: 'hard'
        }

    def init_db(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS easy (
            id    INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL
                          UNIQUE,
            name  TEXT    UNIQUE
                          NOT NULL,
            score INTEGER NOT NULL
                          DEFAULT (0) 
        )""")
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS advanced (
            id    INTEGER PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
            name  TEXT    NOT NULL
                          UNIQUE,
            score INTEGER NOT NULL
                          DEFAULT (0) 
        )""")
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS hard (
            id    INTEGER PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
            name  TEXT    UNIQUE
                          NOT NULL,
            score INTEGER NOT NULL
                          DEFAULT (0) 
        )""")
        self.con.commit()

    def cursor(self):
        return self.con.cursor()

    def connection(self):
        return self.con

    def get_leaderboard(self, i):
        leaderboard = self.con.cursor().execute(f"""
        SELECT name, score FROM {self.tables[i]}
        ORDER BY score ASC, name ASC""").fetchall()
        return leaderboard

    def add_new_score(self, i, name: str, score: int):
        table = self.tables[i]
        score_id = self.cur.execute(f"""
        SELECT id FROM {table}
        WHERE name = ?""", (name,)).fetchone()

        if score_id:
            self.cur.execute(f"""
            UPDATE {table}
            SET score = MAX(score, ?)
            WHERE id = ?""", (score, score_id[0]))
        else:
            self.cur.execute(f"""
            INSERT INTO {table}(name, score)
            VALUES(?, ?)""", (name, score))

        self.con.commit()

    def close(self):
        self.con.close()
