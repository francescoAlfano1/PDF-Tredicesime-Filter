📘 PDF Payslip Filter (Filtro Tredicesime)
Utility desktop per filtrare cedolini PDF all’interno di archivi ZIP
📌 Descrizione del progetto
PDF Payslip Filter è un’applicazione desktop standalone (Windows) sviluppata in Python 3 che permette di filtrare automaticamente file PDF contenuti in un archivio ZIP, identificando quelli relativi alla tredicesima mensilità tramite un sistema di parole chiave configurabile dall’utente.

Il programma:

analizza ogni PDF senza estrarlo su disco
cerca parole chiave definite dall’utente
crea un nuovo ZIP contenente solo i PDF identificati
genera un file di log dettagliato con l’esito dell’analisi

È pensato per utenti non tecnici, in particolare per contesti HR / amministrazione del personale che gestiscono grandi volumi di cedolini.

🧰 Tecnologie utilizzate
Python 3

Librerie:

PyPDF2 – estrazione testo dai PDF

tkinter – interfaccia grafica (GUI)

zipfile – gestione archivi ZIP

io, os, datetime – utilità standard

🎯 Funzionalità principali
Interfaccia grafica semplice e guidata (nessuna riga di comando)

Selezione dei file tramite finestre di dialogo

Parsing PDF in memoria, senza estrazione su disco

Filtraggio basato su parole chiave personalizzabili

Generazione automatica di un file di log con timestamp

Gestione errori PDF corrotti o non leggibili

Nessuna installazione di Python richiesta (versione .exe disponibile)

📂 Struttura dei file
Nella stessa cartella dell’eseguibile devono essere presenti:

Codice
ScriptFiltraTredicesima.exe
parole_chiave.txt
Il file parole_chiave.txt contiene una parola chiave per riga, ad esempio:

Codice
tredicesima
mens.supplementare
🚀 Come utilizzare l’applicazione
Avvia ScriptFiltraTredicesima.exe.

Compare un messaggio introduttivo con le istruzioni.

Seleziona:

lo ZIP di origine contenente i PDF

il nome e la posizione dello ZIP filtrato da generare

Il programma analizza ogni PDF e crea:

un nuovo ZIP con i soli PDF che contengono almeno una parola chiave

un file di log nella stessa cartella dello ZIP di origine

📄 Output generati
🔹 Archivio ZIP filtrato
Contiene solo i PDF identificati come “tredicesima”.

🔹 File di log
Nome esempio:

Codice
log_filtraggio_2025-12-17_12-21-30.txt
Per ogni PDF indica:

“è una tredicesima (trovato: …)” → se contiene parole chiave

“cedolino normale” → se non contiene parole chiave

“errore nella lettura” → se il PDF non è stato processato correttamente

📝 Note importanti
La ricerca è case-insensitive.

Le parole chiave possono essere modificate liberamente senza ricompilare l’applicazione.

Ogni esecuzione genera un nuovo log, evitando sovrascritture.

Il programma non modifica i PDF originali.

👤 Autore
Francesco Alfano  
Data progetto: 17/12/2025
