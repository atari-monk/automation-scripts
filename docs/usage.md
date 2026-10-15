## Usage

### Log

One liner

```sh
name="" && text="" && script="/home/atari-monk/atari-monk/project/automation-scripts/src/log.py" && python3 "$script" "$name" "$text"
```

Input

```sh
script="/home/atari-monk/atari-monk/project/automation-scripts/src/log.py"
read -rp "name: " name
[ -z "$name" ] && echo "name required"
read -rp "text: " text
[ -z "$text" ] && echo "text required"
if [ -n "$name" ] && [ -n "$text" ]; then
  python3 "$script" "$name" "$text"
fi
```

Readable

```sh
name=""
text=""
script="/home/atari-monk/atari-monk/project/automation-scripts/src/log.py"
python3 "$script" "$name" "$text"
```
