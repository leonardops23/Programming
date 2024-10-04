from database import connect

class TaskRepository:
    def add_task(self, user_id, title, priority, due_date):
        """Adds a new task to the database."""
        conn = connect()
        c = conn.cursor()
        c.execute("INSERT INTO tasks (user_id, title, priority, due_date, status) VALUES (?, ?, ?, ?, ?)", 
                  (user_id, title, priority, due_date, 'incomplete'))
        conn.commit()
        conn.close()

    def get_tasks(self, user_id, filter_by=None):
        """Fetches tasks for a user, optionally filtered by priority, status, or due date."""
        conn = connect()
        c = conn.cursor()
        if filter_by:
            c.execute(f"SELECT * FROM tasks WHERE user_id = ? AND {filter_by[0]} = ?", (user_id, filter_by[1]))
        else:
            c.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        tasks = c.fetchall()
        conn.close()
        return tasks

    def update_task_status(self, task_id, status):
        """Updates the status of a task (complete/incomplete)."""
        conn = connect()
        c = conn.cursor()
        c.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        """Deletes a task from the database."""
        conn = connect()
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
