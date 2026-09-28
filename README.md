# AirCard-iOS WalletFix builder

This is a GitHub Actions builder overlay for AirCard-iOS. It is not a
precompiled IPA: the Rust/Xcode build must run on a macOS runner.

The upstream iOS app currently invalidates Wallet rendered faces by writing
sentinel bytes into FrontFace/Preview/PlaceHolder. The current macOS AirCard
implementation instead moves those protected cache leaves out through the
Airlift link and removes the moved objects. This builder is intended to port
that behavior into AirCard-iOS.

Use:
1. Create a GitHub repository.
2. Upload the contents of this ZIP.
3. Open Actions and run the workflow.
4. The workflow is configured to stop rather than silently produce a
   misleading IPA until the Rust FFI removal operation is compiled in.

The upstream project documents build-ios.sh as the Rust/AirliftFFI build step
and build-ipa.sh as the unsigned IPA packaging step.
