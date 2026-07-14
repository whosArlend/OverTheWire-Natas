from pathlib import Path
for i in range(6, 33):
    Path(f"level-{i:02}.md").touch()