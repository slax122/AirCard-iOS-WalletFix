# Wallet cache diagnosis

Your screenshots show that the custom artwork is already present in the
Apple Account card/details representation, while the main Wallet card face
still uses Apple's stock artwork.

Current upstream AppViewModel.swift writes `corrupted` into FrontFace,
Preview, and PlaceHolder under both .cache and .pkcache.

The current macOS AirCard implementation uses a real move-out/removal
operation for those protected rendered files instead. That is the behavior
the eventual iOS Rust FFI patch needs to reproduce.

Sources checked:
- https://github.com/Mak5er/AirCard-iOS
- https://github.com/Mak5er/AirCard
