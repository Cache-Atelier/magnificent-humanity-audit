#!/bin/bash
# capture_report.sh <render_html_name> <H> <outprefix>  — full-page dark+light captures at width 1100
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="/Users/dominicrishe/Documents/web-dev/magnificent-humanity-audit/design-explorations"
NAME="$1"; H="$2"; PREFIX="$3"
W=1100
# light variant: copy with bootstrap default flipped to 'light'
LIGHT="${NAME%.html}-LIGHTPROBE.html"
sed "s/if(!t){t='dark';}/if(!t){t='light';}/" "$DIR/$NAME" > "$DIR/$LIGHT"
for MODE in dark light; do
  if [ "$MODE" = "dark" ]; then URL="http://localhost:8742/$NAME"; else URL="http://localhost:8742/$LIGHT"; fi
  OUT="$DIR/audit-shots/${PREFIX}-${MODE}-full.png"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 \
    --window-size=${W},${H} \
    --virtual-time-budget=9000 \
    --screenshot="$OUT" "$URL" 2>/dev/null
  python3 -c "
import struct
f=open('$OUT','rb'); f.read(16); w,h=struct.unpack('>II', f.read(8))
print('$OUT', w, 'x', h)
"
done
rm -f "$DIR/$LIGHT"
