# The Impossible Atlas: Asset Pipeline v1
Updated: 2026-10-12
Status: static artwork and extraction validated by user inspection; animation and in-engine delivery NOT validated.

## Golden rules
- Work in a separate lab. Do not alter the original Tokyo corridor without explicit approval.
- One bite at a time. Art approval comes before processing.
- Preserve the original Gemini output and approved character design. No silent regeneration or substitutions.
- No claims of deployment or gameplay success until the live iPhone URL is opened and tested.
- Keep source files, processed PNGs, and inspection previews distinct.
- Never treat a committed file as proof that its images load.

## Pipeline
1. **Art generation:** Gemini makes one asset using approved game references.
2. **Art review:** approve style, silhouette, scale, and perspective. No cleanup yet.
3. **Extraction:** remove baked checkerboard / background / floor for sprite assets; preserve original art.
4. **Edge cleanup:** inspect on dark AND light backgrounds at native and enlarged scale. Remove JPEG halos without erasing clothing, collars, glow, or outlines.
5. **User approval:** only user-approved version is canonical.
6. **Animation (unproven):** produce coherent frames with consistent identity, dimensions, baseline, and real motion.
7. **Sprite packing (unproven):** exact cell boundaries, no frame bleed, alpha PNG, documented fps and anchor.
8. **Phaser lab (unproven):** load all hosted assets, inspect scaling, looping, collision, and mobile controls.
9. **Deployment verification (unproven):** check Cloudflare live URL on iPhone. No downloads, file selectors, or missing assets.

## Test results
| Asset | Art | Processing | Notes |
| --- | --- | --- | --- |
| Cigarette vending machine | Approved | Approved | Gemini added checkerboard and floor; extracted original art |
| Open AnI security guard | Approved | Approved V3 | White JPEG fringe remained after first two passes; V3 approved |
| Laser gate | Approved | Approved | Two pillars and red glow preserved |
| Cigarette pack | Approved | Approved | Need 32×32 readability test in Phaser |
| Tokyo office corridor | Strong cinematic art | Not processed | One-point perspective is unsuitable as a side-scrolling gameplay background; preserve for cinematic/transition use |

## Animation experiment
- Gemini produced seven guard poses when asked for eight, with repeated leg positions and incomplete gait. Character design remained fairly consistent.
- Grok output suffered character drift and was not usable.
- **Do not mark animation as solved.** Next experiment: isolate the seven original Gemini poses, inspect them individually, measure gait differences, and test a timed loop in a standalone lab. Reject if the motion is unconvincing. Do not burn more generations until this test is evaluated.

## Acceptance checklist
- [ ] Exact approved artwork preserved
- [ ] True transparency, not checkerboard pixels (sprites)
- [ ] No visible white/gray halos on contrasting backgrounds
- [ ] Consistent scale and perspective
- [ ] Animation frames are distinct, aligned, and loop without identity drift (animated assets)
- [ ] Works at actual in-game display size
- [ ] Hosted images load automatically in live Phaser lab on iPhone
- [ ] User explicitly approves before integration

## Workflow lesson
Gemini is a promising *artist*, not yet a reliable *animator*. Deterministic cleanup can rescue static assets. Processing, hosting, and game integration are separate gates. Never conflate a tool success with a playable result.
