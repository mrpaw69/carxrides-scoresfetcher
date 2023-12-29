# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2023-12-29

### Added

- This changelog
- Added "UTC" at the end of datetime string to eliminate timezone confusion
- Added UTC timestamp to "ts_utc" to posts.csv and comments.csv

### Removed

- Removed accidentally pushed API keys (they cannot be used now anyway)

### Fixed

- "Older posts first" bug has been fixed

### Related PRs/Issues

- [#6 Fix the sorting](https://github.com/mrpaw69/carxrides-scoresfetcher/pull/6)
- [#7 1.1.1 release](https://github.com/mrpaw69/carxrides-scoresfetcher/pull/7)

## [1.1.0] - 2023-12-23

### Changed

- Removed the 3 winners limit

### Related PRs/Issues

- [#3 Ability to write about more than 3 winners](https://github.com/mrpaw69/carxrides-scoresfetcher/pull/3)

## [1.0.1] - 2023-12-18

### Changed

- Switched from MIT license to Apache 2.0 license

### Related PRs/Issues

- [#2 Update license](https://github.com/mrpaw69/carxrides-scoresfetcher/pull/2)

## [1.0.0] - 2023-12-11

 Nothing was added/changed/removed, it's [rc-1.0.0](#rc-100---2023-12-08) rereleased as a stable release

## [rc-1.0.0] - 2023-12-08

### Added

- Ability to fetch all posts and comments from r/CarXStreetRides within specified time range, using PRAW lib
- Scores calculation based on the fetched posts
- Saving all the scores

### Related PRs/Issues

- [#1 Getting ready for open-source](https://github.com/mrpaw69/carxrides-scoresfetcher/pull/1)

[unreleased]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.1.0...develop
[1.2.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/compare/rc-1.0.0...1.0.0
[rc-1.0.0]: https://github.com/mrpaw69/carxrides-scoresfetcher/releases/tag/rc-1.0.0
