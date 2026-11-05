cd "$(dirname "$0")"
ARGS=""
for f in "$@"; do b=$(basename $f .md); pandoc -f gfm-tex_math_dollars -t html5 -s --metadata title="$b" -V title= -c short.css $f -o $PWD/$b.html; ARGS="$ARGS $PWD/$b.html=$PWD/$b.pdf"; done
node build.js $ARGS >/dev/null
for f in "$@"; do b=$(basename $f .md); python3 -c "from pypdf import PdfReader;print('$b', len(PdfReader('$b.pdf').pages))"; done
