############
Benchmarking
############
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
