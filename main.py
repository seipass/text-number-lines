from __future__ import annotations
def run(text):
 return "\n".join(f"{i}: {s}" for i,s in enumerate(text.splitlines(),1))
