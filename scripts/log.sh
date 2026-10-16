script="$HOME/atari-monk/project/automation-scripts/src/log.py"

read -rp "name: " name
read -rp "text: " text
read -rp "flag (blank/-s/-e): " flag

[ -z "$name" ] && { echo "name required" >&2; exit 1; }
[ -z "$text" ] && { echo "text required" >&2; exit 1; }

args=("$name" "$text")
[ -n "$flag" ] && args+=("$flag")

python3 "$script" "${args[@]}"