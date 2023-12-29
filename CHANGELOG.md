# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Versions with `.rc_x` postfix at the end, where x is a release number, are Release Candidate pre-releases. Example: 6.9.0.rc_1, which means "Version 6.9.0 Release Candidate 2".
>NOTE: The first Release Candidate is rc-1.0.0, not 1.0.0_rc_0

Versions with `.alpha_x` postfix at the end, where x is a release number, are Alpha(very early) pre-releases. Example: 6.9.0.alpha_0, which means "Version 6.9.0 Alpha 1".
>NOTE: Alpha releases may lack features from current versions

Versions with `.beta_x` postfix at the end, where x is a release number, are Beta(early) pre-releases. Example: 6.9.0.beta_2, which means "Version 6.9.0 Release Beta 3".
>NOTE: Beta releases may lack features from current versions

## [Unreleased]

### Added

- This changelog
- Added "UTC" at the end of datetime string to eliminate timezone confusion
- Added "ts_utc" to posts.csv and comments.csv

### Removed

- Removed accidentally pushed API keys (they cannot be used now anyway)

### Fixed

- "Older posts first" bug has been fixed

## [1.1.0] - 2023-12-23

### Changed

- Removed the 3 winners limit

## [1.0.1] - 2023-12-18

### Changed

- Switched from MIT license to Apache 2.0 license

## [1.0.0] - 2023-12-11

 Nothing was added/changed/removed, it's [rc-1.0.0](#rc-100---2023-12-08) rereleased as a stable release

## [rc-1.0.0] - 2023-12-08

### Added

- Ability to fetch all posts and comments from r/CarXStreetRides within specified time range, using PRAW lib
- Scores calculation based on the fetched posts
- Saving all the scores

[unreleased]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.1.0...develop
[1.1.1.beta_0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.1.0...1.1.1.beta_0
[1.1.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/rc-1.0.0...1.0.0
[rc-1.0.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/releases/tag/rc-1.0.0
