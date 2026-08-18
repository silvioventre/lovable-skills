# Writing workspace knowledge

Rules that hold across every project in the workspace. Written once, applied everywhere, so an entry here is worth more than the same entry repeated in five projects — and a wrong entry costs five times as much.

Only workspace owners and admins can edit it, which is the point: it is where a team's guardrails live.

## The placement test

Before adding anything, ask: **would this still be true in the next project we start?**

Yes → workspace. No → project knowledge.

Applied honestly, this keeps workspace knowledge small and stable, which is what makes it followed.

## What belongs here

**Coding standards.** Type strictness, forbidden patterns, export style, variable declarations.

**Naming conventions.** Casing for variables, components, types, files.

**Preferred libraries.** The styling approach, the component library, how server state and client state are handled. This one prevents the most churn: without it, every project accumulates a slightly different stack.

**Architectural patterns** that should be consistent — where API calls live, what components are allowed to do directly.

**Testing requirements.** What must be tested, what must be run after a change.

**Code quality rules.** Linting, dead code, unused imports.

**Language and formatting.** Comment language, date format, number formatting. Easy to forget and irritating to correct repeatedly.

**Brand voice and UI copy rules.** Tone, sentence case versus title case, no placeholder text. These belong here because they apply to every project's user-facing strings.

**Things to avoid.** Often the highest-value section, because it is the one that stops recurring behaviour.

## Shape

```
Coding standards
- Always enable TypeScript strict mode.
- Never use `any`. Use `unknown` and narrow the type.
- Prefer named exports. Do not use default exports.

Naming
- camelCase for variables and functions.
- PascalCase for components and types.
- kebab-case for file names.

Styling
- Use Tailwind CSS. Do not use inline styles or CSS modules.

Libraries
- Use shadcn/ui components when available.
- Use React Query for server state.

Architecture
- Route API calls through a service layer.
- Do not call `fetch` directly from React components.

Testing
- Write tests for new utility functions and hooks.
- Verify new functionality in the browser before marking it complete.

Copy
- Sentence case for headings and buttons.
- Never ship placeholder text such as "Lorem ipsum".

General
- Do not add `console.log` statements.
- Write code comments in English.
```

Note the form: each line is a rule that can be checked against a diff. Nothing here is a preference expressed as a wish.

## What does not belong

- **Anything about one project.** Its purpose, schema, users, or terminology. That is project knowledge.
- **Task-specific procedures.** A checklist that applies to launches is a skill.
- **Rules only some projects should follow.** There is one workspace knowledge and no way to scope it to a subset. A rule that is wrong for some projects will be violated in them, which teaches everyone that the rules are advisory.
- **A style guide copied from elsewhere.** Rules nobody in the team actually follows still consume the character budget and still get applied.

## When a project needs to differ

Project knowledge generally takes precedence over workspace knowledge, so a project that genuinely needs a different rule can state it locally.

Use that sparingly. Frequent overrides mean the workspace rule is wrong, or too specific to be a shared rule at all — and the fix is to change the workspace rule rather than to accumulate exceptions.
