# When knowledge is not working

The usual complaints: *"it keeps using the wrong library"*, *"I've told it three times"*, *"it forgot the schema"*. Diagnose before adding text — the reflex to write more is what produces knowledge that works even less well.

## Diagnose first

Work through these in order. The first match is usually the answer.

**Is the rule actually written down?** Frequently it was said in chat several times and never added anywhere. A repeated instruction is a missing entry, and the fix is one line.

**Is it specific enough to check?** "Write clean code" cannot be followed because nothing distinguishes compliance from violation. "Never use `any` — use `unknown` and narrow it" can. Vague entries are not weak rules, they are non-rules occupying the character budget.

**Is it in the right place?** A rule about this app in workspace knowledge applies to unrelated projects. A rule that should be universal, written into one project, is absent from the rest.

**Does something contradict it?** Two entries pulling in different directions produce inconsistent behaviour that looks like the instruction being ignored. This happens most often after a stack change, when the new rule was added and the old one never removed.

**Is it stale?** Knowledge describing a pattern the project abandoned pushes edits toward the old pattern on every message. Wrong knowledge is worse than none — none produces a guess, wrong produces confident error.

**Is the file too long?** Approaching the 10,000-character limit, everything competes. Adding another paragraph to fix a rule that is being lost makes it more likely to be lost.

**Was it a long conversation?** Standing instructions are followed less consistently deep into a long session. If behaviour was correct early and drifted late, the knowledge is probably fine — restate the rule in the message, or start a fresh conversation for the next piece of work.

## Then fix it

**Delete before you add.** Almost every knowledge file that "isn't working" is too long and partly wrong. Removing stale and vague entries improves adherence more reliably than any addition, because it raises the share of the file that is real.

**Rewrite vague entries as checkable rules.** One line, stated as a rule, phrased so a diff either complies or does not.

**Add the negative form.** For behaviour that keeps recurring, saying what not to do stops it more reliably than describing the alternative. Both together is best: "Route API calls through a service layer. Do not call `fetch` directly from components."

**Move task-specific instructions out.** Anything that only matters for one kind of task belongs in a skill. This is the single biggest source of bloat, and moving it out helps the rules that remain.

**Consolidate.** The same rule expressed three ways in three places is three chances to conflict.

## For a rule that must never break

Knowledge is guidance, not enforcement, and it is explicitly not guaranteed in long conversations. Anything whose violation is expensive needs a mechanism as well:

- **A test**, if the rule is about behaviour. See the `test` skill.
- **A check in a skill**, if it belongs to a particular kind of task — a gate that runs at the right moment rather than a hope carried through every message.
- **A root-level `AGENTS.md`**, which is always read regardless of conversation length. For rules that must survive a long session, this is the more reliable home, and for a user already keeping such a file it is where the rule should go rather than being duplicated.

## Reviewing

Worth doing when the stack changes, when architecture changes, and when a rule stops being true. Read the whole file and ask of every line: *is this still true, is it specific, is it in the right place, and would I miss it if it were gone?*

Anything failing that last question is costing characters and attention for nothing. Delete it.
