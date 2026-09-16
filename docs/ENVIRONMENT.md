# Environment notes

Shared log of setup problems and fixes, started in `w0m1`. Add an entry every
time something breaks during setup — what you ran, the exact error, what
fixed it. Future trainees (and future you) read this before opening an issue.

Add your entry below the template row. Don't delete anyone else's.

| Date | Trainee | What broke | Exact error | Fix |
|------|---------|------------|--------------|-----|
| YYYY-MM-DD | your name | one line | paste the real message | one line |
| 2026-09-16 | jya | `python` resolved to Windows Store stub, not a real interpreter | `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.` | Found real install at `C:\Users\jyaltma\AppData\Local\Programs\Python\Python312-arm64\python.exe` (already present, just not on PATH); added that dir and its `Scripts` subfolder to the User PATH env var |
| 2026-09-16 | jya | `npm ci` failed — Node.js/npm not installed anywhere on the machine | `node: command not found` / `npm: command not found` (bash); `The term 'node' is not recognized...` (PowerShell) | Installed via `winget install --id OpenJS.NodeJS.LTS -e --source winget --accept-package-agreements --accept-source-agreements` |
| 2026-09-16 | jya | `npm ci` failed — no lockfile in repo | `npm error The \`npm ci\` command can only install with an existing package-lock.json or npm-shrinkwrap.json` | Ran `npm install` once to generate `package-lock.json`, then `npm ci` succeeded |
