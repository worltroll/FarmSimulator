import sqlite3

class DBManager:
    def __init__(self):
        self.con = sqlite3.connect('databases/leaderboard.db')

    def cursor(self):
        return self.con.cursor()

    def connection(self):
        return self.con

    def get_leaderboard(self):
        leaderboard = self.con.cursor().execute("""
        SELECT name, score FROM score
        ORDER BY score DESC, name DESC""").fetchall()
        return leaderboard