import zipfile
import io
import os
from datetime import datetime
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox

# Avvia Tkinter
root = tk.Tk()
root.withdraw()

# Pop-up iniziale per guidare l'utente
messagebox.showinfo(
    "Istruzioni",
    "Assicurati che il file 'parole_chiave.txt' si trovi nella stessa cartella dell'eseguibile.\n"
    "In questo file puoi scrivere le parole chiave (una per riga) che il programma userà per identificare i PDF della tredicesima."
    "Una volta fornito il file .zip iniziale, verrà prodotto un file .zip che escluderà tutti i pdf che non identificati come 13esima"
)

# Finestra per scegliere lo ZIP di origine
INPUT_ZIP = filedialog.askopenfilename(
    title="Seleziona lo ZIP di origine",
    filetypes=[("File ZIP", "*.zip")]
)

if not INPUT_ZIP:
    messagebox.showerror("Errore", "Nessun file ZIP di origine selezionato.")
    exit(1)

# Finestra per scegliere dove salvare lo ZIP di destinazione
OUTPUT_ZIP = filedialog.asksaveasfilename(
    title="Salva lo ZIP filtrato come",
    defaultextension=".zip",
    filetypes=[("File ZIP", "*.zip")]
)

if not OUTPUT_ZIP:
    messagebox.showerror("Errore", "Nessun file ZIP di destinazione selezionato.")
    exit(1)

# Lettura parole chiave da file esterno
keywords_file = os.path.join(os.path.dirname(__file__), "parole_chiave.txt")
if not os.path.exists(keywords_file):
    messagebox.showerror(
        "Errore",
        f"File {keywords_file} non trovato.\nCrea 'parole_chiave.txt' con una parola chiave per riga."
    )
    exit(1)

with open(keywords_file, "r", encoding="utf-8") as f:
    SEARCH_TERMS = [line.strip().lower() for line in f if line.strip()]

if not SEARCH_TERMS:
    messagebox.showerror("Errore", "Il file 'parole_chiave.txt' è vuoto. Inserisci almeno una parola chiave.")
    exit(1)

# Genera nome log con data e ora
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"log_filtraggio_{timestamp}.txt"
log_path = os.path.join(os.path.dirname(INPUT_ZIP), log_filename)

# Elaborazione ZIP
with zipfile.ZipFile(INPUT_ZIP, 'r') as zin, zipfile.ZipFile(OUTPUT_ZIP, 'w') as zout, open(log_path, "w", encoding="utf-8") as log:
    for filename in zin.namelist():
        if not filename.lower().endswith(".pdf"):
            continue

        pdf_bytes = zin.read(filename)
        pdf_stream = io.BytesIO(pdf_bytes)

        try:
            reader = PdfReader(pdf_stream)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            text_lower = text.lower()
            found_terms = [term for term in SEARCH_TERMS if term in text_lower]

            if found_terms:
                zout.writestr(filename, pdf_bytes)
                log.write(f"{filename} → è una tredicesima (trovato: {', '.join(found_terms)})\n")
            else:
                log.write(f"{filename} → cedolino normale\n")

        except Exception as e:
            log.write(f"{filename} → errore nella lettura ({e})\n")

# Pop-up finale con conferma
messagebox.showinfo(
    "Operazione completata",
    f"Filtraggio terminato.\nLog scritto in:\n{log_path}"
)
