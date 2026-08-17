# design-and-ux

Skill di design e UX: direzione artistica, sistemi visivi, tipografia, layout, comportamento responsive, accessibilità — il lavoro sull'interfaccia, non sui contenuti o sul codice in generale.

| Skill | Cosa fa |
|---|---|
| [art-direction](art-direction/) | 21 comandi di design: costruire una direzione visiva, criticare, rifinire, rendere più audace o più sobria un'interfaccia. Derivata da [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0). |
| [responsive](responsive/) | Fa funzionare l'interfaccia a ogni larghezza da 320px in su, e lo verifica contro un gate pass/fail. Esecuzione e verifica, non redesign. |

## Come si dividono il lavoro

Si sfiorano su un punto solo, ed è utile tenerlo chiaro:

- **`art-direction` → comando `adapt`** decide *cosa deve diventare* l'esperienza in un altro contesto: se su mobile serve una navigazione diversa, meno contenuto, un ordine di priorità diverso. È una decisione di design.
- **`responsive`** prende il design così com'è e lo fa reggere davvero a ogni larghezza: overflow, reflow, target tattili, tipografia fluida, safe area. È esecuzione e verifica, e non tocca l'identità visiva.

Se il layout è giusto ma si rompe sul telefono, serve `responsive`. Se il layout è sbagliato per il telefono, serve `adapt`.

---

Aggiungi qui le skill nel formato `skills/design-and-ux/<nome-skill>/SKILL.md` (vedi `skills/_template/SKILL.md`).
