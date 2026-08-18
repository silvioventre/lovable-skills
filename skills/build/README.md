# build

Attività di costruzione: capire prima di scrivere, verificare dopo, e le capability che si aggiungono a un'app.

| Skill | Cosa fa |
|---|---|
| [plan](plan/) | Esplora il progetto, confronta approcci, scompone una richiesta vaga in incrementi verificabili. Non scrive codice. |
| [test](test/) | Instrada la verifica allo strumento giusto: browser testing, frontend test, chiamate dirette ed edge test. |
| [auth](auth/) | Decide se l'app ha davvero bisogno di un login, quale metodo, e lo configura. Distingue tre feature di identità che si somigliano. |
| [payments](payments/) | Ambienti test e live, ciclo di vita dell'abbonamento, go-live, e le operazioni irreversibili. |
| [knowledge](knowledge/) | Scrivere e mantenere le istruzioni persistenti: cosa va nel workspace, cosa nel progetto, e quando serve invece una skill. |
| [emails](emails/) | Dominio di invio, template auth e app, e le pratiche di deliverability che decidono se le mail arrivano in inbox. |
| [analyze](analyze/) | Analizza dati e genera file (PDF, CSV, grafici, diagrammi) senza toccare il codice, e costruisce partendo da quello che trova. |

## Ordine naturale

`plan` → `auth` → costruisci → `test` → `payments` → `secure` → `ship`.

`auth` prima di `payments`: un acquisto che non si può legare a un account è un acquisto che non puoi onorare. E `secure` prima di pubblicare, sempre: `auth` e `payments` stabiliscono *chi è* un utente e *cosa ha pagato*, non cosa gli è permesso fare.

Aggiungi qui le skill nel formato `skills/build/<nome-skill>/SKILL.md` (vedi `skills/_template/SKILL.md`).
