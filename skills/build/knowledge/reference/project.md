# Writing project knowledge

Context for one app. Read before every message, so it should answer the questions that otherwise get answered by guessing.

## Generate it from the project, not from the user

For an app that already exists, do not interview the user for facts the code already contains. Read the project and draft from it — routes, tables, patterns, conventions actually in use — then ask only about what the code cannot tell you: who it is for, what the constraints are, which decisions were deliberate.

Where the request is to write knowledge for a grown project, the `plan` skill's investigation approach applies: split the reading into bounded questions, and draft from evidence rather than impression.

## What to include

**What the application does.** Two or three sentences. This is the single most valuable line in the file, because it is what makes every ambiguous request resolvable in context.

**Who uses it.** Primary and secondary users, and what each needs. If there are roles, name them here — role-blind edits to shared logic are a recurring source of bugs.

**Key database tables.** Names, main columns, relationships. Not the full schema — the shape needed to reason about a change without reading the migrations.

**Architecture decisions.** The choices you do not want revisited: where things live, how state is handled, how data is fetched, invariants like storing money as integer cents. Record the decision, not a lecture on why it is correct.

**Domain terminology.** What your words mean in this product. If "transaction" means an inventory movement rather than a payment, saying so once prevents a category of misunderstanding.

**Project-specific constraints.** Compliance requirements, integrations, things that must not change, external systems the app depends on.

**Design guidelines**, if the project has them and they are stable — palette, spacing, component library. If design is still moving, leave it out; stale design rules are worse than none.

**Links to references** that matter: API docs, internal tools.

## A shape that works

```
Project overview
This is a B2B inventory tool for restaurant managers tracking stock
across multiple locations.

Users
Primary: restaurant managers who need quick visibility into stock levels.
Secondary: staff logging inventory changes.

Key database tables
- inventory_items (id, name, category, quantity, unit, location_id)
- locations (id, name, workspace_id)
- transactions (id, item_id, quantity_change, type, created_at)

Architecture rules
- Store monetary values in cents as integers.
- Use optimistic updates for all mutations.
- Reusable components go in /components.

Domain terminology
- "Inventory item" is a tracked ingredient or product.
- "Transaction" is a change in inventory quantity, not a payment.

External references
- API documentation: https://docs.example.com/api
```

Short, specific, checkable. Every line either states a fact about this app or forecloses a decision.

## What to leave out

- **Anything true of every project.** That is workspace knowledge — see [workspace.md](workspace.md).
- **Task-specific procedures.** A release checklist or a review playbook is a skill, not knowledge.
- **The full schema.** It is in the project, and it changes.
- **Aspirations.** "We want to add real-time collaboration eventually" is not context, and it invites work nobody asked for.
- **Anything currently in flux.** A rule that is about to change is a rule that will be followed after it stops being true.

## Keep it current

The failure mode is not an incomplete file, it is a stale one. Knowledge describing a pattern the project abandoned actively pushes edits in the wrong direction, and it does so on every message.

Review it when the stack changes, when architecture changes, and when a rule stops being true. If the project moved and the knowledge did not, delete the wrong lines before adding new ones — see [fixing.md](fixing.md).
