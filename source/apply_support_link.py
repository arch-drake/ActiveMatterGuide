# Standalone optional-support patch: keep built HTML separate from legacy build system.
# Use only on a newly compiled guide that has the known anchors; idempotent by link existence.
from pathlib import Path
import sys
p=Path(sys.argv[1] if len(sys.argv)>1 else 'active_matter_solo_pve_field_guide.html')
s=p.read_text('utf-8')
url='https://buymeacoffee.com/elderdrake'
if url in s: print('Support link already present; no changes');sys.exit(0)
anchor='<footer>Fan-made personal companion.'
if anchor not in s: raise SystemExit('Unknown HTML build; aborting to preserve data')
s=s.replace(anchor, f'<footer><p><a href="{url}" target="_blank" rel="noopener noreferrer">☕ Support the free guide</a> — entirely optional.</p>Fan-made personal companion.',1)
p.write_text(s,'utf-8')
