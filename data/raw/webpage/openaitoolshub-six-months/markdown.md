Karpathy's LLM Wiki, Six Months In: My Honest Setup with Obsidian + Claude
After 6 months running Karpathy's LLM wiki across 35 pages, here's what worked, what didn't, and how Rohit's v2 changed my Obsidian setup. See my pitfalls.
TL;DR
- I've been running the Karpathy LLM wiki pattern in Obsidian for six months across 35 pages, edited mostly by Claude.
- The pattern works — far better than I expected — but only if you treat the schema file as the most important file, which Karpathy's original gist underplays.
- Rohit Ghumare's v2 (added Memory Lifecycle, typed relationships, quality controls) fixed three quiet failure modes I kept hitting in v1.
- Skip the Postgres + Dream Cycle stuff (GBrain) until your wiki crosses ~500 pages. At 35, plain markdown + grep is faster.
- I lost about a week of compounded value to four pitfalls that aren't in any of the original write-ups. They're in this post.
Who I Am, and Why I Run an LLM Wiki
I'm Jim Liu, an independent developer in Sydney. I run openaitoolshub.org and eight other sites, mostly solo. My problem isn't generating notes — Twitter bookmarks, RSS, podcast clips, Claude transcripts pile up faster than I can read. My problem is compounding them so the next time I'm asked "what did you decide about X six weeks ago?", I have a real answer instead of a vibe.
I tried Notion for a year. I tried plain Obsidian for another. Neither lasted because the maintenance burden — adding backlinks, fixing stale claims, marking contradictions — always fell on me, and I always lost. Karpathy's December 2025 gist on the LLM wiki pattern was the first proposal that flipped that: the LLM maintains the wiki, the human investments are inputs and questions. That single inversion is why this stuck when nothing else did.
If you've seen the gist or Andrej Karpathy's original LLM wiki notes and weren't sure whether it was hand-wavy theory or actually deployable, this post is the boring real-world version: what the directory looks like, what schema fields you actually need, and what breaks at month three when the file count grows.
What the Karpathy LLM Wiki Actually Looks Like (After Six Months)
📖 The pattern in one sentence: a three-layer markdown repo (raw/ for immutable inputs, wiki/ for LLM-compiled pages, schema.md for the rules) where Claude — not me — does almost all the editing.
Concretely, my repo today:
wiki/
├── raw/                   # 80 articles ingested verbatim, never edited
│   ├── articles/          # blog posts, gists, transcripts
│   └── repos/             # GitHub repo READMEs I copied in
├── wiki/                  # 35 LLM-compiled pages
│   ├── concepts/          # 14 reusable mental models
│   ├── tools/             # 8 software profiles
│   ├── people/            # 4 person profiles
│   ├── insights/          # 5 my-own analytical pieces
│   ├── originals/         # 4 verbatim user-thought captures
│   └── indexes/           # concept-index.md, lint reports
├── log.md                 # append-only operation log
└── schema.md              # filing rules, field definitions, lint protocols
📊 The compounding behavior is real. When I ingest a new article on, say, AI agent memory, Claude touches an average of 8–12 existing pages: adds backlinks, updates the concepts index, flags one contradiction with a six-month-old note, refines a TL;DR. I haven't measured the file edit count rigorously — my log.md says the median ingest touches 9 files — but it lines up with what the original gist calls the ripple effect.
The other thing nobody warns you about: TL;DR enforcement saves your context window more than the index does. Every page in my wiki has a ≤50-character TL;DR at the top. When I ask Claude "what did I decide about RAG vs LLM wiki?", it can scan 35 TL;DRs in a single read instead of trying to compress 35 full pages. Karpathy's gist mentions the TL;DR-on-top idea once; in practice it's load-bearing.
How I Set Mine Up (And Where I Diverge From the Gist)
I'm not going to walk through "install Obsidian" — anyone reading this can do that. The interesting choices are:
🧭 What I kept from Karpathy v1:
- Three folders only at the top of wiki/: my version isconcepts/,tools/,people/. Not 14 like GBrain. Fewer folders = fewer "where does this go?" decisions.
- log.mdas append-only. Every ingest, lint, contradiction-mark, or page-rewrite gets a one-line entry with a UNIX timestamp prefix. I- grepthis file more than I expected — about twice a week.
- Schema first, content second. I wrote schema.mdbefore I had 5 pages. It defines the frontmatter fields, the canonical slug rules, the contradiction-resolution protocol. This is the part most write-ups skip and the part that matters most. Rohit Ghumare put it bluntly: "Schema is the most important file." He's right.
🧭 What I added from Rohit's v2:
- Memory Lifecycle frontmatter: every page has last_verified: 2026-05-01,confidence: high|medium|low, and (when relevant)superseded_by: another-page.mdorcontradicts: an-older-claim.md. v1 has none of these. After three months I had pages with stale ChatGPT pricing claims sitting next to fresh ones, both confidently asserted. The lifecycle fields fixed it.
- Typed wikilinks: instead of plain [[obsidian]], I write[[obsidian]] (uses)or[[gbrain]] (alternative-to). Six relationship types total. It feels fussy at first; by month two it lets Claude give much sharper answers because the graph isn't just "X is connected to Y" but "X uses Y" or "X contradicts Y".
- Contradiction protocol: when Claude finds a new claim that contradicts a wiki page, the rule is don't overwrite, mark. Add contradicts:field, keep both, surface during lint. This is the change I appreciate most. (Pitfall #3 below is the day I broke this rule.)
🧭 What I skipped:
- Hybrid search (BM25 + vector + graph). The Rohit v2 essay recommends it. At 35 pages, grep -r "keyword" wiki/returns in 40ms. I'll revisit at 500 pages.
- GBrain's Postgres + Dream Cycle. Garry Tan's GBrain stack deploys at 14,700+ files with nightly cron consolidation. Beautiful engineering. Total overkill for me right now. Markdown + manual weekly lint is good enough until at least 500 pages, probably 1,000.
- Multi-agent mesh. A team-scale concept. Solo, I don't need it.
What Surprised Me (Rohit v2 vs GBrain vs Plain v1)
⚖️ Here's the honest comparison after running variants of all three:
| Dimension | Karpathy v1 | Rohit v2 | GBrain (Garry Tan) | What I Actually Run | 
|---|---|---|---|---|
| Storage | Markdown | Markdown + lifecycle fields | Postgres + pgvector + markdown | Markdown + lifecycle fields | 
| Search | grep | grep + typed graph | Hybrid (BM25 + vec + graph) | grep + manual graph view | 
| Lint | Manual | Quality-control protocol | Nightly Dream Cycle cron | Weekly manual lint | 
| Originals | Not addressed | Not addressed | Dedicated originals/folder | Dedicated originals/folder | 
| Best for | <100 pages | 100–500 pages | 1,000+ pages, ops-grade | 35 pages, solo | 
| Maintenance | ~5 min/day | ~10 min/day | Cron-driven, ~0 | ~15 min/day | 
The real surprise: Karpathy's v1 has a hole around capturing your own thoughts, and GBrain's originals/ folder is the patch. v1 implicitly assumes you're ingesting external articles. But the highest-value content I generate is my own takes — the contrarian read on a paper, the framework I improvised in a Slack DM. Without an originals/ folder those go into Notion drafts and die.
⚖️ The other surprise: I write better with the wiki than I did without it. When I sit down to publish a blog post (this one, for instance), I grep my wiki for the relevant concepts, pull TL;DRs into context, and Claude drafts with citations to my own prior thinking. The "compounding asset" framing isn't a metaphor — it's a real productivity loop. My drafts now reference my own historical decisions, which is the move that makes the writing feel grounded instead of generic.
4 Pitfalls I Hit (And What I'd Do Differently)
- Month 2 — I forgot to lint after big ingest weeks. I'd dump 6–8 articles into - raw/over a Saturday, watch Claude generate new pages, and skip the weekly- lintpass because everything looked tidy. By month 3 I had three orphan pages with no inbound links and one contradiction sitting unmarked between two- concepts/files. Cost: about a week of "wait, what's the current view?" confusion. Lesson: lint protocol isn't optional, even when nothing looks broken. Karpathy's v1 calls this out; I just didn't internalize it.
- Month 3 — I let Claude "smooth" content in - originals/. I had a hot take written in my own messy phrasing — something like "knowledge compounding ≠ knowledge hoarding". Claude, doing its usual editing pass, rewrote it to "compound knowledge effectively". Cleaner prose, completely lost the original cognitive shape. Lesson:- originals/is verbatim-only. I added a- do-not-rewritetag and updated- schema.mdto forbid LLM edits in that folder. The language is the insight — that's the whole point of the folder.
- Month 4 — I overwrote a contradiction instead of marking it. I had an old wiki page claiming "RAG is the right architecture for personal knowledge bases." A new article I ingested said the opposite (LLM wiki replaces RAG). I let Claude rewrite the old page to match. Wrong move. Two months later I needed the old reasoning to argue with someone, and it was gone. Lesson: contradictions are assets, not errors. I now explicitly run - contradicts:and keep both versions. Rohit v2 is right about this and v1 is silent.
- Month 5 — I changed tools without re-reading - schema.md. I migrated from one note app to Obsidian and forgot that my schema specified- aliasesfield for canonical slug deduplication. The migration script didn't carry the field. Result: two pages on the same person under different slugs (- karpathy.mdand- andrej-karpathy.md), Claude treated them as different entities, recommendations got weird. Lesson: any tool change starts with re-reading- schema.mdand writing a migration plan. Schema first, content second, tooling third.
Methodology: How I Got the Numbers in This Post
📊 Sample: my own personal LLM wiki, 35 wiki pages + 80 raw inputs, deployed November 2025 to May 2026 (six months).
Data sources:
- wiki/log.md— append-only operation log, every ingest/lint/edit timestamped
- Obsidian's built-in graph view — backlink count snapshots
- Claude Code session transcripts (I save them in raw/sessions/for the same reason I save articles)
- My personal time tracker (Toggl) for the maintenance-time numbers
I ingest 1–3 articles per day on average. I lint weekly (Sunday morning, ~20 min). I publish to my blog roughly once a week, drawing from the wiki. The "8–12 pages touched per ingest" figure is the median over the last 30 ingests; the spread is 4 to 23.
This isn't a controlled study — sample size 1, no comparison group. But it's directional, and it's mine. I share the wiki structure publicly under Brain-First Lookup Protocol in my openaitoolshub.org CLAUDE.md so anyone can audit the schema choices.
Who Should (and Shouldn't) Try This Pattern
🧭 You should try Karpathy's LLM wiki pattern if:
- You generate or consume more than 5 pieces of content per week (articles, podcasts, transcripts).
- You've tried Notion / Roam / Obsidian solo and abandoned it because of maintenance burden.
- You already have an LLM workflow you trust (Claude Pro, ChatGPT Plus, Cursor, etc.) — you're not adding a new dependency.
- Your knowledge has a temporal dimension that matters: you need to know what you thought six months ago, not just what's true today.
🧭 You probably shouldn't if:
- You have fewer than ~30 inputs total. The compounding only kicks in past some critical mass; below that, plain notes are fine.
- Your knowledge is mostly transactional (recipes, contact info, passwords) rather than analytical. A wiki overpowers a database.
- You're in a regulated field (legal, medical, financial advisory). The contradictions-as-assets philosophy clashes with compliance requirements that demand single-source-of-truth.
- You won't write a schema.md. Without it, the wiki devolves into a graveyard within two months. I've watched this happen to friends.
FAQ
What's the difference between the Karpathy LLM wiki and a RAG system?
RAG retrieves chunks from documents at query time and synthesizes a fresh answer each time. The Karpathy LLM wiki pre-compiles the synthesis into stable markdown pages with explicit cross-references. RAG repeats work; the wiki accumulates it. For personal knowledge management at <500 pages, the wiki is faster, cheaper, and produces more coherent answers. RAG wins above ~10K documents where pre-compiling is impractical.
Do I need Obsidian, or will any markdown editor work?
Any markdown editor works. Karpathy's original gist doesn't require Obsidian. I use it because the graph view and backlink panel are useful when manually lint-checking. VS Code with markdown preview plus a [[wikilink]] extension does 90% of the same job for free.
How is the Karpathy LLM wiki different from a "second brain" (Tiago Forte's PARA, Building a Second Brain)?
PARA is a filing system for humans. The Karpathy LLM wiki is a filing system for an LLM, which happens to also work for humans. The key difference: BASB asks you to do the maintenance work. The LLM wiki asks Claude to do it. That single inversion changes whether the system survives month three.
Why didn't you go with GBrain's full Postgres + Dream Cycle setup?
I'll switch when my page count crosses ~500 and grep starts feeling slow. Currently it returns in <50ms. GBrain is built for 14K+ file deployments with nightly cron consolidation. At my scale it's beautiful infrastructure with nothing to do.
How much does this cost to run?
Obsidian: free. Claude Pro: $20/month, which I'd pay anyway. My total marginal cost over six months: $0. The "expensive" version is the time investment — about 15 minutes a day, which I net-recover from faster writing.
About the Author
Jim Liu is an independent developer based in Sydney. He runs openaitoolshub.org and eight other sites, all built and maintained solo. He's been running Karpathy's LLM wiki pattern in Obsidian since November 2025 and writes about AI tools, developer workflows, and the practical economics of solo software businesses. Read more of his work in the AI Coding Tools Guide or his Claude Code Memory deep dive.