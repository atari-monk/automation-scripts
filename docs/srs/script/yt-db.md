## yt-db

### core

- [x] define python script path variable
  - use $HOME
- [x] set variables with text from user input to collect video data:
  - category
  - name
  - id (unique video id from yt url)
- [x] make sure required variables are provided
- [x] build args
  - log name: "yt-db.log"
  - text
  - prepare text by combining category, name, id
  - separate them with vertical bars
- [x] run python script with args

### features

- [x] folders was introduced, log_name must be now log_path with `folder/log_name` values
  - not hard coded string
  - folder and log name is variable
  - input for path is needed

---

[tts](https://raw.githubusercontent.com/atari-monk/automation-scripts/main/docs/srs/script/yt-db.txt)
