from database import connect


def add_note(title, content):
    conn = connect()
    c = conn.cursor()
    c.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()


def view_note():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()
    return notes


def update_note(id, title, content):
    conn = connect()
    c = conn.cursor()
    c.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, id))
    conn.commit()
    conn.close()
    print("Modified Note")
  

def delete_note(id):
    conn = connect()
    c = conn.cursor()
    c.execute(
        'DELETE FROM notes WHERE id = ?', (id)
    )
    conn.commit()
    conn.close()
