## Section 1 — Plain bullets at top of document (CONTROL, should work)

* Item 1.1 — expected to survive round-trip
* Item 1.2 — expected to survive round-trip
* Item 1.3 — expected to survive round-trip


---

## Section 2 — Bullets inside a blockquote (CONTROL, should work)

> Bullets inside a blockquote:
>
> * Item 2.1 — expected to survive round-trip
> * Item 2.2 — expected to survive round-trip


---

## Section 3 — Checkbox list (CONTROL, should work)

- [ ] Item 3.1 — expected to survive round-trip
- [x] Item 3.2 — expected to survive round-trip


---

:::info
A plain `:::info` admonition (no checkboxes inside).
:::


## Section 4 — Plain H2 + bullets after a simple info admonition

* Item 4.1 — expected behaviour: present
* Item 4.2 — expected behaviour: present
* Item 4.3 — expected behaviour: present


---

| Column A | Column B |
|----------|----------|
| Row 1    | value    |
| Row 2    | value    |


## Section 5 — H2 + bullets immediately after a GFM table

* Item 5.1 — expected behaviour: present
* Item 5.2 — expected behaviour: present


---

## Section 6 — Pattern that failed in the real document

:::warning
A `:::warning` admonition that contains a checkbox list — this is the exact
shape that preceded the failing section in the real document (Pillar 4.2).

- [x] Checkbox 6.x — completed item inside admonition
- [ ] Checkbox 6.y — open item inside admonition
- [x] Checkbox 6.z — completed item inside admonition
:::

**Proposed Approach:**

* Item 6.1 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 6.2 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 6.3 — EXPECTED: present, ACTUAL in real doc: dropped


---

## Section 7 — Section with Outline-specific `==highlight==` runs

This paragraph has ==highlighted text== and a hard line break below this sentence.\
A continuation line after a `\` escape, like the real doc used.

**Some bold paragraph after the highlight + escape:**

* Item 7.1 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 7.2 — EXPECTED: present, ACTUAL in real doc: dropped


---

## Section 8 — Mid-document H2 + bullets directly (no preceding paragraph)

* Item 8.1 — expected behaviour: present
* Item 8.2 — expected behaviour: present


---

## Section 9 — H2 → `**bold-only paragraph**` → bullets

**Next Steps**

* Item 9.1 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 9.2 — EXPECTED: present, ACTUAL in real doc: dropped


---

## Section 10 — H2 → `Label:` paragraph → bullets

Status:

* Item 10.1 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 10.2 — EXPECTED: present, ACTUAL in real doc: dropped


---

## Section 11 — H3 immediately under H2

### Subsection 11a

* Item 11.1 — EXPECTED: present, ACTUAL in real doc: dropped
* Item 11.2 — EXPECTED: present, ACTUAL in real doc: dropped


---

## Section 12 — Trailing paragraph

This trailing paragraph should always be present. It proves the parser does
keep going past any dropped lists rather than truncating the document.
