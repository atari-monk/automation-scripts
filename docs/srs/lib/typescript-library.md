## Typescript Library

`lib/typescript_library.py`

- [Project Files](project-files.md)

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
