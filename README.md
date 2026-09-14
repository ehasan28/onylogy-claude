# Onylogy Claude

Claude Code skills and systems by Onylogy.

- **Skills** live under `skills/<name>/` — a self-contained `SKILL.md` (plus optional
  `references/`) that Claude loads automatically when a task matches its description.
- **Systems** live at the repository root — larger packages (playbooks, templates, build
  tooling) that a skill points to.

## Skills

| Skill | What it does |
|---|---|
| [`onywrites`](skills/onywrites/SKILL.md) | Writes blog posts, or rewrites existing ones, so they read as human-authored rather than AI-generated. Built on the structural findings of [StoryScope](https://arxiv.org/abs/2604.03136) (Russell et al., COLM 2026) rather than surface wordlists, which the same paper shows barely affect detection. |
| [`nu-term-paper`](skills/nu-term-paper/SKILL.md) | Writes a complete National University of Bangladesh (জাতীয় বিশ্ববিদ্যালয়) Bangla sociology term paper from a title, in the exact NU format (front matter, five chapters ১.১–৫.৩, footnotes, গ্রন্থপঞ্জি), with verified sources and a Word/PDF/Bijoy build. Thin wrapper over the `nu-term-paper-system/` system below. |

## Systems

| System | Contents |
|---|---|
| [`nu-term-paper-system/`](nu-term-paper-system/) | `term-paper-write.md` (the full playbook: intake, research protocol, 100 % structure spec, voice, build & QA, delivery, Google Docs), `skeleton/` (manuscript with every fixed template string), `tooling/` (docx builder with footnotes, TOC page map, Bijoy/SutonnyMJ conversion, verification sheet), `references/`. |

## Installing

```bash
git clone https://github.com/ehasan28/onylogy-claude.git
cp -R onylogy-claude/skills/onywrites ~/.claude/skills/onywrites
cp -R onylogy-claude/skills/nu-term-paper ~/.claude/skills/nu-term-paper
```

Restart Claude Code, or start a new session, and the skills are available. They trigger
automatically when a request matches their description, or invoke them directly with
`/onywrites` or `/nu-term-paper`.

`nu-term-paper` needs the system folder too: keep the cloned repository (or at least
`nu-term-paper-system/`) somewhere permanent and set the path at the top of its `SKILL.md` —
or simply install the system folder itself as the skill:

```bash
cp -R onylogy-claude/nu-term-paper-system ~/.claude/skills/nu-term-paper
```

To install into a single project instead of globally, copy the skill folder to
`.claude/skills/` inside that project's repository.

## Structure

```
skills/
  <skill-name>/
    SKILL.md          required: frontmatter (name, description) + instructions
    references/       optional: supporting docs the skill loads on demand
<system-name>/        optional: a larger package a skill depends on (playbook, templates, tooling);
    SKILL.md          it carries its own SKILL.md + references/ so the folder is also installable as a skill
```

## License

MIT. See [LICENSE](LICENSE). Third-party assets keep their own licences (e.g. the Siyam Rupali
font in `nu-term-paper-system/tooling/` is GPL).
