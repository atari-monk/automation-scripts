## Typescript Library

`lib/typescript_library.py`

### docs

- create helper `create_docs`
  - use `create_folder` to create
    - `docs`
  - use `create_file` to create
    - `\_config.yml`

### prompt

- create helper `create_prompt`
- use `create_folder` to create
  - `prompt`
- use `create_file` to create
  - `prompt.md`

### src

- create helper `create_src`
- use `create_folder` to create
  - `src`
- use `create_file` to create
  - `index.ts`

### config files

- base path: `/home/atari-monk/atari-monk/project/`
- use `copy_file_and_log`
  - source: `base/typescript-library/file-name`
  - destination: `base/project-name/file-name`
  - on files:
    - `.gitignore`
    - `package.json`
    - `README.md`
    - `tsconfig.json`
    - `tsup.config.ts`
- use `set_package_meta` to set name and description for `package.json`
