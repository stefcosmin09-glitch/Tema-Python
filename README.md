# 🐍 Python Core Concepts — Tema 1

Proiect realizat în cadrul cursului **DevOps Online — IT School**.
Conține 8 exerciții practice de Python care acoperă conceptele de bază folosite în DevOps.

---

## 📁 Structura proiectului

| Fișier | Descriere |
|--------|-----------|
| `Ex1.py` | Tipuri de date — string, int, bool, None, list, set, dict, tuple |
| `Ex2.py` | Input utilizator + variabile de mediu cu `os.environ` |
| `Ex3.py` | Argumente din linia de comandă cu `sys.argv` + `os.mkdir` |
| `Ex4.py` | HTTP requests cu `requests` + citit/scris fișiere |
| `Ex5.py` | Parsare fișier log cu `enumerate()` + căutare string |
| `Ex6.py` | Monitorizare proces cu `subprocess` + `while True` |
| `Ex7.py` | Măsurare timp răspuns site web cu `time.time()` + funcții |
| `Ex8.py` | Explorare `subprocess` — comenzi sistem + coduri de eroare |

---

## 🚀 Cum rulezi

### Instalare dependențe
```bash
pip install requests
```

### Exercițiul 4 — HTTP requests
```bash
# Creează fișierul cu URL-uri
echo "https://httpstat.us/200" > urls.txt
echo "https://httpstat.us/404" >> urls.txt

python3 Ex4.py
# Rezultate salvate în success.txt și errors.txt
```

### Exercițiul 5 — Parser log-uri
```bash
# Creează fișierul de log
echo "ERROR: Database connection failed" > logs.txt
echo "INFO: Server started" >> logs.txt

python3 Ex5.py
```

### Exercițiul 6 — Monitor proces
```bash
python3 Ex6.py
# Monitorizează procesul my-script.sh și îl repornește dacă cade
```

### Exercițiul 7 — Monitor timp răspuns
```bash
python3 Ex7.py
# Afișează min, medie și max timp de răspuns pentru un URL
```

---

## 🛠️ Tehnologii folosite

- **Python 3**
- `requests` — HTTP calls
- `subprocess` — comenzi sistem
- `os`, `sys` — sistem de fișiere și argumente
- `time` — măsurare performanță
- `logging` — logging profesional

---

## 📚 Concepte acoperite

- Tipuri de date Python
- Citit/scris fișiere (`open`, `with`)
- HTTP requests și status codes
- Procesare fișiere de log
- Monitorizare procese sistem
- Funcții și module
- Argumente din linia de comandă

---

## 👤 Autor

**Gheorghe Ștefăniță Cosmin**  
Junior DevOps Engineer  
[GitHub](https://github.com/stefcosmin09-glitch)
