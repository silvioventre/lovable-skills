---
name: lovable-codebase-audit-cleanup
description: Perform a two-phase codebase rationalization on a Lovable project — a comprehensive read-only audit to find dead code, unused code, obsolete dependencies, duplicated implementations, and maintainability risks, followed by a strictly-scoped, approval-gated cleanup of only the batches the user explicitly approves. Use this skill whenever the user asks to "audit the codebase," "find dead/unused code," "clean up the project," "reduce technical debt," "find unused dependencies," references an approved audit batch (e.g. "implement Batch 2"), or asks for a codebase health check, even if they don't use these exact words. Do not skip straight to editing code when this skill applies — always determine which phase (Audit or Cleanup) the request belongs to before acting.
---

# Lovable Codebase Audit & Cleanup

This skill governs two distinct, sequential phases of codebase rationalization. They must never be merged into a single pass. Determine which phase applies before doing anything else.

## Phase routing

1. **No prior audit exists, or the user asks to inspect/find/review issues** → run **Phase 1: Audit**.
2. **An audit report already exists and the user references an approved batch or finding IDs to implement** → run **Phase 2: Cleanup**.
3. **The user asks to "clean up" without a prior audit** → do not skip to editing. Run Phase 1 first, present the findings and the batch roadmap, and wait for explicit batch approval before touching any code.

Never combine phases in one response. Never modify code while still in Phase 1.

---

## Phase 1: Audit (read-only)

