# PDF Payslip Filter – Filtro Tredicesime

Utility desktop Python che automatizza il filtraggio di **cedolini paga in formato PDF** contenuti in un archivio ZIP.

## 🛠️ Tecnologie
- Python 3
- `PyPDF2` (lettura PDF)
- `tkinter` (interfaccia grafica)
- `zipfile` (gestione archivi)

## 📋 Descrizione
Il programma identifica i documenti relativi alla tredicesima mensilità tramite un sistema di parole chiave configurabile dall'utente, produce un nuovo archivio ZIP contenente solo i PDF identificati, e genera un file di log con l'esito dell'analisi di ciascun documento.

## ✅ Funzionalità principali
- Interfaccia grafica guidata (selezione file tramite finestre di dialogo)
- Lettura e parsing del testo da PDF multipli senza estrazione su disco
- Filtraggio basato su parole chiave personalizzabili via file esterno (`parole_chiave.txt`)
- Generazione automatica di un log con timestamp per la tracciabilità
- Gestione degli errori per PDF corrotti o illeggibili

## 💡 Punti di forza
- Orientato all'utente finale non tecnico (nessuna riga di comando)
- Configurabile senza modificare il codice sorgente
- Gestione degli errori per PDF corrotti o illeggibili

## 🏢 Contesto d'uso
Ambito HR / amministrazione del personale — gestione massiva di archivi documentali.
