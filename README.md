# Auto-generation of Lo-fi Hip-hop w/ Tonality

This project is the result of my attempts to hack together a very basic lo-fi hip hop beat generator.

The repository consists of:
* an extendable object-oriented hierarchy of musical objects such as Note, MajorSeventhChord, etc.
* a "composer" class to sequentially decide which chords should be generated
* an imported/forked synthesizer piano class to play and render the chord sequence
* a "processor" class to overlay the .wav samples over our newly synthesized track

Currently doing research on how machine learning can be incorporated into this project!

In the meantime, [check out some beats produced by this algo!!](https://pl728.github.io/lofi-generator-live-website/)
