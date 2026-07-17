# lovable-skills

Libreria centrale di **skill riutilizzabili per Lovable** ([docs.lovable.dev](https://docs.lovable.dev)).

Una skill è un playbook markdown a tema — nome, descrizione (il trigger che dice a Lovable *quando* usarla) e istruzioni — che Lovable carica su richiesta (via `/nome-skill`) o automaticamente quando una richiesta corrisponde alla descrizione. A differenza della *knowledge* (sempre in contesto), le skill si caricano solo quando servono, quindi qui dentro possiamo tenerne quante ne vogliamo senza appesantire ogni conversazione.

## Struttura

```
skills/
├── _template/                  # scheletro da copiare per una nuova skill
│   └── SKILL.md
├── launch-and-quality/         # checklist di lancio, QA, review pre-rilascio
├── content-and-copy/           # contenuti ricorrenti, tono di voce, formati
├── review-playbooks/           # audit e review (accessibilità, SEO, landing, ecc.)
├── workflows-and-processes/    # processi interni, onboarding, handoff, routine di team
└── code-quality/               # audit del codice, debito tecnico, pulizia dipendenze
    └── lovable-codebase-audit-cleanup/
        └── SKILL.md
```

Ogni skill vive nella propria cartella dentro una categoria:

```
skills/<categoria>/<nome-skill>/
└── SKILL.md
    (+ eventuali file bundled: reference.md, template.md, ecc.)
```

Le categorie sono un punto di partenza generico: quando emergono esigenze reali (es. un dominio specifico: e-commerce, SaaS, siti vetrina) si aggiungono nuove cartelle categoria senza toccare quelle esistenti.

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

## Linee guida rapide

- Una skill, un compito: se copre troppo, dividila.
- Metti esplicitamente cosa **non** fare, non solo cosa fare.
- Regole valide per ogni messaggio → *knowledge* del workspace, non skill.
- Istruzioni concrete e concise battono sempre le linee guida astratte.
- Fai manutenzione: rimuovi skill obsolete o con istruzioni non più valide.

Riferimento completo: [Define reusable instructions with skills](https://docs.lovable.dev/features/skills) (Lovable docs).
