# Cython (Protonox Optimized)

Expected source: https://github.com/cython/cython (latest stable 3.x preferred; fall back to 0.29.x if required by P4A)

## Protonox Notes
- Build configuration tuned for ARM64 performance and reproducibility.
- Prefer `CYTHON_LIMITED_API` disabled for compatibility with python-for-android.
- Strip `.git` after syncing to keep repository lightweight.

## Sync Checklist
1. Fetch a release archive or clone `https://github.com/cython/cython`.
2. Remove `.git` if cloned.
3. Note the version in `../VERSIONS.md`.
