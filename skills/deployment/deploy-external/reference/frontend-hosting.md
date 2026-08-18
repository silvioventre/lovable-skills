# Hosting the frontend elsewhere

The most common move outside Lovable Cloud, and the most reversible. The backend can stay where it is; no architectural change is needed.

## Build requirements

Projects are standard Vite applications that build to static files.

| Setting | Value |
|---|---|
| Build command | `npm run build` |
| Output directory | `dist/` |
| Node version | 22 recommended |

Any host that runs a Node build and serves static files works: managed Git-based platforms, object storage behind a CDN, containers, or a VM with a web server.

## Environment variables — the part that trips people

**Variables prefixed `VITE_` are embedded at build time, not read at runtime.** Two consequences:

- **They must be set before the build runs**, in the hosting platform's build environment. Setting them afterwards changes nothing until the next build.
- **Their values ship inside the bundle** and are readable by every visitor. This is fine for a publishable key designed for client use. It is never acceptable for a secret — see the `secure` skill.

When the backend stays on Lovable Cloud, the frontend needs its connection values set before building. They are in the project's `.env` file:

```
VITE_SUPABASE_URL
VITE_SUPABASE_PUBLISHABLE_KEY
```

Copy them into the host's build environment variables. The publishable key is designed to be public; the server-side rules are what constrain it.

## Git-based platforms

Netlify, Cloudflare Pages, Vercel, AWS Amplify, Azure Static Web Apps, Firebase Hosting. These connect to the GitHub repository and rebuild on each push.

Setup is the same everywhere: point at the repo, set build command `npm run build`, publish directory `dist/`, Node 22, and add the environment variables **before the first build**.

Two things to configure that are easy to forget:

- **SPA routing.** A single-page app needs unmatched routes rewritten to `index.html`, or every deep link and refresh returns a 404. This is the most common "it works on the homepage only" report after moving hosting.
- **Which branch deploys.** Pushing from Lovable to the tracked branch now deploys to production. Decide whether that is what you want, or whether production should track a separate branch.

## Object storage plus CDN

S3 with CloudFront, Cloud Storage with Cloud CDN, and equivalents. These serve files but do not build, so a pipeline has to run `npm run build` and upload `dist/`.

The same SPA routing requirement applies, configured as an error-document rule or a CDN function rather than a redirects file. Also set cache headers deliberately: hashed assets can cache for a long time, `index.html` must not, or visitors keep getting the previous release.

## Containers

For Kubernetes, ECS, Cloud Run, or a single VM. A standard two-stage build: install and build in Node, then serve the static output with a web server.

```dockerfile
# Build stage
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Serve stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

The nginx config needs the SPA rewrite, or deep links 404:

```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

Build-time variables must be passed as build arguments and set before `npm run build` runs — a container built without them ships a frontend that cannot reach its backend, and the failure appears at runtime as an unexplained connection error.

Generating the Dockerfile and web server configuration is in-project work and can be done here. Building the image, pushing it to a registry, and running it are the user's.

## Verify after moving

Check on the deployed URL, not locally:

- **The homepage loads**, and assets, fonts, and images resolve.
- **A deep link typed directly** resolves rather than 404ing. This is the SPA routing check, and it is the one that fails.
- **A hard refresh on a sub-route** works, for the same reason.
- **The backend is reachable** — a signed-in read and a write, confirming the build-time variables were present.
- **Authentication completes**, including any redirect URLs, which frequently reference the old origin and must be updated at the provider.

That last point is a common failure after a domain change: sign-in appears to work and then redirects into nothing, because the auth provider still lists the previous URL.

## What changes afterwards

Production is now yours: deployments, rollbacks, uptime, caching, logs. Lovable still handles development and previews, but it cannot see or debug the production environment. When production breaks and the preview is fine, the difference is in infrastructure you own, and the host's logs are where the answer is.
