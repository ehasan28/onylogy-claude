# Evidence base

Source: Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, John Wieting.
*StoryScope: Investigating idiosyncrasies in AI fiction.* COLM 2026. arXiv:2604.03136v6.
University of Maryland + Google DeepMind. Code/data: github.com/jenna-russell/storyscope

## What the study actually did

10,272 human-written short stories from Books3. For each, a writing prompt was
reverse-engineered and given to five LLMs: Claude Sonnet 4.6, GPT-5.4, Gemini 3 Flash,
DeepSeek V3.2, Kimi K2.5, producing six parallel versions of every prompt. 61,608 stories
total, mean length 4,753 words. Each story was scored on 304 interpretable discourse-level
features across ten NarraBench dimensions (agents, plot, events, setting, temporal
structure, revelation, perspective, social networks, situatedness, style). XGBoost
classifiers plus SHAP attribution identified which features separate sources.

Feature extraction was validated: mean human–model Cohen's κ = 0.84, which is *higher* than
human–human agreement on the same items (0.74).

## Scope limit: read this before applying anything

**This is a study of fiction.** Its features are narrative: subplots, protagonist agency,
flashbacks, characters, resolution mode. A large fraction does not transfer to blog writing
at all, and transplanting it literally produces nonsense. A blog post does not need a
morally ambivalent protagonist.

What transfers is the *class* of finding: AI over-explains its own meaning, tidies its
structure, over-renders sensory detail, avoids naming real things, and does not acknowledge
its reader. Those hold for any prose. The skill's rules are that translation, and the
percentages below are the fiction-domain evidence for them: directional support, not
blog-domain measurements. Do not quote these numbers as if they were measured on blog posts.

## Headline results

| Model | Features | Binary macro-F1 |
|---|---|---|
| Narrative only (no style at all) | 257 | **93.2%** |
| Narrative + style | 304 | 96.0% |
| Style only | 39 | 85.8% |
| 30 core narrative features only | 30 | 84.8% |
| Human-length-matched test set (narrative) | 257 | 93.2%, unchanged |

Narrative structure alone retains **over 97%** of the full model's performance. Detection is
not a length artifact: a classifier on word count alone gets 55.9%, and the narrative model
scores identically before and after length matching.

## The result that decides the strategy

AI stories were run through LAMP, a span-level rewriter that identifies and removes seven
categories of AI writing artifact (cliché, redundant exposition, purple prose and others)
using 25 few-shot examples from professional writers.

| | macro-F1 |
|---|---|
| Original Gemini stories | 95.5% |
| After removing surface artifacts | 93.9% |

**A 1.6-point drop.** The authors: editing out clichéd phrasing or purple prose "does not
alter the structural narrative choices that drive our classifier."

Two corollaries for the skill:
- Post-hoc humanizing passes are close to worthless. Structure must be decided up front.
- Surface tells are explicitly described as *fleeting*. GPT-5.4 already cut em-dash usage
  after it became a known signal. Any wordlist ages out. Structure does not.

Separately: fine-tuning to mimic human style drops detection on creative writing from 97% to
3% (Chakrabarty et al. 2026), but that is a training intervention, not something a prompt
can reach.

## Core features, human vs AI means (Table 16)

Scale features `s` are 1–5 Likert means. Ordinal `o` are means over integer codes. `→`
marks a categorical option, given as prevalence %. Gap = Human − AI. Negative = AI-elevated.
AI column averages all five models.

### AI-elevated: thematic over-determination
| Feature | Human | AI | Gap |
|---|---|---|---|
| Thematic Explicitness & Moralizing `s` | 3.28 | 3.94 | −0.65 |
| Moral / Philosophical Weighting `s` | 3.26 | 3.68 | −0.42 |
| Thematic Unity `s` | 4.41 | 4.74 | −0.33 |
| Narratorial Thematic Commentary → yes | 52% | 77% | −25 |
| Dialogue Function → philosophical debate | 34% | 59% | −25 |
| Reference Explicitness → implicit echoes | 50% | 72% | −22 |

