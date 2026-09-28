#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
swift = root / "ios-app/AppViewModel.swift"
rust = root / "rust-core/src/exploit.rs"

s = swift.read_text()
r = rust.read_text()

markers = [
    ('Swift', 'Data("corrupted".utf8)', s),
    ('Swift', 'al_exploit_write_dir', s),
    ('Rust', 'async fn exploit_write_dir(', r),
    ('Rust', 'async fn exploit_write_single_file(', r),
]
missing = [f"{kind}: {needle}" for kind, needle, text in markers if needle not in text]
if missing:
    print("Upstream source changed; refusing a partial patch.")
    print("\n".join(missing))
    raise SystemExit(2)

print("Expected upstream Wallet-cache implementation found.")
print("A real compiled fix requires the Rust FFI removal implementation.")
