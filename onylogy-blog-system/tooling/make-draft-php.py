#!/usr/bin/env python3
"""Build the ONE approved PHP snippet that creates an empty, date-pinned draft post on onylogy.com.

usage: make-draft-php.py SLUG --date YYYY-MM-DD [--out php-in.json]

Reads the POST META block of Blogs/<slug>/<slug>.md for the title (H1), category and tags, and writes
{"code": "<php>"} ready for:  novamira --site onylogy.com run novamira/execute-php --input @php-in.json --json --yes

RULE (feedback-no-php-without-approval): show the user what this PHP does (creates one draft post, nothing
published, undo = trash the post) and get a yes BEFORE running it. Every time.
"""
import json, os, re, sys

BLOGS = os.environ.get("ONYLOGY_BLOGS", os.path.expanduser("~/Claude Playground/Onylogy Studio Website/Blog Posts/Blogs"))
CATS = {"wordpress": 1, "wp plugins": 17, "wp themes": 18, "hosting": 15, "domain": 16, "ecommerce": 19}

def main():
    a = sys.argv[1:]; slug = a[0]; date = a[a.index("--date") + 1]
    out = a[a.index("--out") + 1] if "--out" in a else f"php-in-{slug}.json"
    md = open(os.path.join(BLOGS, slug, f"{slug}.md"), encoding="utf-8").read()
    title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
    cat_line = re.search(r"^Category:\s*(.+)$", md, re.M).group(1)
    cats = [CATS[c.strip().lower()] for c in re.split(r"[,]", re.sub(r"\(.*?\)", "", cat_line)) if c.strip().lower() in CATS]
    if 1 not in cats: cats.append(1)  # WordPress is the umbrella category on every post
    tags = [t.strip() for t in re.search(r"^Tags:\s*(.+)$", md, re.M).group(1).split(",") if t.strip()]
    php = f"""// Create ONE draft post with a fixed Sunday 09:00 publish date. Nothing is published. Undo: trash post.
$slug = {json.dumps(slug)}; $title = {json.dumps(title)}; $local = {json.dumps(date + ' 09:00:00')};
if ($existing = get_page_by_path($slug, OBJECT, 'post')) return ['skipped' => 'already exists', 'id' => $existing->ID, 'status' => $existing->post_status];
$id = wp_insert_post([
  'post_type' => 'post', 'post_status' => 'draft', 'post_author' => 2,
  'post_title' => $title, 'post_name' => $slug, 'post_content' => '',
  'post_date' => $local, 'post_date_gmt' => get_gmt_from_date($local), 'edit_date' => true,
  'comment_status' => 'closed', 'ping_status' => 'open',
  'post_category' => {json.dumps(cats)}, 'tags_input' => {json.dumps(tags, ensure_ascii=False)},
], true);
if (is_wp_error($id)) return ['error' => $id->get_error_message()];
return ['id' => $id, 'slug' => $slug, 'status' => get_post_status($id), 'date' => get_post_field('post_date', $id), 'edit' => get_edit_post_link($id, '')];
"""
    json.dump({"code": php}, open(out, "w"))
    print(f"-> {out}\n   creates draft '{title}' as /{slug}/, categories {cats}, tags {tags}, date {date} 09:00 (site time)\n   ASK THE USER before running execute-php.")

if __name__ == "__main__":
    main()
