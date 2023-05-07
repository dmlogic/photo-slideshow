import sqlite3


class Lookup:

    database = None
    filepath = None

    def __init__(self, dbpath, photopath):
        self.database = sqlite3.connect(dbpath)
        self.filepath = photopath

    def random_image(self):
        query = self.database.cursor()
        sql = '''SELECT a.id as album_id,
                        p.google_id,
                        a.title,
                        p.created_at
                    FROM photos p
                    JOIN albums a ON a.id = p.album_id
                    ORDER BY RANDOM()
                    LIMIT 1'''
        row = query.execute(sql).fetchone()
        return self.create_data(row)

    def create_data(self, raw):
        return {
            'path': self.filepath+'bluebells.jpg',
            # 'path': self.filepath+str(raw[0])+'/'+str(raw[1])+'.jpg',
            'title': raw[2],
            'date': raw[3]
        }
