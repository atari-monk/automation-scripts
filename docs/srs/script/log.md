## log

`src/log.py`

### core

- [x] log format: "%(asctime)s %(message)s"
- [x] define key - marker pairs:
  - start: [START]
  - end: [END]
- [x] define key - aliases pairs:
  - start: -s, --start
  - end: -e, --end
- [x] use extract_flags helper
- [x] select marker for extracted flag
- [x] use require_args helper
- [x] extract log_name and text from args
- [x] set path for logs dir
- [x] use get_logger helper
  - set log file name
- [x] log text with optional marker

### features

- [x] folders was introduced, log_name must be now log_path with `folder/log_name` values

---

[tts](log.txt)
