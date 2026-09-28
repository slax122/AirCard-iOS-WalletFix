# AirCard-iOS WalletFix Source Builder

This package fixes the problem with the earlier ZIP: it now has the expected
`ios-app/` and `rust-core/` directories and a GitHub Actions workflow that
pulls the real upstream AirCard-iOS source into them automatically.

The upstream repository is the source of truth. The current public repository
contains `ios-app`, `rust-core`, `AirliftFFI.xcframework`, `project.yml`, and
the iOS build scripts.

## Use

1. Create an empty GitHub repository.
2. Upload the contents of this ZIP.
3. Open **Actions** and run **Sync upstream source**.
4. The workflow downloads the upstream source and uploads a `source-tree`
   artifact containing the real `ios-app/` and `rust-core/` trees.

No Xcode or VM is required on your computer for the sync step.

## Important

This is a source/build package, not a pre-signed IPA. Building iOS software
still requires Apple's build/signing environment. The workflow is deliberately
set up to stop before producing a misleading "fixed" IPA unless the source
patch applies cleanly.
