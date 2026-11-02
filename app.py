import sqlite3

def init_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'segredo123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('diego', 'userpass')")
    conn.commit()
    return conn

# ❌ 1. IMPLEMENTAÇÃO VULNERÁVEL (Concatenação de string -> SQL Injection)
def login_vulneravel(conn, username, password):
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

# ✅ 2. IMPLEMENTAÇÃO SEGURA (Consulta Parametrizada / Prepared Statement)
def login_seguro(conn, username, password):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchone()

if __name__ == "__main__":
    db = init_db()
    
    # Entrada maliciosa típica de SQL Injection
    payload_ataque = "' OR '1'='1"
    
    print("--- Teste com Login Vulnerável ---")
    user = login_vulneravel(db, payload_ataque, "qualquer_senha")
    print("Resultado (Bypass bem-sucedido):", user)

    print("\n--- Teste com Login Seguro (Mitigado) ---")
    user = login_seguro(db, payload_ataque, "qualquer_senha")
    print("Resultado (Acesso bloqueado com sucesso):", user)
