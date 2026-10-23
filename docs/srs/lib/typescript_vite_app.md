## Typescript Vite App

`lib/typescript_vite_app.py`

- [Project Files](project-files.md)
- base path: `/home/atari-monk/atari-monk`

### config files

- use `copy_file_and_log`
  - source: `base/project/typescript-vite-app/file-name`
  - destination: `base/project/project_name/file-name`
  - on files:
    - `.gitignore`
    - `index.html`
    - `package.json`
    - `tsconfig.json`
- use `set_package_meta` to set name and description for `package.json`

### src

- create helper `create_src`
  - use `create_folder` to create
    - `src`
  - use `copy_file_and_log`
    - source: `base/project/typescript-vite-app/file-name`
    - destination: `base/project/project_name/file-name`
    - on files:
      - `main.ts`
      - `style.css`

### public

- create helper `create_public`
  - use `create_folder` to create
    - `public`
  - use `copy_file_and_log` to copy
    - source: `base/project/typescript-vite-app/public/favicon.svg`
    - destination: `base/project/project_name/public/favicon.svg`
