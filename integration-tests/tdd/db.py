import sqlite3
from inline_tdd import itestdd

# Initialize in-memory SQLite database
conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Create table and insert seed data
cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT UNIQUE
    )
""")
cur.executemany(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    [
        ("Alice", 30, "alice@example.com"),
        ("Bob", 25, "bob@example.com"),
        ("Charlie", 35, "charlie@example.com"),
    ],
)
conn.commit()

# ============================================================
# Read-only queries (run first, seed data is unchanged)
# ============================================================

def count_users():
    itestdd().check_eq(n, 3)
    n = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return n


def get_user_by_id(uid):
    itestdd().given(uid, 1).check_eq(row["name"], "Alice")
    itestdd().given(uid, 2).check_eq(row["name"], "Bob")
    row = cur.execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone()
    return row


def get_user_names():
    itestdd().check_eq(names, ["Alice", "Bob", "Charlie"])
    names = [r["name"] for r in cur.execute("SELECT name FROM users ORDER BY id")]
    return names


def get_users_older_than(age):
    itestdd().given(age, 28).check_eq(names, ["Alice", "Charlie"])
    itestdd().given(age, 100).check_eq(names, [])
    names = [
        r["name"]
        for r in cur.execute("SELECT name FROM users WHERE age > ? ORDER BY name", (age,))
    ]
    return names


def search_users(keyword):
    itestdd().given(keyword, "li").check_eq(names, ["Alice", "Charlie"])
    itestdd().given(keyword, "bob").check_eq(names, ["Bob"])
    itestdd().given(keyword, "zzz").check_eq(names, [])
    names = [
        r["name"]
        for r in cur.execute(
            "SELECT name FROM users WHERE LOWER(name) LIKE LOWER(?) ORDER BY name",
            (f"%{keyword}%",),
        )
    ]
    return names


def get_avg_age():
    itestdd().check_eq(avg, 30.0)
    avg = cur.execute("SELECT AVG(age) FROM users").fetchone()[0]
    return avg


def get_user_emails():
    itestdd().check_eq(emails, ["alice@example.com", "bob@example.com", "charlie@example.com"])
    emails = [
        r["email"]
        for r in cur.execute("SELECT email FROM users ORDER BY id")
    ]
    return emails


def get_max_age():
    itestdd().check_eq(result, 35)
    result = cur.execute("SELECT MAX(age) FROM users").fetchone()[0]
    return result


def get_min_age():
    itestdd().check_eq(result, 25)
    result = cur.execute("SELECT MIN(age) FROM users").fetchone()[0]
    return result


def get_user_count_by_age_range(lo, hi):
    itestdd().given(lo, 25).given(hi, 30).check_eq(n, 2)
    itestdd().given(lo, 0).given(hi, 20).check_eq(n, 0)
    n = cur.execute("SELECT COUNT(*) FROM users WHERE age BETWEEN ? AND ?", (lo, hi)).fetchone()[0]
    return n


def user_exists(email):
    itestdd().given(email, "alice@example.com").check_true(found)
    itestdd().given(email, "nobody@example.com").check_false(found)
    found = cur.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,)).fetchone()[0] > 0
    return found


def get_names_upper():
    itestdd().check_eq(names, ["ALICE", "BOB", "CHARLIE"])
    names = [r[0] for r in cur.execute("SELECT UPPER(name) FROM users ORDER BY id")]
    return names


def get_name_lengths():
    itestdd().check_eq(lens, [5, 3, 7])
    lens = [r[0] for r in cur.execute("SELECT LENGTH(name) FROM users ORDER BY id")]
    return lens


# ============================================================
# Write operations (these modify the DB; order matters)
# ============================================================

# TDD pattern for writes: itestdd checks the variable assigned by the
# immediately-next statement.  We combine the SQL call and the value
# extraction into a single assignment so the checked variable exists.

def insert_user(name, age, email):
    itestdd().given(name, "Dave").given(age, 40).given(email, "dave@example.com").check_eq(rowcount, 1)
    rowcount = cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email)).rowcount
    conn.commit()
    return rowcount


def verify_insert(email):
    itestdd().given(email, "dave@example.com").check_eq(row["name"], "Dave")
    row = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    return row


def count_after_insert():
    itestdd().check_eq(n, 4)
    n = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return n


def update_user_age(uid, new_age):
    itestdd().given(uid, 1).given(new_age, 31).check_eq(rowcount, 1)
    rowcount = cur.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, uid)).rowcount
    conn.commit()
    return rowcount


def verify_update(uid):
    itestdd().given(uid, 1).check_eq(row["age"], 31)
    row = cur.execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone()
    return row


def delete_nonexistent(uid):
    itestdd().given(uid, 999).check_eq(rowcount, 0)
    rowcount = cur.execute("DELETE FROM users WHERE id = ?", (uid,)).rowcount
    return rowcount


def delete_user(uid):
    itestdd().given(uid, 4).check_eq(rowcount, 1)
    rowcount = cur.execute("DELETE FROM users WHERE id = ?", (uid,)).rowcount
    conn.commit()
    return rowcount


def count_after_delete():
    itestdd().check_eq(n, 3)
    n = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return n
