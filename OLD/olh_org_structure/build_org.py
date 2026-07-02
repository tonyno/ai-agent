#!/usr/bin/env python3
"""Generate the OpenLoop Health org-structure Markdown + interactive HTML.

The org data below is the single source of truth. Edit it, then re-run:
    python3 build_org.py
Outputs (written next to this script):
    olh-org-structure.md    -- human-readable source (roster, hierarchy, mermaid)
    olh-org-structure.html  -- self-contained interactive org chart
Photos for people with a real headshot live in photos/<slug>.jpg.
Everyone else gets a deterministic colored initials avatar.

Source: 13 Google Contacts directory screenshots captured 2026-05-27.
"""
import base64
import html
import json
import re
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent

# ---------------------------------------------------------------------------
# SOURCE OF TRUTH: the org tree.
# Each node: name, title, photo (filename in photos/ or None), children.
# Optional: unconfirmed=True + note  -> draws a flag in both outputs.
# ---------------------------------------------------------------------------

def P(name, title, children=None, photo=None, unconfirmed=False, note=None):
    return {
        "name": name, "title": title, "photo": photo,
        "children": children or [], "unconfirmed": unconfirmed, "note": note,
    }

ORG = [
    P("Christian Williams", "Top of captured org · title not shown in source", photo=None, children=[
        P("Diego Rodriguez", "Director, Technical Program Management & GM Perú",
          photo="diego-rodriguez.jpg", children=[
            P("Daniel Moncada", "Senior Technical Program Manager", photo="daniel-moncada.jpg"),
            P("Ramesh Peesapaty", "Staff Technical Program Manager"),
        ]),
        P("Gabriel Alizaidy", "Director, New Product Formulation and Rollout"),
        P("Jake Rzeszutko", "Director, Supply Chain", children=[
            P("Denea Shelton", "Supply Chain Specialist"),
            P("Luciana Teles", "Manager, Supply Chain"),
            P("Marcial Saldana", "Sr. Supply Chain Specialist"),
        ]),
        P("Kate Hainsworth", "VP, Enterprise Operations"),
        P("Ryan Cantera", "Chief of Staff (COO)"),
        P("Scott Heldt", "VP, Customer Solutions & Implementation",
          photo="scott-heldt.jpg", children=[
            P("Katie Dave", "Director of Programs"),
            P("Mitchell Barish", "Sr. Director, Implementation",
              photo="mitchell-barish.jpg", children=[
                P("Faith Williams", "Implementation Project Manager"),
                P("Nirupa Parmhans", "Implementation Manager II"),
                P("Pamela Suarez", "Sr. Manager, Client Implementations",
                  photo="pamela-suarez.jpg", children=[
                    P("Aastha Patel", "Implementation Manager II"),
                    P("Anisha Shukla", "Manager, Implementation"),
                    P("Joe Millones", "Manager, Implementation"),
                    P("Seevieta Biswas", "Manager, Implementation", children=[
                        P("Johna Davis", "Senior Implementation Manager"),
                        P("Shannon Falter", "Implementation Manager"),
                    ]),
                    P("Surjt Kumar", "Sr. Implementation Manager"),
                ]),
                P("Russell Nicholson", "Senior Manager, Implementation"),
                P("Winter Valent", "Implementation Manager II"),
            ]),
            P("Susan Trinh", "Director, Solutions Engineering"),
        ]),
        P("Shaun Wei", "EVP, Engineering", photo="shaun-wei.jpg", children=[
            P("Aditya Pilla", "Sr. Software Engineer"),
            P("Akintayo Akinyemi", "Software Engineer II"),
            P("Alejandro Roman", "Software Engineer II"),
            P("Ankit Basrur", "Software Engineer II"),
            P("Arman Valaee", "Sr. Software Engineer"),
            P("Bruno Verano", "Sr. Software Engineer"),
            P("Cesar Montenegro", "Staff Software Engineer"),
            P("Daming Wu", "Software Engineer II (Fullstack Evergreen)"),
            P("Eric Zhang", "Staff Software Engineer"),
            P("Gloria Yu", "Principal Product Manager"),
            P("Habibullah Noorzaie", "Sr. Software Engineer"),
            P("Harry Liu", "Director of Engineering, LaunchPad"),
            P("Ian Benedict", "Sr. Software Engineer"),
            P("Igal Babushkin", "Software Engineer II (Fullstack Evergreen)"),
            P("Jeff Williams", "Staff Product Manager – Products & Services"),
            P("Jorge Herrera", "Sr. Software Engineer"),
            P("Juan Calvo", "Sr. Software Engineer"),
            P("Katie Yarbrough", "Sr. Product Manager"),
            P("Kevin Leung", "Senior Engineering Manager"),
            P("Lakshmi Ramamurthy", "Staff Product Manager"),
            P("Mason Gallo", "Senior Staff Software Engineer"),
            P("Muneeb Hussain", "Sr. Software Engineer"),
            P("Pavel Shkleinik", "Staff Software Engineer"),
            P("Ranxin Li", "Software Engineer"),
            P("Saketh Jakka", "Software Engineer"),
            P("Sandeep Bharadwaj", "Staff Technical Lead"),
            P("Sumit Deb", "Senior Engineering Manager"),
            P("Venkata Gade", "Software Engineer"),
            P("Yael Mark", "Senior Product Manager"),
            P("Yuriy Tolstykh", "Senior Software Engineer"),
        ]),
    ]),
    P("Curtis Olson", "Engineering leadership · title not shown in source",
      photo="curtis-olson.jpg", unconfirmed=True,
      note="Reporting line up the chain is not captured in the source screenshots "
           "(his profile shows no manager and he is not among Shaun Wei's reports).",
      children=[
        P("Alex Nima", "Director, Engineering"),
        P("Ben Routson", "Principal Software Engineer"),
        P("Chris Robot", "Staff Software Engineer"),
        P("Clint Johnson", "Principal Software Engineer"),
        P("Jamie Gray", "Sr. Director, Platform Product Management", children=[
            P("Cristina Tepelikian", "Product Manager"),
            P("Jack McKnight", "Sr. Product Manager"),
            P("Jose Diaz", "Product Manager II"),
            P("Justin Batt", "Principal Product Manager – Data Analytics and Governance"),
            P("Matthew Spaulding", "Principal Product Manager"),
        ]),
        P("Kerry Wilson", "Principal Software Engineer"),
        P("Mitchell Cravens", "Manager, Engineering"),
        P("Scott Huff", "Staff Software Engineer"),
    ]),
]

