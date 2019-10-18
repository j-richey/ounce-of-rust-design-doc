####################
Other Considerations
####################
This section contains other design considerations for the Tic Tac Toe crate.

..  TODO:
    * How to find wining games / end of game condition (include example code)
    * Sharing the code.
      * Source is on GitHub (name of repo) :ref:`ref-source-available-on-github-story`
      * What license the library is released under: hint, its the MIT license. :ref:`ref-permissive-license-story`
    * How to add the library to crates.io:
      * See https://doc.rust-lang.org/cargo/reference/publishing.html
      * :ref:`ref-available-on-crates-io-story`
    * Documenting the library: :ref:`ref-getting-started-example-story` and :ref:`ref-detailed-library-documentation-story`
      * How to document public members (tipple slashes, link to details)
      * How to hose the documentation. I think just adding the crate to crates IO does this.
      * Documentation guidelines: https://rust-lang-nursery.github.io/api-guidelines/documentation.html
    * :ref:`ref-stable-library-api-story`
      * Travis.ci that builds the library and runs the tests (including documentation tests)
      * Travis.ci also builds for Windows or other OS's :ref:`ref-cross-platform-support-story`
        * See https://docs.travis-ci.com/user/multi-os/
      * A CHANGELOG.md file is sufficient for this purpose according ot the rust thing.


===========================
Benchmarking AI Update Time
===========================
The :ref:`ref-maximum-ai-update-time-story` user story requires there be a benchmark
for the AI update time. Luckily cargo makes this as easy as running `cargo bench`. [#rustbenchmark]_

:numref:`code-ai-move-benchmark` shows an example of benchmarking the worst case
AI move.

..  _code-ai-move-benchmark:
..  code-block:: rust
    :caption: Example worst case AI move benchmark.

    #[bench]
    fn worst_case_ai_move_benchmark(b: &mut Bencher) {
        let game = Game::new();
        b.iter(|| AIMove::new(game, 0.0));
    }

The worst case is time is for a new game and a zero percent mistake probability.
Under these situations the :doc:`ai-algorithms` have to evaluate the entire
problem space.


..  rubric:: Footnotes

..  [#rustbenchmark] See `Benchmark tests <https://doc.rust-lang.org/1.7.0/book/benchmark-tests.html>`_ for details.
