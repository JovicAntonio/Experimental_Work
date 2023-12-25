import psycopg2
from psycopg2 import sql

def reload_cache(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT pg_reload_conf();")
    conn.commit()

def terminate_backend_cache_purge(conn):
    cursor = conn.cursor()
    cursor.execute("""
            SELECT pg_stat_reset();
        """)
    conn.commit()

def cache_purge(choice):
    try:
        conn = psycopg2.connect(
            dbname = "postgres",
            user = "pgsqladmin",
            password = "pgsqladminpass",
            host = "127.0.0.0",
            port = "5432",
        )
        if choice == 1:
            reload_cache(conn)
        elif choice == 2:
            terminate_backend_cache_purge(conn)
        print("Cache cleared successfully!")

    except psycopg2.Error as e:
        print(f"Error: {e}")


    conn.close()
