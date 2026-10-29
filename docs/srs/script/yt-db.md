## yt-db

### core

- [x] define python script path variable
  - use $HOME
- [x] set variables with text from user input to collect video data:
  - id (unique vodeo id from yt url)
  - name
  - tags (comma separeted list)
- [x] make sure required variables are provided
- [x] build args
  - log name: "yt-db.log"
  - text
  - prepare text by combining id, name, tags
  - separate them with vertical bars
- [x] run python script with args

### features

- [] folders was introduced, log_name must be now log_path with `folder/log_name` values
  - not hard coded string
  - folder and log name is variable
  - input for path is needed

---

[tts](yt-db.txt)
