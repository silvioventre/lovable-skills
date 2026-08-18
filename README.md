# lovable-skills

A central library of reusable Lovable.dev skills.

Libreria centrale di **skill riutilizzabili per Lovable** ([docs.lovable.dev](https://docs.lovable.dev)).

Una skill è un playbook markdown a tema — nome, descrizione (il trigger che dice a Lovable *quando* usarla) e istruzioni — che Lovable carica su richiesta (via `/nome-skill`) o automaticamente quando una richiesta corrisponde alla descrizione. A differenza della *knowledge* (sempre in contesto), le skill si caricano solo quando servono, quindi qui dentro possiamo tenerne quante ne vogliamo senza appesantire ogni conversazione.

## Struttura

```
skills/
├── _template/                  # scheletro da copiare per una nuova skill
│   └── SKILL.md
├── code-quality/               # audit del codice, debito tecnico, dipendenze
│   └── lovable-codebase-audit-cleanup/
├── design-and-ux/              # direzione artistica, sistemi visivi, UI/UX
│   ├── art-direction/
│   └── responsive/
├── troubleshooting/            # errori, comportamenti sbagliati, loop di fix
│   └── debug/
├── security/                   # segreti, validazione, RLS, autenticazione
│   └── secure/
├── deployment/                 # pubblicazione, accessi, hosting esterno
│   ├── ship/
│   └── deploy-external/
└── build/                      # pianificare prima, verificare dopo
    ├── plan/
    └── test/

scripts/validate-skills.py      # valida ogni skill contro i limiti di Lovable
```

Le categorie nascono quando serve la prima skill che le abita: niente cartelle vuote in attesa. Sul tavolo per il futuro, senza impegno: SEO e AI search, contenuti ricorrenti e tono di voce, processi interni e workflow di team.

## Skill disponibili

| Skill | Categoria | Cosa fa |
|---|---|---|
| [lovable-codebase-audit-cleanup](skills/code-quality/lovable-codebase-audit-cleanup/) | code-quality | Audit in sola lettura del codice + pulizia a batch approvati: codice morto, dipendenze inutilizzate, duplicazioni, debito tecnico. |
| [art-direction](skills/design-and-ux/art-direction/) | design-and-ux | 21 comandi di design: costruire una direzione visiva, criticare, rifinire, rendere più audace o più sobria un'interfaccia. Opera derivata da [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0), adattata a Lovable. |
| [responsive](skills/design-and-ux/responsive/) | design-and-ux | Fa funzionare l'interfaccia a ogni larghezza da 320px in su e lo verifica contro un gate pass/fail: overflow, reflow, target tattili, zoom 400%, safe area. |
| [debug](skills/troubleshooting/debug/) | troubleshooting | Instrada il sintomo al playbook giusto — build, schermata bianca, comportamento sbagliato, backend, loop di fix — e corregge la causa radice, non il sintomo. |
| [secure](skills/security/secure/) | security | Instrada la questione di sicurezza al layer giusto (frontend, edge function, RLS, auth) e applica la regola che vale lì. Gate di 10 controlli prima di pubblicare. |
| [ship](skills/deployment/ship/) | deployment | Preflight prima di andare live, distinzione tra accesso al progetto e accesso al sito pubblicato, verifica sul live, ripubblicazione. |
| [deploy-external](skills/deployment/deploy-external/) | deployment | Se e cosa spostare fuori da Lovable Cloud: responsabilità che assumi, cosa migra a mano, requisiti di build, Docker. |
| [plan](skills/build/plan/) | build | Esplora il progetto, confronta approcci, scompone una richiesta vaga in incrementi verificabili. Delega l'indagine ai subagent e non scrive codice. |
| [test](skills/build/test/) | build | Instrada la verifica allo strumento giusto — browser testing, frontend test, chiamate dirette ed edge test — e distingue cosa vale la pena testare da cosa no. |

Ogni skill vive nella propria cartella dentro una categoria:

```
skills/<categoria>/<nome-skill>/
└── SKILL.md
    (+ eventuali file bundled: reference.md, template.md, ecc.)
```

Le categorie sono contenitori leggeri: quando emerge un'esigenza reale (un dominio specifico, un tipo di lavoro ricorrente) si aggiunge una cartella categoria senza toccare quelle esistenti.

## Creare una nuova skill

1. Copia `skills/_template/SKILL.md` in `skills/<categoria>/<nome-skill>/SKILL.md` (crea la categoria se non esiste ancora).
2. Compila i tre campi obbligatori:
   - **name**: identificativo breve e permanente, minuscolo, solo lettere/numeri/trattini (es. `launch-checklist`). Non cambia dopo la creazione — per rinominare bisogna ricreare la skill.
   - **description**: inizia con "Use when..." e descrivi trigger, scope e confini il più concretamente possibile. È il segnale principale che Lovable usa per decidere se caricare la skill.
   - **instructions**: il corpo markdown che Lovable segue una volta caricata la skill — step, vincoli, esempi, edge case, formato di output atteso.
3. Il nome della cartella deve coincidere con il nome della skill (kebab-case, niente trattini iniziali/finali o doppi).
4. Se servono riferimenti più lunghi, template o piccoli script, aggiungili come file bundled accanto a `SKILL.md` (max 1MB a file, 200 file / 10MB totali per skill).

## Importare le skill in Lovable

Da **Settings → Skills → Add → Import from GitHub**, incollando l'URL della sottocartella della singola skill (repo con più skill richiede l'import per sottocartella, non del repo intero):

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/<categoria>/<nome-skill>
```

Lovable scarica, valida e aggiunge la skill al workspace con nome, descrizione e file bundled intatti.

## Validare una skill

Prima di committare, o prima di importare in Lovable:

```bash
python3 scripts/validate-skills.py
```

Controlla ogni cartella che contiene un `SKILL.md` contro i vincoli reali di Lovable, così un errore di formato emerge qui e non al momento dell'import:

- frontmatter YAML presente, con `name` e `description`
- `name` uguale al nome della cartella, minuscolo, solo lettere/numeri e trattini singoli, max 64 caratteri
- `SKILL.md` entro i 100.000 caratteri
- ogni file bundled entro 1 MB, e per skill max 200 file / 10 MB totali
- tutti i link `.md` interni risolvono

Il frontmatter viene parsato con un parser YAML vero, non con una regex: Lovable lo legge come YAML, quindi tutto ciò che rompe il parser rompe anche l'import.

Gira automaticamente su ogni push e pull request via [GitHub Actions](.github/workflows/validate-skills.yml).

### La trappola dei due punti

In YAML un valore non quotato **non può contenere `: `** (due punti seguiti da spazio): il parser lo legge come una chiave annidata e l'import fallisce con `mapping values are not allowed in this context`. È l'errore più facile da introdurre scrivendo una `description`.

```yaml
# rotto
description: Use when auditing a page: metadata, headings, internal links.

# ok — riformulato senza due punti
description: Use when auditing a page for metadata, headings and internal links.

# ok — valore quotato
description: "Use when auditing a page: metadata, headings, internal links."
```

Stesso discorso per ` #` (avvia un commento) e per un valore che inizia con `&`, `*`, `!`, `%` o `` ` ``. Nel dubbio, quota tutto il valore.

## Linee guida rapide

- Una skill, un compito: se copre troppo, dividila.
- Metti esplicitamente cosa **non** fare, non solo cosa fare.
- Regole valide per ogni messaggio → *knowledge* del workspace, non skill.
- Istruzioni concrete e concise battono sempre le linee guida astratte.
- Fai manutenzione: rimuovi skill obsolete o con istruzioni non più valide.

Riferimento completo: [Define reusable instructions with skills](https://docs.lovable.dev/features/skills) (Lovable docs).
