# Investigating an existing project

For a project that has grown, that someone else built, or that the user has not opened in months. The goal is an accurate picture of what exists before anything is added to it.

## Ask the right questions, in parallel

Split the investigation into bounded questions and delegate them to subagents. Each one gets a specific question, the paths that matter, and what to report back. They run at once and report independently.

For an unfamiliar project, the questions that establish the shape:

- **What are the main surfaces?** Routes and pages, what each is for, which are reachable and which are dead.
- **How does data flow?** Where it comes from, what transforms it, where it lands. The shape at each hop.
- **How is authentication handled?** Where identity is established, how roles are resolved, what is protected and how.
- **What is the data model?** Tables, relationships, which are actually used, which have policies.
- **What patterns does this codebase use?** State management, data fetching, error handling, component structure. Not what is best practice — what *this* project does.
- **What is shared?** Components and utilities used in many places, because those are the things a change can break widely.

For a targeted question — *why does this behave this way*, *where is this handled* — one investigation with traceable evidence is better than several shallow ones. Ask for the answer plus the files and the path through them, so the conclusion can be checked rather than trusted.

## Write briefings that return something useful

A subagent sees only what you pass it. It does not have the conversation, your earlier reading, or the user's original phrasing unless you include them.

A briefing that works contains: the specific question, where to start looking, what the answer should include, and what is out of scope. A briefing that does not is "look at the auth code" — which returns a summary of the auth code, not an answer.

Ask for evidence, not conclusions. "Explain how sign-in works, citing the files and the order they run in" is checkable. "Summarise the auth system" is a paragraph you cannot verify.

## Read the findings critically

Subagent findings inform the plan; they do not replace judgment.

- **Where two findings disagree**, that gap is usually the most interesting thing in the investigation — frequently a real inconsistency in the project rather than a mistake by either.
- **Where a finding has no file behind it**, treat it as a hypothesis. A confident summary with nothing to check is the failure mode of delegated research.
- **Where nothing was found**, distinguish "this does not exist" from "this was not looked for". They lead in opposite directions.

## What to establish before proposing anything

At the end of an investigation you should be able to say, specifically:

- **What already exists** that the new work would touch or duplicate. The most common waste in a grown project is building a second version of something that is already there.
- **What the project's conventions are**, so the new work matches instead of introducing a competing pattern.
- **Where the fragile parts are** — auth, payments, migrations, anything shared widely — so the plan routes around them or handles them deliberately.
- **What is dead.** Code that no longer runs, tables nobody reads, routes nothing links to. Worth naming, not worth fixing here — that is the `lovable-codebase-audit-cleanup` skill.

## Report it in the project's own terms

An investigation that returns generic architecture description has failed. The output should name this project's routes, tables, and components, and describe how *this* app works — including the parts that are unusual, inconsistent, or clearly the result of an earlier decision nobody remembers.

Then say what surprised you. The thing that did not match expectation is nearly always where the next bug or the next wrong assumption is waiting.
