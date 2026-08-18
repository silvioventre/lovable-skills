# deployment

Andare live e ospitare: pubblicazione, controllo degli accessi al sito pubblicato, hosting fuori da Lovable Cloud.

| Skill | Cosa fa |
|---|---|
| [ship](ship/) | Preflight prima di pubblicare, la distinzione tra project access e website access, verifica sul sito live, ripubblicazione. |
| [deploy-external](deploy-external/) | Se e cosa spostare fuori da Lovable Cloud, cosa diventa responsabilità tua, cosa migra da solo e cosa a mano, requisiti di build e Docker. |

## Come si dividono il lavoro

- **`ship`** = pubblicare *su* Lovable Cloud e controllarne l'accesso.
- **`deploy-external`** = far girare frontend o backend *altrove*.

Entrambe rimandano a `secure` per il gate di sicurezza invece di duplicarlo.

Aggiungi qui le skill nel formato `skills/deployment/<nome-skill>/SKILL.md` (vedi `skills/_template/SKILL.md`).
