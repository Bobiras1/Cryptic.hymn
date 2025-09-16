# -*- coding: utf-8 -*-
"""
ΞΕΝΟ-ὝΜΝΟΣ — Ancient Greek × Alien RPG
A looping, atmospheric text generator that repeatedly chants short stanzas,
mixing ancient-Greek lexemes, transliteration, and invented alien glyphs.

Stop with Ctrl+C.
"""

import random
import time
import itertools
import sys

# Pools of ancient-ish Greek roots, adjectives, verbs (small curated set)
GREEK_NOUNS = [
    "ἄστηρ", "χρόνος", "λόγος", "ψυχή", "πόλις",
    "ὕδωρ", "πνεῦμα", "νύξ", "θάλασσα", "νους"
]

GREEK_ADJ = [
    "ἀρχαῖος", "βαθύς", "ἁγνός", "σκοτεινός", "ἀέναος",
    "ἄφθαρτος", "ἑρμηνευτικός", "μακραίωνος"
]

GREEK_VERBS = [
    "ἀνέτειλε", "ἐπιφάνη", "ὑποκρύπτει", "ἀναβοά", "ὁδηγεῖ",
    "συλλαμβάνει", "ὑφαίνει"
]

# Alien names, glyphs, and postfixes
ALIEN_GLYPHS = [
    "⟟", "⨳", "⩚", "⋮", "ꖎ", "𐑂", "᚛", "᚜", "⚯", "✶"
]

ALIEN_SOUNDS = [
    "k'thox", "zrā", "q'ul", "ɸa-š", "x'rul", "ŋa'th", "s'vex"
]

ALIEN_TITLES = [
    "Σαυρ-Ὃ", "Χαρ–Μ'α", "Ωλ-Ξι", "Θ'υλ-πᾶ", "Νοξ·Ḡ"
]

REFRAINS = [
    "ἔτι καὶ ἔτι — ⟟⟟⟟",
    "Ὡς ἀεί — 𐑂𐑂",
    "Ἀέναος ὕμνος· k'thox…",
    "Πάλιν· q'ul q'ul q'ul"
]

# small helper functions

def pick(seq):
    return random.choice(seq)

def greekize(name):
    """Add Greek-style endings and diacritics to an alien token."""
    suffixes = ["ος", "ης", "ον", "ᾱ", "ᾶ", "ας"]
    return name + random.choice(suffixes)

def glyph_cluster(n=2):
    return "".join(random.choice(ALIEN_GLYPHS) for _ in range(n))

def make_hero():
    # combine an alien sound and a Greek noun/title
    a = pick(ALIEN_SOUNDS)
    g = pick(ALIEN_TITLES)
    return f"{g}·{a}"

def stanza(seed=None):
    """Generate a short stanza mixing Greek and alien elements."""
    if seed is not None:
        random.seed(seed)
    hero = make_hero()
    noun = pick(GREEK_NOUNS)
    verb = pick(GREEK_VERBS)
    adj = pick(GREEK_ADJ)
    glyphs = glyph_cluster(random.randint(1,3))
    alien_breath = pick(ALIEN_SOUNDS)
    refrain = pick(REFRAINS)

    lines = []
    # line 1: invocation
    lines.append(f"Ὦ {hero}, ὁ τῆς {greekize(noun)} φύλαξ {glyphs}")
    # line 2: action
    lines.append(f"— {verb} ἐπὶ τὸν {adj}· {alien_breath}·{glyphs}")
    # line 3: enigmatic clause
    lines.append(f"καὶ ἔσχατον σημεῖον: «{glyphs}{pick(GREEK_NOUNS)}»")
    # refrain
    lines.append(f"{refrain}")
    return "\n".join(lines)

def chorus(loop_index):
    """A repeating chorus that slightly mutates each cycle for variety."""
    base = "Χορός τῶν ὕλων —"
    echo = glyph_cluster(2 + (loop_index % 3))
    chant = pick(ALIEN_SOUNDS)
    return f"{base} {echo} {chant}"

def slow_print(text, delay=0.0):
    """Print but allow for optional per-line small delays."""
    for line in text.splitlines():
        print(line)
        sys.stdout.flush()
        if delay:
            time.sleep(delay)

def main():
    # friendly heading
    print("ὝΜΝΟΣ — The Endless Hymn (press Ctrl+C to exit)\n")
    time.sleep(0.8)

    # use an infinite iterator for counts
    for i in itertools.count(1):
        try:
            # produce a block (stanza + chorus)
            s = stanza()
            c = chorus(i)
            separator = "\n" + ("─" * 36) + "\n"
            slow_print(s, delay=0.5)       # small per-line drift
            print(separator)
            slow_print(c, delay=0.5)
            print("\n")                     # blank line between cycles
            # sleep a small random interval to avoid burning CPU and create rhythm
            pause = random.uniform(0.8, 2.2)
            time.sleep(pause)
        except KeyboardInterrupt:
            print("\n\nἈνάπαυλα — the hymn pauses. Farewell, wanderer.")
            break

if __name__ == "__main__":
    main()
