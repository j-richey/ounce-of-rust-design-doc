############
Benchmarking
############

The library provides a benchmark of the worst case AI update time allowing
users of the library to evaluate if the library fits in with their performance
goals. Cargo contains built in benchmark support: any tests that have the
``bench`` attribute are exercised by running ``cargo bench``. [#rustbenchmark]_
:numref:`code-ai-move-benchmark` shows an example of benchmarking the worst
case AI move.

..  _code-ai-move-benchmark:
..  code-block:: rust
    :caption: Example worst case AI move benchmark.

    #[bench]
    fn worst_case_ai_move_benchmark(b: &mut Bencher) {
        let game = Game::new();
        let mistake_probability = 0.0;
        b.iter(|| AIMove::new(game, mistake_probability));
    }

The worst case update time is for a new game and a zero percent mistake probability.
Under this situation the :doc:`ai-algorithms` have to evaluate the entire
problem space.

The library's source code repository ``README.md`` file contains instructions on
how to run the benchmarks.


..  rubric:: Related Requirements

* :ref:`ref-maximum-ai-update-time-story`


..  rubric:: Footnotes

..  [#rustbenchmark] See `Benchmark tests <https://doc.rust-lang.org/1.7.0/book/benchmark-tests.html>`_ for details.