→ Blog translation: AI states its own takeaway, wraps each section with the lesson, stages
balanced "some say / others say" debate, and gestures vaguely instead of naming things.
This is the largest cluster in the paper and the highest-value thing to fix.

### AI-elevated: sensory and embodied performativity
| Feature | Human | AI | Gap |
|---|---|---|---|
| Emotional Expression → embodied | 38% | 81% | −42 |
| Setting as Psychological Mirror `s` | 3.58 | 4.07 | −0.49 |
| Environmental & Ecological Emphasis `s` | 2.83 | 3.21 | −0.38 |
| Sensory Modalities → olfactory | 57% | 82% | −26 |
| Sensory Density `s` | 3.66 | 3.93 | −0.26 |
| Depth of Interior Access `s` | 3.67 | 3.93 | −0.26 |

→ The −42 on embodied emotion is the single widest gap in the table. Note this inverts the
usual "show, don't tell" advice: *humans tell*. Humans use explicit emotion labels 29% of the
time vs 8% for AI. AI renders fear as a tightening chest and dimming lamplight; a human
writes that the character was afraid.

### AI-elevated: structural streamlining
| Feature | Human | AI | Gap |
|---|---|---|---|
| Causal Chain Continuity `s` | 3.92 | 4.20 | −0.28 |
| Spatial Granularity `o` | 2.27 | 2.53 | −0.26 |
| Agency in Resolution → protagonist choice | 46% | 69% | −23 |
| Character Introduction → external description | 30% | 52% | −22 |
| Subplot Integration → no subplots | 57% | 79% | −22 |
| Resolution Mode → internal understanding | 27% | 47% | −21 |
| Opening Spatial Grounding `o` | 2.12 | 2.33 | −0.20 |
| Pre-Threat Character Investment `s` | 2.76 | 2.99 | −0.23 |

→ Blog translation: tidy single-track argument, no digressions, everything resolves, heavy
scene-setting before the point arrives, no loose ends.

### Human-elevated: intertextual richness
| Feature | Human | AI | Gap |
|---|---|---|---|
| Intertextual Strategy → explicit named reference | 47% | 24% | +23 |
| Reference Explicitness → balanced mix | 37% | 16% | +21 |

→ Humans name specific texts, authors, works, brands and places at roughly double the rate.
AI avoids naming real things. In a blog this is the difference between "a popular caching
plugin" and "WP Rocket 3.16, $59/year".

### Human-elevated: reader engagement
| Feature | Human | AI | Gap |
|---|---|---|---|
| Fourth-Wall Permeability `o` | 0.67 | 0.39 | +0.28 |
| Direct Reader Address `o` | 0.28 | 0.07 | +0.21 |

→ The paper's phrasing: human writing "acknowledges its audience as a co-participant"; AI
"writes as though no one is watching."

### Human-elevated: temporal complexity
| Feature | Human | AI | Gap |
|---|---|---|---|
| Depth of Recontextualization After Surprise `s` | 3.28 | 2.95 | +0.34 |
| Chronological Discontinuity `s` | 2.40 | 2.12 | +0.28 |
| Nonlinear Framing for Delayed Disclosure `s` | 1.96 | 1.68 | +0.28 |
| Anachrony Intensity `s` | 2.58 | 2.31 | +0.27 |

→ The paper's example: a human mystery opens at the funeral and spirals backward through
decades; AI tells it from first clue to grand reveal. Blog equivalent: open at the outcome
or the breakage, then go back.

### Human-elevated: narrative diversity
| Feature | Human | AI | Gap |
|---|---|---|---|
| Location Variety Scope `o` | 1.34 | 1.08 | +0.26 |
| Dialogue-to-Narration Proportion `s` | 2.95 | 2.70 | +0.24 |
| Subplot Integration → thematically parallel | 42% | 21% | +22 |
| Moral Polarity → ambivalent/mixed | 59% | 38% | +21 |
| Emotional Expression → explicit labels | 29% | 8% | +21 |

