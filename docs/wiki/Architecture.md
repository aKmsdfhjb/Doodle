# Doodle Recognition — Architecture

## System flow

```mermaid
flowchart TD
 A[Quick Draw dataset] --> B[Prepare and label images]
 B --> C[Train CNN]
 C --> D[Save doodle_model.h5]
 E[Browser drawing canvas] --> F[Submit sketch image]
 F --> G[Flask inference API]
 D --> G
 G --> H[Resize and normalize image]
 H --> I[CNN prediction]
 I --> J[Class and confidence]
 J --> E
```

## Design notes

- Keep user-interface responsibilities separate from model, API and data-service responsibilities.
- Validate inputs at the application boundary and return clear error messages.
- Keep secrets and privileged credentials on the server side.
- Document the versions of data, dependencies and model artifacts used for reproducible results.
- Test the full user journey after deployment, not only the build step.

## Deployment boundary

GitHub Pages can host static HTML, CSS, JavaScript and prebuilt frontend assets. It cannot execute Python/Flask services, server-side React Router actions, private environment variables or database operations. Those parts require a separate backend or application host.