Use Plan mode (or the project's equivalent read-only/chat mode). Perform a comprehensive, read-only audit of the entire existing codebase to identify dead code, unused code, obsolete dependencies, duplicated implementations, and maintainability risks.

**Do not modify, delete, rename, move, or refactor any file during this phase.**

### Objective

Rationalize the codebase to make it as professional, maintainable, predictable, and technically robust as possible. Identify code that:

- Is no longer referenced or executed, or is unreachable.
- Is obsolete or superseded by a newer implementation.
- Duplicates existing functionality.
- Adds unnecessary complexity or creates maintenance risk.
- Could produce technical issues in future releases.
- Increases bundle size, build time, runtime overhead, or cognitive load without providing value.
- Is inconsistent with the architecture and conventions currently used by the project.

### Audit scope

Inspect the complete repository, including:

- Application routes and route registrations.
- Pages, layouts, components, hooks, utilities, services, providers, contexts, stores, reducers, actions, schemas, types, interfaces, constants, configuration files, tests, scripts, styles, assets, and public files.
- Frontend and backend code, if both are present.
- Supabase or Lovable Cloud integrations: migrations, Edge Functions, database clients, queries, RPC calls, storage usage, authentication logic, generated types.
- Package dependencies and dev dependencies.
- Build configuration, TypeScript configuration, linting configuration, environment-variable usage, import aliases, deployment configuration.
- Feature flags, role-based flows, experimental features, legacy implementations, commented-out code, temporary workarounds, stale TODOs.
- CSS classes, design tokens, stylesheets, images, icons, fonts, and other assets that may no longer be used.
- Tests, mocks, fixtures, and test utilities that no longer correspond to active functionality.

### Required analysis

**1. Dead and unreachable code** — files never imported/registered/referenced/executed; unused functions, methods, hooks, components, classes, constants, variables, exports, types, interfaces; unreachable branches; code after unconditional returns/throws/redirects; unreachable routes/screens; unused handlers, effects, subscriptions, listeners, callbacks; exports with no consumers.

**2. Obsolete and superseded implementations** — legacy components/modules replaced by newer versions; old API clients, state-management approaches, auth flows, data-fetching patterns; deprecated library APIs; compatibility code no longer required; temporary migrations/patches/fallbacks/workarounds that became permanent; old feature implementations left alongside the active one.

**3. Duplicate and redundant code** — components implementing substantially the same UI/behavior; utilities/helpers with overlapping responsibility; multiple sources of truth for the same data; repeated validation/formatting/mapping/transformation/permission/business logic; duplicate API calls or DB queries; multiple abstractions solving the same problem; redundant wrappers or pass-through components with no meaningful behavior. Do not assume similar-looking code should automatically be merged — explain whether consolidation would genuinely improve maintainability or create excessive coupling.

**4. Dependencies** — review all production and dev dependencies. For each potentially unused one: search direct imports; search indirect usage through configuration, plugins, scripts, generated code, CLI commands, build tooling, runtime loading; check if required by the framework/deployment environment; check if it's a peer or transitive requirement; state the evidence supporting removal. Also flag duplicate packages with overlapping capability, packages used only for trivial functionality that an existing project utility could cover, deprecated/abandoned/incompatible/heavy packages, dependencies imported globally but used in one isolated area, and obsolete `package.json` scripts. **Do not recommend removing a package solely because no direct import was found.**

**5. Imports and exports** — unused imports/exports; barrel files exposing obsolete modules; circular dependencies; deep imports bypassing intended public interfaces; inconsistent aliases/import paths; modules with excessive responsibility; dynamic imports that look unused but load at runtime.

**6. State, effects, and runtime behavior** — state written but never read; state read but never meaningfully changed; derived state duplicating source state; effects doing no useful work or with stale/incorrect dependencies; subscriptions/timers/observers/listeners/interceptors never cleaned up; duplicate network/DB requests; unneeded cache/invalidation layers; error-handling paths that silently swallow failures; code technically used but functionally ineffective.

**7. Types and schemas** — unused types, interfaces, enums, schemas, DTOs, generated definitions; multiple incompatible definitions for the same domain entity; overly broad types hiding obsolete properties; propagated-but-never-consumed properties; validation schemas no longer matching active forms/payloads/DB structures; type assertions or `any` usage concealing obsolete or broken code paths.

**8. Styling and assets** — unused CSS files, selectors, utility classes, design tokens, animations, fonts, icons, images, videos; duplicate style definitions; legacy theme values; inline styles replicating design-system capability; components bypassing current design tokens; assets referenced only by obsolete code. Be careful with dynamically constructed class names and runtime-loaded assets.

**9. Tests and tooling** — tests for features that no longer exist; tests that never run (excluded/misnamed); unused mocks/fixtures; duplicated test utilities; disabled tests, skipped suites, stale snapshots, obsolete test config; ineffective lint/format/build/CI rules; missing coverage around high-risk cleanup candidates.

**10. Security and technical-risk review** — old auth/authorization paths; client-side-only role checks; unused endpoints or Edge Functions; obsolete env vars or secret references; legacy storage buckets, DB functions, RPC calls, policies; debug logging that may expose sensitive data; old admin routes; hidden features still reachable via direct URL; unmaintained dependencies with known compatibility or security issues. **Never expose secret values in the audit output.**

### False-positive protection

Before classifying anything as dead or unused, explicitly check for: dynamic imports, lazy-loaded routes, reflection/metadata-driven registration, framework conventions, dependency injection, plugin registration, runtime string references, CSS class construction, environment-specific code, feature flags, role-based behavior, server-only or client-only execution, test-only usage, build-time usage, configuration-file usage, generated code, database triggers/policies/scheduled jobs/webhooks/external consumers, files imported outside the standard source directory, and public APIs that may be consumed externally.

**When usage cannot be proven either way, classify the item as "requires verification," never "safe to remove."**

### Evidence requirements

Every finding must include: file path; relevant symbol/export/dependency/route/asset/config entry; finding category; concrete evidence; the search or dependency path used to determine usage; confidence level (high/medium/low); removal risk (low/medium/high/critical); potential impact; recommended action; required validation before removal. Never write an unsupported statement like "this appears unused" without explaining why.

### Required output — Audit report

Return a structured report with these sections:

1. Executive summary
2. Current architecture overview
3. Critical technical or security risks
4. High-confidence dead-code candidates
5. Unused or questionable dependencies
6. Duplicate and redundant implementations
7. Obsolete architectural patterns
8. Unused routes, components, hooks, utilities, types, styles, assets
9. Runtime, state-management, and side-effect risks
10. Testing and tooling gaps
11. Items requiring manual verification
12. Recommended target architecture and conventions
13. Prioritized cleanup roadmap
14. Proposed validation and regression-test strategy

Include a findings table with columns: `ID | Category | File or dependency | Symbol or area | Evidence | Confidence | Removal risk | Recommended action | Required tests`.

### Cleanup roadmap (proposed by the audit, not executed yet)

Organize the proposed cleanup into small, reversible batches:

- **Batch 0** — establish a clean baseline and record existing failures.
- **Batch 1** — unused imports, local variables, trivial exports, obvious commented-out code.
- **Batch 2** — high-confidence unused files and assets.
- **Batch 3** — unused dependencies and obsolete scripts.
- **Batch 4** — duplicate utilities, hooks, components, types.
- **Batch 5** — obsolete routes, services, state, data flows, backend functions.
- **Batch 6** — architectural simplification and consistency improvements.
- **Batch 7** — final regression, performance, security, and build verification.

For every batch, specify: exact scope, expected benefit, main risks, required tests, rollback approach, and whether it can be performed independently from other batches.

### Audit guardrails

- Do not modify code during this audit.
- Do not optimize code merely to reduce line count.
- Do not replace clear code with clever abstractions.
- Do not consolidate unrelated domain logic.
- Do not create a large generic component to eliminate superficial duplication.
- Do not remove generated files without confirming how they are regenerated.
- Do not remove database or backend resources without checking external consumers.
- Do not treat any change to public behavior, user flows, permissions, API contracts, database schemas, or visual output as in scope.
- Do not add new dependencies to perform the audit unless strictly necessary and explicitly justified.
- Prefer repository evidence over assumption; separate confirmed findings from hypotheses.
- Prioritize safety, maintainability, clarity, and regression prevention over aggressive deletion.
- End the audit by recommending the smallest safe first cleanup batch.
- **Do not implement any change until the user explicitly approves the audit and the proposed cleanup sequence.**

---

## Phase 2: Cleanup (execution, approval-gated)

Implement **only** the approved batch from a previously completed audit. Never start this phase without an explicit list of approved finding IDs from the user.

**Approved batch:** the user must supply the batch number and finding IDs to implement. If they haven't, ask for them before touching any code — do not infer or assume a batch.

### Before changing code

- Confirm the working version is checkpointed and can be restored.
- Check the current repository status.
- Run the existing build, type-checking, linting, and test commands.
- Record any pre-existing failures separately (do not conflate them with regressions introduced by this cleanup).
- Revalidate every approved finding against the current codebase.
- **Stop and report if the repository has materially changed since the audit** rather than proceeding on stale findings.

### Implementation rules

- Modify only the findings explicitly approved for this batch.
- Do not include findings from later batches.
- Use the smallest safe set of changes.
- Remove code only when the evidence still supports removal.
- Preserve public behavior, visual output, routes, permissions, API contracts, database behavior, and user flows.
- Do not perform unrelated formatting or refactoring.
- Do not rename or reorganize files unless required by the approved batch.
- Do not replace removed code with new abstractions unless necessary.
- Do not uninstall dependencies until all direct, indirect, configuration, build-time, test-time, and runtime usage has been checked.
- Do not delete backend resources, migrations, database functions, policies, buckets, Edge Functions, or environment-variable references without explicit approval.
- Do not suppress TypeScript, linting, build, or test failures.
- Do not use `any`, ignored errors, disabled lint rules, or commented-out code to make validation pass.
- Do not silently change behavior to accommodate the cleanup.

### Incremental execution

Apply the approved cleanup in small logical groups. After each group:

- Run the relevant tests.
- Run type checking.
- Run linting.
- Run the production build.
- Check affected routes and user flows.
- Revert that group if it introduces a regression that cannot be resolved without expanding the approved scope.

For high-risk findings, make one isolated change at a time.

### Validation checklist

At minimum, validate: application startup; production build; TypeScript compilation; linting; existing automated tests; route accessibility; authentication and authorization flows; role-based behavior; data loading and mutation flows; error, empty, loading, and success states; responsive behavior for affected pages; backend or Supabase interactions affected by the cleanup; absence of new console errors or warnings; absence of broken imports, missing assets, or unresolved modules; bundle and dependency integrity.

Where automated coverage is missing, provide a concrete browser-based regression checklist.

### Required output — Cleanup report

After implementation, return:

- Executive summary of the cleanup.
- Approved finding IDs completed.
- Exact files changed.
- Exact files deleted.
- Dependencies removed or changed.
- Explanation of each change and its evidence.
- Commands and tests executed.
- Before-and-after validation results.
- Pre-existing failures that remain.
- Any findings that were not removed, and why.
- Known risks or areas requiring manual verification.
- Rollback instructions.
- Recommended next cleanup batch.

Also report quantitative changes where available: files removed; lines removed; dependencies removed; assets removed; bundle-size change; test-count or coverage change; build-time change.

### Cleanup guardrails

**Do not begin another cleanup batch automatically. Stop after completing and validating the approved batch.**
