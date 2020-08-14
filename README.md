# Auto-generation of Lo-fi Hip-hop w/ Tonality

This project is the result of my multiple attempts to hack together a very basic lo-fi hip hop beat generator.

The repository consists of:
* an extendable object-oriented hierarchy of musical objects (notes, chords, major seventh chord, etc)
* a "Composer" class to sequentially decide which chords should be generated
* a (cloned) synthesizer piano class to play the notes
* a "Processor" class to overlay the .wav samples over our newly synthesized track

Check out [sample beats](http:/pl728.github.io/lofi-site) produced by this algo!!
