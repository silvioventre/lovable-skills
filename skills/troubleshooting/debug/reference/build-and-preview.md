# Build failures, blank screens, and preview problems

Hard failures. The app does not build, or builds and shows nothing. Clear these before any other investigation — a project that will not run cannot be reasoned about.

## Build errors

Read the error text before touching anything. Build errors are usually precise, and the file and line in the message are almost always the real location.

| Error family | Usual cause | Fix |
|---|---|---|
| Type error, type mismatch | A value's shape changed but a consumer was not updated. Frequently a database value arriving as a string where a number was expected, or a nullable field treated as non-null | Correct the type at the boundary where the data enters, not at each place it is consumed |
| Cannot find module, unresolved import | File moved, renamed, or deleted while an import was left behind; or a package used but never installed | Fix the path, or add the dependency. Never stub the module to silence it |
| X is not defined / not a function | Import removed, wrong named vs default import, or a rename applied in one place only | Trace the symbol to its definition and reconcile |
| Duplicate declaration | The same helper introduced twice by separate edits | Delete one and point both callers at the survivor |
| Syntax error | An incomplete edit — an unclosed brace, a stray fragment from a partial change | Read the surrounding block; the reported line is often just after the real break |

When the message names a file and line, start there. When it does not, the last changed file is the first suspect.

## Blank or white screen

The build succeeded but nothing renders. Work through these in order — the first four cover nearly every case.

1. **Read the browser console.** A blank screen almost always has a runtime error behind it, and the console names it. This single step resolves most cases; do not skip it because the page "just looks empty".
2. **A crash during render.** An exception thrown in a top-level component takes down the whole tree. The console shows it. Common triggers: reading a property of `undefined` before data arrives, calling a method on a value whose shape changed, mapping over something that is not an array.
3. **Build or preview configuration.** A broken build config file, or security headers introduced into the project, can produce a blank page with nothing in the console. Ask what changed in configuration since it last rendered.
4. **Routing or auth gating.** The route may render nothing because no route matched, or because an auth guard redirected to a destination that itself renders nothing. Check what the URL is and what the router does with it.
5. **A missing return.** A component that falls through without returning JSX renders nothing and raises no error. Check the component that should own the page.
6. **Data-dependent emptiness.** The page renders but every region is conditional on data that never arrived. Confirm with a hard-coded value — if the layout appears, the bug is in the data path, so continue in [backend.md](backend.md).

If the console is clean and configuration is unchanged, revert to the last version that rendered and compare. A blank screen with no error is nearly always something removed rather than something broken.

## Preview not found, sandbox stuck

Usually environmental rather than a bug in the code.

- **Hard refresh first.** Sandbox problems are frequently transient and clear on a reload.
- **If it persists**, suspect the connection or a broken sync with the connected repository rather than the app code.
- **Do not start editing code to fix this.** Changing application code to resolve an environment problem adds real bugs on top of a temporary one. Confirm the app actually broke before touching it.

## "File exceeds the 10 MB per-file commit limit"

Every change is saved into the project's code, and a single file above 10 MB cannot be stored there. This normally follows attaching a large video, image, or archive in chat and asking for it to be added to the project.

Large media does not belong in project code. Ask for the files to be migrated to CDN assets — the platform uploads them, repoints the app, and leaves small placeholders behind. There is no manual command to run for this, and any CLI named in the error message is internal tooling, not a step for the user.

The same limit blocks edits to an oversized file already pushed from outside, so a file over 10 MB must shrink or move before it can be changed at all.

## Before moving on

A build that succeeds and a page that renders is the floor, not the fix. If the original complaint was behavioural, continue in [behavior.md](behavior.md) — clearing a hard failure often reveals the bug that was reported in the first place.
