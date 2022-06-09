import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="rursus",
   user="rursus",
   password="abc123"
)

# read_dict: returns the list of all dictionary entries:
#   argument: C - the database connection.
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# add_word: add a new word and its translation to the dictionary
#   arguments: C           - the database connection.
#              word        - the dictionary word to be added
#              translation - the translation of the word
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# delete_word: deletes an entry identified by an ID
#   arguments: C  - the database connection.
#              ID - the identification of the entry
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

# save_dict: saves the database by committing the changes
#   arguments: C  - the database connection.
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

print("""Hello and welcome to the dictionary! Available commands:
  add    - add a word and a translation
  delete - delete a word
  list   - list the entire dictionary
  quit   - save the dictionary and quit
""")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        for i, wd, trans in read_dict(conn):
            print(f"{i}: {wd} - {trans}")
    elif cmd == "add":
        word = input("  Word: ")
        trans = input("  Translation: ")
        add_word(conn, word, trans)
        print(f"  Added word {word}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print("  Deleted word number {ID}")
    elif cmd == "quit":
        save_dict(conn)
        print("  Database saved! Good bye!")
        exit()