# Collapse this manager's reports into one summary node in the Mermaid diagram
# only (full names still appear in the roster table, hierarchy list and HTML).
MERMAID_COLLAPSE = {"Shaun Wei"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

def initials(name):
    parts = [p for p in re.split(r"\s+", name) if p]
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    return name[:2].upper()

def avatar_hue(name):
    return sum(ord(c) for c in name) * 37 % 360

def walk(nodes):
    for n in nodes:
        yield n
        yield from walk(n["children"])

def count(nodes):
    return sum(1 + count(n["children"]) for n in nodes)

# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def md_hierarchy(nodes, depth=0):
    lines = []
    for n in nodes:
        photo = f" · photo" if n["photo"] else ""
        photo = f"  ![{n['name']}](photos/{n['photo']})" if False else ""  # photos shown in gallery, not inline
        flag = " ⚠️ *(reporting line unconfirmed)*" if n["unconfirmed"] else ""
        lines.append(f"{'  ' * depth}- **{n['name']}** — {n['title']}{flag}")
        lines.extend(md_hierarchy(n["children"], depth + 1))
    return lines

def md_table(nodes):
    rows = []
    def rec(nodes, manager):
        for n in nodes:
            ph = "✓ photo" if n["photo"] else "initials"
            flag = " ⚠️" if n["unconfirmed"] else ""
            rows.append(f"| {n['name']}{flag} | {n['title']} | {manager} | {ph} |")
            rec(n["children"], n["name"])
    rec(nodes, "— (top of captured org)")
    return rows

def md_mermaid(nodes):
    lines = ["flowchart TD"]
    ids = {}
    def nid(name):
        if name not in ids:
            ids[name] = "n%d" % len(ids)
        return ids[name]
    def label(n, extra=""):
        t = n["title"].split(" · ")[0]
        flag = "⚠️ " if n["unconfirmed"] else ""
        return f'{nid(n["name"])}["{flag}<b>{n["name"]}</b><br/>{t}{extra}"]'
    def rec(nodes):
        for n in nodes:
            lines.append(f"    {label(n)}")
            if n["name"] in MERMAID_COLLAPSE and n["children"]:
                gid = nid(n["name"] + "__group")
                lines.append(f'    {gid}["{len(n["children"])} engineers & PMs<br/><i>see roster table</i>"]')
                lines.append(f'    {nid(n["name"])} --> {gid}')
                continue
            for c in n["children"]:
                lines.append(f'    {nid(n["name"])} --> {nid(c["name"])}')
            rec(n["children"])
    rec(nodes)
    # style the unconfirmed nodes
    for n in walk(nodes):
        if n["unconfirmed"]:
            lines.append(f"    style {nid(n['name'])} stroke:#d9534f,stroke-width:2px,stroke-dasharray:4 3")
    return lines

def md_gallery(nodes):
    out = []
    for n in walk(nodes):
        if n["photo"]:
            out.append(f'<img src="photos/{n["photo"]}" alt="{n["name"]}" width="84" '
                       f'title="{n["name"]} — {n["title"]}" '
                       f'style="border-radius:50%;margin:4px"/>')
    return out

def build_md():
    total = count(ORG)
    with_photo = sum(1 for n in walk(ORG) if n["photo"])
    lines = []
    a = lines.append
    a("# OpenLoop Health — Org Structure")
    a("")
    a(f"> **Source:** 13 Google Contacts directory screenshots captured **2026-05-27** "
      f"(`olh_org_structure/`).  ")
    a(f"> **Generated:** {date.today().isoformat()} by `build_org.py` (edit that file and re-run to regenerate).  ")
    a(f"> **Coverage:** {total} people across {with_photo} real headshots; everyone else uses an initials avatar.")
    a("")
    a("## How to use this file")
    a("")
    a("This Markdown is the **source of truth**. Other outputs are generated from the same dataset:")
    a("")
    a("- `olh-org-structure.html` — interactive, collapsible org chart with photos.")
    a("- `photos/` — cropped headshots for the people whose profile page had a real photo.")
    a("- The structured tree lives in `build_org.py` (`ORG`); the sections below mirror it.")
    a("")
    a("## Caveats & data notes")
    a("")
    a("- **Christian Williams** is the top of the *captured* tree; his own title is not shown in the source "
      "(his avatar is the OpenLoop logo, not a headshot).")
    a("- **Curtis Olson** leads an engineering/product group, but **his reporting line up the chain is not "
      "captured** — his profile shows no manager and he is not among Shaun Wei's reports. He is shown as a "
      "separate branch flagged ⚠️.")
    a("- Only profile pages that were screenshotted expose their direct reports; people without their own "
      "screenshot appear as leaves even if they may manage others.")
    a("- Titles and names are transcribed verbatim from the screenshots.")
    a("")
    a("## Org chart (Mermaid)")
    a("")
    a("> Shaun Wei's 30 reports are collapsed into a single node here for readability; "
      "their names are in the roster table and the interactive HTML.")
    a("")
    a("```mermaid")
    lines.extend(md_mermaid(ORG))
    a("```")
    a("")
    a("## Reporting hierarchy")
    a("")
    lines.extend(md_hierarchy(ORG))
    a("")
    a("## Roster")
    a("")
    a("| Name | Title | Reports to | Avatar |")
    a("| --- | --- | --- | --- |")
    lines.extend(md_table(ORG))
    a("")
    a("## Photo gallery")
    a("")
    a("People with a real headshot extracted from the source screenshots:")
    a("")
    a("<p>" + "".join(md_gallery(ORG)) + "</p>")
    a("")
    (HERE / "olh-org-structure.md").write_text("\n".join(lines) + "\n")
    return total, with_photo

# ---------------------------------------------------------------------------
# HTML (interactive, self-contained)
# ---------------------------------------------------------------------------

def photo_data_uri(filename):
    """Read photos/<filename> and return an inline base64 data URI."""
    raw = (HERE / "photos" / filename).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode("ascii")

def to_client(nodes):
    return [
        {"name": n["name"], "title": n["title"],
         "photo": photo_data_uri(n["photo"]) if n["photo"] else None,
         "initials": initials(n["name"]), "hue": avatar_hue(n["name"]),
         "unconfirmed": n["unconfirmed"], "note": n["note"],
         "children": to_client(n["children"])}
        for n in nodes
    ]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>OpenLoop Health — Org Structure</title>
<style>
  :root {
    --ink:#1f2933; --muted:#6b7785; --line:#cfd8e3; --card:#ffffff;
    --bg:#eef2f7; --accent:#e0245e; --flag:#d9534f;
  }
  * { box-sizing:border-box; }
  body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
         color:var(--ink); background:var(--bg); }
  header { padding:20px 28px; background:#fff; border-bottom:1px solid var(--line);
           position:sticky; top:0; z-index:20; }
  header h1 { margin:0 0 4px; font-size:20px; }
  header .meta { color:var(--muted); font-size:13px; }
  .toolbar { margin-top:12px; display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
  .toolbar button { font:inherit; font-size:13px; padding:6px 12px; border:1px solid var(--line);
                    background:#fff; border-radius:7px; cursor:pointer; }
  .toolbar button:hover { background:#f1f5fa; }
  .toolbar input { font:inherit; font-size:13px; padding:6px 10px; border:1px solid var(--line);
                   border-radius:7px; min-width:200px; }
  .legend { font-size:12px; color:var(--muted); display:flex; gap:16px; align-items:center; flex-wrap:wrap; }
  .legend .dash { display:inline-block; width:22px; height:0; border-top:2px dashed var(--flag);
                  vertical-align:middle; margin-right:5px; }
  .scroller { overflow:auto; padding:34px 28px 60px; }
  .tree, .tree ul { list-style:none; margin:0; padding:0; }
  .tree { display:flex; gap:40px; justify-content:center; min-width:max-content; }
  /* nested tree connectors */
  ul.children { display:flex; padding-top:24px; position:relative; }
  ul.children > li { position:relative; padding:24px 14px 0; }
  /* vertical line up from each child to the horizontal bus */
  ul.children > li::before { content:""; position:absolute; top:0; left:50%; height:24px;
                             border-left:1px solid var(--line); }
  /* horizontal bus segments */
  ul.children > li::after { content:""; position:absolute; top:0; left:0; right:0; height:24px;
                            border-top:1px solid var(--line); }
  ul.children > li:first-child::after { left:50%; }
  ul.children > li:last-child::after { right:50%; }
  ul.children > li:only-child::after { display:none; }
  /* line down from a parent into its bus */
  li.node > .branch { position:relative; }
  li.node.has-kids.open > .branch::after { content:""; position:absolute; bottom:0; left:50%;
                                           height:24px; border-left:1px solid var(--line); }
  li.node > .branch { padding-bottom:0; }
  li.node.has-kids.open > .branch { padding-bottom:24px; }
  .card { width:210px; background:var(--card); border:1px solid var(--line); border-radius:12px;
          padding:12px 12px 12px 14px; margin:0 auto; box-shadow:0 1px 2px rgba(16,24,40,.06);
          display:flex; gap:11px; align-items:center; position:relative; cursor:default; }
  .card.kids { cursor:pointer; }
  .card.kids:hover { border-color:#9bb0c9; box-shadow:0 2px 8px rgba(16,24,40,.12); }
  .card.flagged { border:1.5px dashed var(--flag); }
  .avatar { width:46px; height:46px; border-radius:50%; flex:0 0 46px; object-fit:cover;
            display:flex; align-items:center; justify-content:center; color:#fff; font-weight:600;
            font-size:15px; overflow:hidden; }
  .card .name { font-size:13.5px; font-weight:600; line-height:1.2; }
  .card .title { font-size:11.5px; color:var(--muted); line-height:1.25; margin-top:2px; }
  .toggle { position:absolute; bottom:-11px; left:50%; transform:translateX(-50%); width:22px; height:22px;
            border-radius:50%; background:#fff; border:1px solid var(--line); color:var(--muted);
            font-size:12px; line-height:20px; text-align:center; z-index:2; }
  .count { font-size:10px; color:var(--muted); position:absolute; top:6px; right:9px; }
  .flag-badge { font-size:10px; color:var(--flag); position:absolute; top:6px; right:9px; }
  li.node.closed > .branch + ul.children { display:none; }
  .card.dim { opacity:.28; }
  .card.hit { outline:2px solid var(--accent); outline-offset:1px; }
  footer { color:var(--muted); font-size:12px; padding:0 28px 30px; text-align:center; }
</style>
</head>
<body>
<header>
  <h1>OpenLoop Health — Org Structure</h1>
  <div class="meta">__META__</div>
  <div class="toolbar">
    <button id="expandAll">Expand all</button>
    <button id="collapseAll">Collapse to leaders</button>
    <input id="search" type="search" placeholder="Search name or title…" autocomplete="off"/>
    <span class="legend"><span class="dash"></span>reporting line unconfirmed &nbsp;·&nbsp; click a card with a number to expand/collapse</span>
  </div>
</header>
<div class="scroller"><ul class="tree" id="tree"></ul></div>
<footer>Source: Google Contacts directory screenshots, captured 2026-05-27. Generated by build_org.py.</footer>
<script>
const DATA = __DATA__;

function avatar(p){
  if(p.photo){
    const img=document.createElement('img');
    img.className='avatar'; img.src=p.photo; img.alt=p.name;
    return img;
  }
  const d=document.createElement('div');
  d.className='avatar'; d.textContent=p.initials;
  d.style.background='hsl('+p.hue+',55%,45%)';
  return d;
}

function makeNode(p, depth){
  const li=document.createElement('li');
  // default view: roots expanded one level (show leaders), deeper levels collapsed
  const startOpen = depth < 1;
  li.className='node'+(p.children.length?(' has-kids '+(startOpen?'open':'closed')):'');
  const branch=document.createElement('div'); branch.className='branch';
  const card=document.createElement('div');
  card.className='card'+(p.children.length?' kids':'')+(p.unconfirmed?' flagged':'');
  card.appendChild(avatar(p));
  const info=document.createElement('div');
  const nm=document.createElement('div'); nm.className='name'; nm.textContent=p.name;
  const tt=document.createElement('div'); tt.className='title'; tt.textContent=p.title;
  info.appendChild(nm); info.appendChild(tt); card.appendChild(info);
  if(p.unconfirmed){
    const b=document.createElement('div'); b.className='flag-badge'; b.textContent='⚠';
    b.title=p.note||'reporting line unconfirmed'; card.appendChild(b);
  } else if(p.children.length){
    const c=document.createElement('div'); c.className='count'; c.textContent=p.children.length;
    card.appendChild(c);
  }
  branch.appendChild(card);
  if(p.children.length){
    const tog=document.createElement('div'); tog.className='toggle'; tog.textContent=startOpen?'−':'+';
    card.appendChild(tog);
    const toggle=(e)=>{e.stopPropagation();
      const open=li.classList.toggle('open'); li.classList.toggle('closed',!open);
      tog.textContent=open?'−':'+';};
    card.addEventListener('click',toggle);
    li.appendChild(branch);
    const ul=document.createElement('ul'); ul.className='children';
    p.children.forEach(c=>ul.appendChild(makeNode(c, depth+1)));
    li.appendChild(ul);
  } else {
    li.appendChild(branch);
  }
  return li;
}

const tree=document.getElementById('tree');
DATA.forEach(r=>tree.appendChild(makeNode(r, 0)));

function setOpen(open){
  document.querySelectorAll('li.node.has-kids').forEach(li=>{
    li.classList.toggle('open',open); li.classList.toggle('closed',!open);
    const t=li.querySelector(':scope > .branch .toggle'); if(t)t.textContent=open?'−':'+';
  });
}
document.getElementById('expandAll').onclick=()=>setOpen(true);
document.getElementById('collapseAll').onclick=()=>{
  // collapse everything, then open only the two roots
  setOpen(false);
  tree.querySelectorAll(':scope > li.node.has-kids').forEach(li=>{
    li.classList.add('open'); li.classList.remove('closed');
    const t=li.querySelector(':scope > .branch .toggle'); if(t)t.textContent='−';
  });
};

const search=document.getElementById('search');
search.addEventListener('input',()=>{
  const q=search.value.trim().toLowerCase();
  const cards=document.querySelectorAll('.card');
  if(!q){cards.forEach(c=>c.classList.remove('dim','hit')); return;}
  setOpen(true);
  cards.forEach(c=>{
    const txt=c.querySelector('.name').textContent.toLowerCase()+' '+c.querySelector('.title').textContent.toLowerCase();
    const hit=txt.includes(q);
    c.classList.toggle('hit',hit); c.classList.toggle('dim',!hit);
  });
});
</script>
</body>
</html>
"""

def build_html(total, with_photo):
    data = json.dumps(to_client(ORG), ensure_ascii=False)
    meta = (f"{total} people · {with_photo} headshots · source captured 2026-05-27 "
            f"· ⚠ = reporting line unconfirmed")
    out = (HTML_TEMPLATE
           .replace("__DATA__", data)
           .replace("__META__", html.escape(meta)))
    (HERE / "olh-org-structure.html").write_text(out)

if __name__ == "__main__":
    total, with_photo = build_md()
    build_html(total, with_photo)
    print(f"Generated olh-org-structure.md and olh-org-structure.html "
          f"({total} people, {with_photo} headshots).")
