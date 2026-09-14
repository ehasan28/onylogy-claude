# Onylogy Claude Skills

A collection of [Claude Code](https://claude.com/claude-code) skills. Each skill lives in
its own folder under `skills/` and is a self-contained `SKILL.md` (plus optional reference
files) that Claude loads automatically when the task matches its description.

## Skills

| Skill | What it does |
|---|---|
| [`onywrites`](skills/onywrites/SKILL.md) | Writes blog posts, or rewrites existing ones, so they read as human-authored rather than AI-generated. Built on the structural findings of [StoryScope](https://arxiv.org/abs/2604.03136) (Russell et al., COLM 2026) rather than surface wordlists, which the same paper shows barely affect detection. |
| [`nu-term-paper`](skills/nu-term-paper/SKILL.md) | Writes a complete National University of Bangladesh (জাতীয় বিশ্ববিদ্যালয়) Bangla sociology term paper from a title, in the exact NU format (front matter, five chapters ১.১–৫.৩, footnotes, গ্রন্থপঞ্জি), with verified sources and a Word/PDF/Bijoy build pipeline. Includes the playbook, manuscript skeleton and build tooling. |

## Installing a skill

Copy the skill's folder into your Claude Code skills directory:

```bash
git clone https://github.com/ehasan28/onylogy-claude-skills.git
cp -R onylogy-claude-skills/skills/onywrites ~/.claude/skills/onywrites
cp -R onylogy-claude-skills/skills/nu-term-paper ~/.claude/skills/nu-term-paper
```

Restart Claude Code, or start a new session, and the skill is available. It triggers
automatically when a request matches its description, or invoke it directly with
`/onywrites` or `/nu-term-paper`.

To install into a single project instead of globally, copy the folder to
`.claude/skills/` inside that project's repository.

## Structure

```
skills/
  <skill-name>/
    SKILL.md          required: frontmatter (name, description) + instructions
    references/        optional: supporting docs the skill loads on demand
    (a skill may also ship extra folders, e.g. nu-term-paper/skeleton and tooling)
```

## License

MIT. See [LICENSE](LICENSE).
