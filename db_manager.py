import sqlite3

class DBManager:
    def __init__(self):
        self.con = sqlite3.connect('databases/leaderboard.db')
        self.cur = self.con.cursor()
        self.init_db()

    def init_db(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS score (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                score INTEGER DEFAULT 0
            )
        """)
        self.con.commit()

    def cursor(self):
        return self.con.cursor()

    def connection(self):
        return self.con

    def get_leaderboard(self):
        leaderboard = self.con.cursor().execute("""
        SELECT name, score FROM score
        ORDER BY score DESC, name DESC""").fetchall()
        return leaderboard

    def add_new_score(self, name: str, score: int):
        score_id = self.cur.execute("""
        SELECT id FROM score
        WHERE name = ?""", (name,)).fetchone()

        if score_id:
            self.cur.execute("""
            UPDATE score
            SET score = ?
            WHERE id = ?""", (score, score_id[0]))
        else:
            self.cur.execute("""
            INSERT INTO score(name, score)
            VALUES(?, ?)""", (name, score))

        self.con.commit()