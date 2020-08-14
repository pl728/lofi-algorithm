# Auto-generation of Lo-fi Hip-hop w/ Tonality

This project is the result of my multiple attempts to hack together a very basic lo-fi hip hop beat generator.

The repository consists of:
* an extendable object-oriented hierarchy of musical objects such as Note, MajorSeventhChord, etc.
* a "composer" class to sequentially decide which chords should be generated
* an imported/forked synthesizer piano class to play and render the chord sequence
* a "processor" class to overlay the .wav samples over our newly synthesized track

Eventually, machine learning will be incorporated into this project. 

In the meantime, check out some [beats](http:/pl728.github.io/lofi-site) produced by this algo!!
