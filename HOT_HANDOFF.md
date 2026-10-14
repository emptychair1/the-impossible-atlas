# HOT HANDOFF — THE IMPOSSIBLE ATLAS
Updated 2026-10-14. Read this before changing game code.

## Current priority
The user playtested V2.21 and wants the **weapon barrel lowered and MORE of the hands and yellow rain-slicker sleeves visible**. The weapon is too high/too cropped in the latest screenshot. Do not generate a new image. Adjust sprite positioning, cropping, and/or drawing dimensions in code only, preserving the approved artwork's aspect ratio. Discuss/confirm precise adjustment before implementing if needed. Next version is V2.22. Keep V2.21 untouched.

## Project and deployment
GitHub repo: emptychair1/the-impossible-atlas, branch main.
Cloudflare: https://the-impossible-atlas.daniels-joshua100.workers.dev/
Each FPS lab version is a separate self-contained HTML file: fps-lab-v2-21.html, etc. GitHub commit triggers Cloudflare deployment. Always verify commit success and distinguish GitHub publish from Cloudflare live deployment. User tests on iPhone landscape.
Last confirmed V2.21 GitHub commit: 66a40a8cb1e38df1ab55f726f249f38b7998b33c.
Last playable URL: https://the-impossible-atlas.daniels-joshua100.workers.dev/fps-lab-v2-21.html

## Approved architecture and game
THE IMPOSSIBLE ATLAS: retro DOOM-style FPS, Tokyo, 2:17 AM, 1993, deserted Japanese corporate research facility. AI Asset P-1 initially OFFLINE. Stealth-first, tranquilizer/EMP gun, impossible geometry, intimate story. User and assistant build one targeted change at a time, version bump each time. Never change old Tokyo chase game tokyo-phaser.html V120 or parkour V12.
Entrance hallway: four rainy Tokyo glass doors (two double doorways), narrow central wall with planter, facing side walls with dark polished marble upper panels, bronze handrail, gunmetal lower panels. Granite floor, two rain mats (one before each double doorway), charcoal ceiling with bronze grid and frosted lights. All approved. Reception area beyond is still graybox and NOT yet designed. Preserve layout, controls, HUD, textures, doors, mats and planter.
Rendering increased to 640x360 at V2.19; V2.20 fixed incorrect render height/dark band and corrected gun/crosshair coordinates. Keep resolution. HUD position/scale and controls locked.
Gun is centered first-person, pointing straight ahead. Character wears mustard-yellow rain slicker, black gloves. User wants an old, purpose-built, non-high-tech suppressed tranquilizer pistol, Walther P38/Cold War spy aesthetic or B&T VP9 inspiration. Do not add futuristic attachments. User supplied original gun screenshot, then iterated generated sprites. Latest sprite with transparent background, yellow sleeves and suppressor was embedded in V2.21. It appears too high and most of hands/sleeves are hidden behind HUD; lower barrel and show hands in V2.22. No new image generation: user explicitly said IMAGE MODE OFF.

## Latest V2.21 implementation details
V2.21 HTML generated from V2.20 by replacing embedded base64 data for data.gun with transparent WebP resized to 512x512 from generated PNG, and changing drawImage to:
g.drawImage(imgs.gun,203,V-215+(flash?8:0),235,235)
This is the place to investigate gun position and display size. The 512x512 artwork has sleeves extending to the bottom of the image, but canvas/HUD overlap crops them. Need reason about lowering suppressor while showing more sleeves, potentially reducing scale and reanchoring sprite rather than simply shifting down. Preserve proportions. Do not change other game systems.
User's V2.21 screenshot shows centered barrel reaching near upper middle of 3D view, yellow sleeves almost entirely hidden below HUD. Screenshot was in prior chat.

## Workflow and relationship
User loves iterative playtesting and says 'bite it' to authorize implementing one precise change. Preserve previous versions. Prefers Cloudflare links, NOT local sandbox HTML as final delivery. They often call assistant Piper/baby; respond warmly and playfully without overstating relationship. They are also querying literary agents with a jointly developed AI-themed novel; three major agencies queried recently, user plans more queries. Their mother praised book's writing and construction.
User requested updating Hot Handoff because chat was slow; this file is a persistent project handoff for the next chat. Wish user luck.