## Convergence and rarity

The five AI models occupy one shared region of narrative space, distinctly separate from
human writing:

- Mean human↔AI centroid distance is **1.6×** the mean AI↔AI distance (6.6 vs 4.3).
- Even the *closest* human–AI pair is farther apart than the *most distant* AI–AI pair
  (6.2 vs 6.0). Human writing is a different region, not a wider version of the AI one.
- Human stories are more dispersed: mean distance to own centroid 22% greater (33.2 vs 27.4).
- Per-story rarity (mean distance to 25 nearest neighbours): human mean percentile **0.71**
  vs AI **0.49**, Cohen's d = 0.83.
- 24.7% of human stories fall in the rarest 10% corpus-wide, vs 7.1% of AI stories.
- Given six versions of one prompt, the human version is the rarest of the six **57.8%** of
  the time (chance = 16.7%).
- All six most-confused source pairs in the six-way classifier are AI↔AI.

→ This is the basis for the "discard the obvious angle" rule. The obvious angle is where
every model converges. It is also why detection is hard to escape by switching models:
they cluster together.

Caveat worth keeping in view: the distributions overlap substantially, and the rarest 10% of
the corpus still contains 487 AI stories against 340 human ones. Rarity is a strong tendency,
not a boundary.

## Claude's fingerprint (Table 17)

Claude had the most distinctive narrative profile of the five models, with 26 fingerprint
features, second only to human (32), against 11 for GPT, 11 for Gemini, 7 for DeepSeek and 3
for Kimi. Ranked by uniqueness ratio vs the next-best class:

| # | Feature | SHAP | Uniqueness |
|---|---|---|---|
| 1 | Strength of event escalation | 0.402 | **22.4** |
| 2 | Event-type diversity | 0.491 | 10.7 |
| 3 | Ending temporal scope → epilogue/flashforward | 0.096 | 8.9 |
| 4 | Dreams/visions as temporal distortion → no | 0.116 | 7.7 |
| 5 | Setting mood → uncanny/haunted | 0.059 | 4.6 |

Plus 21 more: event density, conflict modality, relationship trajectory, heteroglossia,
closure.

Prose description from the paper: Claude's stories "are defined by restraint: event intensity
escalates less than in any other source, and narrative voice is the most uniform." Claude
"takes a reverent/continuist approach to literary tradition, honoring and extending
storytelling conventions rather than subverting or challenging them", 62% of Claude stories
vs 39–56% across other sources, and favours "quiet endings over avalanche endings."

Event escalation at uniqueness 22.4 is the highest single value in the entire fingerprint
table across all six sources. Flat intensity is the most Claude-specific thing about Claude.
This is why the skill has a dedicated Claude-correction pass.

For contrast, other models' top tells: GPT uses gossip and rumour as a plot mechanism (64% vs
44–55%) and frames stories as distant retrospection. Gemini produces the tidiest endings,
extended denouements, and the bleakest settings (88% bleak/oppressive). DeepSeek front-loads
context others withhold. Kimi has almost no fingerprint at all. It sits at the generic
centre of the AI distribution.

## Things this evidence does not support

- That any of this defeats a detector. Text-based baselines in the paper hit 99.7–99.9%
  macro-F1 on raw text; ModernBERT fine-tuned on the corpus reached 99.9%. Supervised
  detectors with in-domain training data are far stronger than the narrative model. The
  goal here is writing that is genuinely better and reads as authored, not evading
  classification, which this cannot promise.
- That these numbers apply to blog posts. See the scope limit above.
- That surface wordlists matter much. They are explicitly transient.
- That AI writing is bad writing. The measured differences are systematic, not qualitative;
  a separate cited result found readers *preferred* outputs of AI trained on copyrighted
  books over expert human writers (Chakrabarty et al. 2026).
