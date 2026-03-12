# Index of Social Actor

> In this project we attempt to represent the abstract space of social actors at the planetary scale.
The objective is to identify the most relevant actors across multiple categories—including individuals, firms, states, NGOs, and other organized entities.
> By constructing this index, we aim to establish comparative metrics and analytical frameworks that allow systematic analysis of actors, their capacities, and their roles within global socio-economic systems.

## Formulation

- The system must provide a central entry point to the Social Actor Index, linking to both the Actor Type Index and the Individual Actor Index.
- The entry point should function as a navigation hub and guide for the entire site.
- It must include a global footer used consistently across the site.

## 1. Architectural Intent

## 1.1 Functional Role

The landing page functions as:

> A curated institutional registry gateway with inquiry-driven entry.

It is not:

* A dashboard
* A data lab
* A comparison engine
* A high-density analytics surface

It is:

* A structured portal
* A registry overview
* An institutional identity surface

## 2. Core Design Principles

* Elegance over novelty
* Motion as refinement, not spectacle
* Hierarchy over density
* Inquiry before browsing
* Institutional tone above commercial tone
* Accessibility as structural constraint (WCAG 2.2 AA minimum)
* Usability grounded in ISO 9241 dialogue principles
* Cognitive load minimization (Hick, Fitts, progressive disclosure)
* Grid and typographic proportional discipline
* Design system governance and tokenization
* Performance as aesthetic condition
* Privacy and trust as first-class design properties

## 3. Page Structural Architecture

The landing page consists of six structured layers:

```
[2] Institutional Hero Layer
[3] Inquiry Layer (Search + CTA)
[4] Classification Filter Layer
[5] Entity Registry Grid
[6] Institutional Footer
```

# 4. Layer Specifications


## 4.1 Institutional Hero Layer

### Components

* Crest emblem (logo.png)
* Roman founding mark (EST. MMXXIV)
* Primary title: INDEX GENTIUM
* Institutional sub-label: Laboratorium Arbitristae
* Mission subtitle

### Hierarchy

1. Emblem (symbolic authority)
2. Title (identity)
3. Institutional attribution
4. Descriptive framing

### Visual Rules

* Center aligned
* Generous vertical whitespace
* Serif typography for title
* Muted neutral palette
* Subtle letter-spacing on title

---

## 4.2.1 Entrance Motion (Subtle)

Sequential fade-in:

| Element  | Delay | Duration |
| -------- | ----- | -------- |
| Crest    | 0ms   | 250ms    |
| Title    | 80ms  | 250ms    |
| Subtitle | 150ms | 250ms    |
| Search   | 250ms | 250ms    |

Easing: ease-out
No scaling.
No bounce.

Total reveal under 700ms.

---

# 5. Inquiry Layer (Search as Primary Action)

## 5.1 Conceptual Shift

Search is not a filter tool — it is:

> The primary intellectual entry point.

---

## 5.2 Structural Components

1. Label (above input)
2. Search input
3. Explore CTA button
4. Optional live suggestion panel

---

## 5.3 Label

Text:

```
INQUIRE THE REGISTRY
```

Style:

* Small caps
* Slight letter spacing
* Subtle gray tone
* Positioned above input field

Purpose:
Signals intellectual action.

---

## 5.4 Search Input Field

### Placeholder

```
Search sovereign entities, regions, or classifications…
```

### Search Tags

* Make tags feel refined and taxonomic — not like primary CTA buttons.
* ...


Tags represent:

- Filters
- Classifications
- Facets of the registry


**Position**

* Place the tag row immediately below the search field.
* Maintain balanced vertical spacing so it reads as part of the search module, not as a detached element.
* Align the tag row horizontally with the exact width of the search field.
* It must be after the drop down.

---

**Structure**

* Include one static pseudo-tag: **“All Nations”** (default selected state).
* All remaining tags must be dynamically generated from `catalog.json`.
* The system must gracefully support variable tag counts.

---

**Width & Layout Constraints**

* The total horizontal span of the tag container must never exceed the width of the search field.
* Tags must remain visually contained within that boundary.
* If overflow occurs, apply controlled horizontal scrolling or internal truncation.
* Wrapping beyond the search width is not permitted.

---

**Typography & Aesthetic Coherence**

* Typography must match the site’s established font family, weight hierarchy, and letter spacing.
* Color palette must follow the site’s restrained tonal system.
* Tags must preserve the overall institutional, archival character of the interface.
* Avoid visual treatments that introduce stylistic inconsistency or promotional tone.



## 5.4.0 Search Results Specs

Correct structural, stacking, and interaction defects in the search dropdown so that:

0. The dropdown shall render without overlapping any existing UI component. Its positioning logic must ensure spatial separation from adjacent elements, preserving layout integrity and visual hierarchy at all viewport sizes.
1. The dropdown never overlaps filter controls incorrectly.
2. The visual hierarchy is preserved.
3. The component is accessible and predictable.
4. The aesthetic remains restrained and classical.
5. The dropdown shall contain a metadata summary section presenting aggregate counts (e.g., total entities, classification counts).
6. The dropdown shall display a maximum of five result items simultaneously. When additional results are available, the interface shall provide vertical navigation controls (scroll or directional navigation) to access the remaining entries.

Architectural Constraints:

* The search module must be a self-contained component.
* No global z-index values above 20 are permitted.
* No element outside the component may affect its stacking context.
* The dropdown must be visually and structurally separate from filter controls.

Interaction Model:  Dropdown Visibility Rules - The dropdown must open when:

* Input receives focus
* User types into input
* The dropdown must close when:
* User presses Escape
* User clicks outside the component
* A result is selected
* The dropdown must remain open when:
* Clicking within the dropdown
* Interacting with filter chips

Keyboard Navigation  Required behavior:

* ArrowDown → moves highlight down
* ArrowUp → moves highlight up
* Enter → selects highlighted item
* Escape → closes dropdown
* Tab → closes dropdown and continues focus flow
* One result at a time must have active state.

## 5.4.1 Interaction States

### Default

* Light neutral border
* Soft shadow (very faint)
* 6–8px border radius
* Subtle underline accent (1px muted blue)

### Hover

* Border darkens slightly
* Shadow deepens by 8%
* Transition: 150ms

### Focus

* Accent border color activates
* Underline deepens
* Soft halo (very faint)
* No glow explosion
* Transition: 150–200ms

### Active Typing

* Suggestion dropdown appears
* Minimalist styling
* Light border
* White background
* Soft shadow
* Entity name bolded
* Category in lighter gray beneath

No aggressive dropdown animations.

---

## 5.5 Explore CTA

Placed adjacent to search.

Text:

```
Explore →
```

### Default

* Outline button
* Transparent background
* Serif or refined sans (consistent)

### Hover

* Light fill (very soft)
* Arrow shifts 3px right
* Duration: 150ms

No scaling.
No pulse.

---

# 6. Classification Filter Layer

### Components

* “All Nations”
* (Future categories possible)

---

## 6.1 Interaction

### Default

* Outlined pill
* Neutral background

### Active

* Slight fill color
* Slightly thicker border
* Smooth transition 120ms

No color explosion.
No heavy animation.

---

# 7. Entity Registry Grid

## 7.1 Layout

* Responsive grid
* 3-column desktop
* 2-column tablet
* 1-column mobile
* Uniform card height
* Generous spacing

---

## 7.2 Card Specification

Each `EntityCard` contains:

| Element           | Function        |
| ----------------- | --------------- |
| Flag icon         | Recognition     |
| Sector tag        | Classification  |
| Entity name       | Primary anchor  |
| Short description | Context         |
| Status indicator  | Active signal   |
| Internal code     | Registry marker |
| View CTA          | Navigation      |



Catalog Spec:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://bremontix.xyz/schema/countries.schema.json",
  "title": "Countries Collection Schema",
  "type": "object",
  "required": ["countries"],
  "additionalProperties": false,
  "properties": {
    "countries": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "name", "tags", "icon", "description", "link"],
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "integer",
            "minimum": 1,
            "description": "Unique numeric identifier for the country entry."
          },
          "name": {
            "type": "string",
            "minLength": 1,
            "description": "Country name."
          },
          "tags": {
            "type": "array",
            "minItems": 1,
            "uniqueItems": true,
            "items": {
              "type": "string",
              "minLength": 1
            },
            "description": "List of classification or grouping tags."
          },
          "icon": {
            "type": "string",
            "minLength": 1,
            "description": "Emoji or symbolic representation."
          },
          "description": {
            "type": "string",
            "minLength": 1,
            "description": "Short descriptive summary."
          },
          "link": {
            "type": "string",
            "format": "uri",
            "description": "URL pointing to detailed country page."
          }
        }
      }
    }
  }
}

```


Data Source: catalog.json  (Load the data from this catalog).
- You can simulate the data;  but must be in catalog.json - not hardcoded.

## 7.3 Card Hover Refinement

### Goals:

Add tactility without disrupting elegance.

---

### On Hover

1. Elevation Shift

   * translateY(-3px)
   * Shadow deepens slightly
   * Duration: 150ms

2. Left Accent Bar

   * 2px vertical line
   * Muted institutional blue
   * Fades in
   * Duration: 150ms

3. Title Emphasis

   * Slightly darker tone
   * No scaling

4. View CTA Interaction

   * Arrow shifts 3px
   * Subtle color darken
   * No size change

---

### Prohibited Effects

* No dramatic hover lift
* No glowing borders
* No animated gradients
* No flip animation
* No parallax

---

# 8. Search Result State

When search active:

Small label above grid:

```
6 entities found
```

Style:

* Small
* Neutral gray
* Light weight

If zero results:

```
No matching entities found.
```

Centered and restrained.

---

# 9. Pagination Layer

Components:

* Prev
* Page Indicator (Center)
    * One blue elongated dot (active state).
    * small gray dot (inactive states).
* Next

### Interaction

* Hover darkens slightly
* Arrow shift subtle
* No jump animation

---

Below is your updated specification.
The structure is preserved exactly. Content density and institutional weight have been increased in a controlled, non-decorative manner.

---

# 10. Footer Institutional Layer

Here is a corrected and expanded version, written as a precise design specification.

---

## 10. Footer — Institutional Layer

## Purpose

The Footer constitutes the **institutional layer** of the landing page.
It provides structural legitimacy, navigational closure, methodological signaling, and registry authority reinforcement.

It must communicate stability, archival seriousness, and epistemic discipline.

The footer is not decorative. It functions as the terminal institutional signature of the page.

---

#### Components

1. **ARBITRISTAE Wordmark**

   * Typographic logotype (no iconography)
   * Small caps or refined serif variant
   * Positioned at the top of the footer block
   * Highest visual weight within the footer

2. **Institutional Descriptor (New)**

   Short institutional statement (max 2–3 lines):

   > A research laboratory dedicated to the structured classification and comparative analysis of sovereign systems and institutional regimes.

   * Smaller than the wordmark
   * Larger than metadata text
   * Line length controlled (avoid wide paragraphs)

3. **Navigation Links**

   * About
   * Methodology
   * Research Notes
   * Contact

   Links should be horizontally arranged on desktop and vertically stacked on mobile.

4. **Registry Metadata (New)**

   Compact, structured registry indicators:

   * Entities Indexed: [dynamic count]
   * Classifications: [dynamic count]
   * Regions Represented: [dynamic count]
   * Last Revision: [ISO date]
   * Version: v1.0

   Metadata must be rendered in reduced typographic scale and lighter visual weight.

5. **Motto Line (Optional but Recommended)**

   Single-line structural motto centered at bottom:

   > Ordo ex comparatione.

   or

   > Scientia per distinctionem.

   No translation. No ornament.

---

#### Layout

* Full-width container
* Center-aligned primary structure
* Generous vertical padding (min 72–96px desktop, 56px mobile)
* Clear visual separation from the body via spacing (not borders unless extremely subtle)

Grid recommendation:

* Three-column layout (desktop):

  * Column I: Wordmark + Descriptor
  * Column II: Navigation
  * Column III: Registry Metadata
* Single stacked column (mobile)
* Max content width aligned with main page grid

Spacing must preserve visual air while increasing informational density by approximately 40% relative to the previous version.

---

#### Visual Style

* **Background:** Deep navy (near-black blue; e.g., #0B1A2B range)
* **Typography:** Light serif typeface consistent with landing hierarchy
* **Text Color:** Soft off-white (not pure white; reduce glare)
* **Hierarchy Control:**

  * Wordmark — highest weight
  * Section headers — medium weight
  * Descriptor — regular
  * Metadata — subtle
  * Motto — lowest emphasis
* **Link Styling:**

  * No underline by default
  * Underline on hover
  * Slight luminance shift on hover (subtle, restrained)

Tone:
Formal, archival, institutional — never promotional.

---

#### Interaction

* No animation.
* No transitions beyond minimal hover state change.
* No motion effects.
* Registry metadata may be dynamically populated but must not animate.
* No counters or numeric transitions.

---

### Positioning Behavior

* Always positioned at the bottom of the document flow.
* If page content is short, footer must anchor to the bottom of the viewport.
* Must not overlap content.
* Must not float.
* Must not collapse.
* The footer participates in normal document flow and may shift vertically as page content expands.
* It must always remain positioned at the bottom of the document structure.
* Its position is strictly relative to the document layout (not fixed or absolute).
* As the page height increases, the footer moves downward accordingly.
* The footer must never appear above the final content block.
* When content height is less than the viewport height, the footer must visually anchor to the bottom of the viewport.
* Under no circumstance should the footer float, overlap content, or detach from the document flow.

Implementation note:
Use flex column layout on the root container (`min-height: 100vh; display: flex; flex-direction: column;`) with footer `margin-top: auto;`.





# 11. Motion Governance System

All motion must obey:

| Parameter           | Limit     |
| ------------------- | --------- |
| Duration            | 120–300ms |
| Easing              | ease-out  |
| Max translateY      | 4px       |
| Scaling             | Avoid     |
| Opacity transitions | Allowed   |
| Color shifts        | Subtle    |

Motion must feel:

* Measured
* Architectural
* Deliberate
* Institutional

---

# 12. Typography System

### Headers

* Serif
* Moderate tracking
* Large hierarchy

### Body

* Refined sans-serif
* High legibility
* Medium weight

### Labels

* Small caps
* Letter-spaced

---

# 13. Color Philosophy

Palette:

* Off-white background
* Muted navy
* Soft gray hierarchy
* Institutional blue accent

No saturated gradients.
No harsh contrast.

---

# 14. Responsive Behavior

### Mobile Adjustments

* Search full width
* CTA stacked below
* Cards full width
* Reduced hover behaviors (mobile fallback)


## Detail Spec

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system:
- Identify the tech stack (e.g. React, Next.js, Vue, Tailwind, shadcn/ui, etc.).
- Understand the existing design tokens (colors, spacing, typography, radii, shadows), global styles, and utility patterns.
- Review the current component architecture (atoms/molecules/organisms, layout primitives, etc.) and naming conventions.
- Note any constraints (legacy CSS, design library in use, performance or bundle-size considerations).

Ask the user focused questions to understand the user's goals. Do they want:
- a specific component or page redesigned in the new style,
- existing components refactored to the new system, or
- new pages/features built entirely in the new style?

Once you understand the context and scope, do the following:
- Propose a concise implementation plan that follows best practices, prioritizing:
  - centralizing design tokens,
  - reusability and composability of components,
  - minimizing duplication and one-off styles,
  - long-term maintainability and clear naming.
- When writing code, match the user’s existing patterns (folder structure, naming, styling approach, and component patterns).
- Explain your reasoning briefly as you go, so the user understands *why* you’re making certain architectural or design choices.

Always aim to:
- Preserve or improve accessibility.
- Maintain visual consistency with the provided design system.
- Leave the codebase in a cleaner, more coherent state than you found it.
- Ensure layouts are responsive and usable across devices.
- Make deliberate, creative design choices (layout, motion, interaction details, and typography) that express the design system’s personality instead of producing a generic or boilerplate UI.

</role>

<design-system>
# Design Style: Minimalist Modern

## Design Philosophy

### Core Principle

**Clarity through structure, character through bold detail.** This design system embraces modern web layouts and dynamic interactions while honoring minimalist foundations. It operates on a fundamental tension: restraint in quantity, confidence in execution. Every element that appears has earned its place—but those elements are executed with deliberate flair and precision.

Whitespace is not empty space; it's a precision instrument for directing attention. Motion is not decoration; it's communication. Color is not scattered; it's concentrated into a single, electrifying accent that commands the eye wherever it appears.

### The Visual Vibe

**Professional yet design-forward. Confident and artistic. Refined but alive.**

Imagine an institutional registry landing page with classical restraint. This design feels like it was crafted by someone who understands both engineering rigor and artistic expression—someone who knows the rules well enough to break them intentionally.

**Emotional Keywords:**
- *Confident* — Never apologetic. Elements are sized boldly, colors are vibrant, animations are purposeful.
- *Sophisticated* — The dual-font typography system, the considered color ratios, the layered shadows all whisper "we sweat the details."
- *Alive* — Subtle animations, pulsing indicators, floating elements, and hover responses create a sense that the interface is breathing.
- *Premium* — Generous whitespace, elevated surfaces, and accent-tinted shadows evoke quality and care.
- *Contemporary* — Gradient text, glassmorphic hints, and asymmetric layouts feel undeniably modern without being trendy.

**What This Design Is NOT:**
- Not sterile or clinical (despite being "minimal")
- Not generic or template-like (bold choices prevent this)
- Not busy or overwhelming (restraint in element count)
- Not flat or lifeless (texture, shadow, and motion add depth)
- Not cold or corporate (the warm serif headlines and vibrant blue inject personality)

### The DNA of This Style

#### 1. The Signature Gradient

The Electric Blue gradient (`#0052FF` → `#4D7CFF`) is the heartbeat of this design system. It's not just an accent color—it's a visual signature that creates instant recognition.

**Where it appears:**
- Primary button backgrounds
- Text highlights on key headline words
- Icon container backgrounds
- Featured card border strokes
- Testimonial accent bars
- Trend indicator badges
- CTA section buttons
- Pricing tier highlights

**Why it works:** A gradient feels more alive than a flat color. The subtle shift from deep Electric Blue to a lighter sky blue creates dimensionality and draws the eye along the element. It signals "this is important" without screaming.

#### 2. Inverted Contrast Sections

Strategic sections flip the color scheme—using the deep slate `foreground` color as a background with light text. This technique:
- Creates dramatic visual rhythm as users scroll
- Prevents the light theme from feeling monotonous
- Provides natural section breaks without heavy dividers
- Makes statistics and key metrics feel more impactful
- Adds sophistication through intentional contrast

**Best used for:** Stats sections, final CTAs, or any content that deserves spotlight emphasis.

#### 3. Animated Depth & Living Elements

This design breathes. Micro-animations and transitions create a sense that the interface is responsive and alive:

- **Pulsing indicators:** Small dots in badges that gently pulse, signaling "live" or "new"
- **Floating elements:** Cards in the hero that bob gently on a slow sine wave
- **Rotating decorative rings:** Dashed circles that rotate infinitely at glacial speed (60+ seconds per rotation)
- **Hover responses:** Elements lift, shadows deepen, icons scale, colors shift
- **Entrance animations:** Content fades up into view as users scroll, with staggered timing

**The philosophy:** Motion should feel natural, almost subconscious. Users shouldn't think "oh, that's animated"—they should simply feel that the interface is polished and responsive.

#### 4. Sophisticated Dual-Font Typography

The pairing of **Calistoga** (display) with **Inter** (UI/body) creates a memorable typographic identity:

- **Calistoga** is warm, characterful, and slightly playful. Its soft serifs and sturdy construction make headlines feel approachable yet substantial. It's the "personality" voice.
- **Inter** is clean, highly legible, and professional. It handles the workhorse duties of body text, labels, and UI elements. It's the "clarity" voice.

This pairing creates a conversation between personality and precision—headlines grab attention with character, then body text delivers information with crystal clarity.

**Monospace accents** (JetBrains Mono) appear in section labels and badges, adding a technical, modern touch that reinforces the "high-tech meets high-design" vibe.

#### 5. Texture Over Flatness

Minimalism often fails because it becomes sterile. This design combats flatness through layered texture:

- **Dot patterns:** Subtle `radial-gradient` dot grids at 2-3% opacity on dark sections
- **Radial glows:** Large, blurred circles of accent color positioned at section corners, creating ambient warmth
- **Layered shadows:** Cards don't just have one shadow—they have subtle, diffuse shadows that create realistic depth
- **Gradient overlays:** Hero sections use radial gradients of the accent color at low opacity for atmospheric depth

These textures are felt more than seen. Users won't consciously notice the dot pattern, but they'll feel that the dark section has "something" that makes it feel richer than a flat color.

#### 6. Asymmetry & Visual Tension

Strict grid alignment is intentionally broken in key moments:

- **Hero layout:** The asymmetric `1.1fr / 0.9fr` grid creates visual tension—the text column is subtly dominant
- **Testimonial offset:** The center card is shifted vertically, breaking the rigid grid rhythm
- **Pricing elevation:** The highlighted tier floats above its siblings
- **Benefits visual:** Asymmetric border radii (`rounded-tl-[4rem] rounded-br-[4rem]`) create organic, memorable shapes

**Why this matters:** Perfect symmetry is predictable. Strategic asymmetry creates visual interest and guides the eye in unexpected ways. It's the difference between "correct" and "designed."

#### 7. The Section Label System

Every major section begins with a consistent badge pattern:
- Rounded pill shape with subtle accent border and tinted background
- Small colored dot (optionally animated/pulsing)
- Uppercase monospace text with wide letter-spacing
- Positioned above the section headline

This creates a visual rhythm and helps users orient themselves. It also adds a touch of UI sophistication—these feel like carefully designed interface elements, not just text.

### Differentiation: Minimalism With a Pulse

This style refuses to be "just clean." Many minimal designs strip away so much that they become forgettable—white backgrounds, gray text, safe choices. This design takes the opposite approach:

**Minimalism through bold choices, not absence.**

- Where others use subtle gray, we use Electric Blue
- Where others use flat backgrounds, we use inverted sections and gradient glows
- Where others use static layouts, we use floating animations and pulsing indicators
- Where others use one safe font, we use a memorable dual-font pairing
- Where others center everything, we embrace asymmetry

The result is a design that is unmistakably minimal in its restraint (few colors, generous whitespace, clean lines) but unmistakably bold in its execution (vibrant accent, animated hero, gradient flourishes).

**It's minimalism that makes a statement.**

### Sensory Description

If this design were a physical space, it would be:
- A bright, airy gallery with white walls and polished concrete floors
- One wall painted in deep midnight blue, dramatically lit
- A single piece of art in electric blue, drawing every eye
- Soft ambient lighting that makes surfaces glow
- The faint hum of something technological and precise
- Clean lines everywhere, but one sculptural element with an unexpected curve

If it were music, it would be:
- Electronic, but warm—not cold synthwave
- Mostly minimal beats with generous silence
- One recurring melodic hook in a bright, clear tone
- Occasional swells that feel like things floating upward
- Professional enough for a corporate lobby, interesting enough to actually listen to

---

## Design Token System (The DNA)

### Color Strategy

**Chromatic Focus:** A warm, near-monochrome palette amplified by a dual-tone accent gradient. The accent colors are used sparingly but with maximum impact—they command attention wherever they appear.

| Token | Value | Usage & Context |
|:------|:------|:----------------|
| `background` | `#FAFAFA` | Primary canvas. Warmer off-white that reduces eye strain. |
| `foreground` | `#0F172A` (Slate-900) | Primary text. Deep slate, not pure black. Also used as inverted section backgrounds. |
| `muted` | `#F1F5F9` (Slate-100) | Secondary surfaces, card backgrounds, subtle fills. |
| `muted-foreground` | `#64748B` (Slate-500) | Secondary text, descriptions, metadata. |
| `accent` | `#0052FF` (Electric Blue) | **Primary action color.** CTAs, links, highlights, icon backgrounds. |
| `accent-secondary` | `#4D7CFF` | Gradient endpoint. Used with `accent` for gradient effects. |
| `accent-foreground` | `#FFFFFF` | Text on accent backgrounds. Always white. |
| `border` | `#E2E8F0` (Slate-200) | Subtle structural borders on cards and dividers. |
| `card` | `#FFFFFF` | Elevated surfaces. Pure white for maximum lift. |
| `ring` | `#0052FF` | Focus rings. Matches the primary accent. |

**The Signature Gradient:**
```css
background: linear-gradient(to right, #0052FF, #4D7CFF);
/* Or diagonal: */
background: linear-gradient(135deg, #0052FF, #4D7CFF);
```
This gradient appears on: primary buttons, featured badges, icon backgrounds, pricing tier borders, testimonial accent bars, trend indicators, and text highlights.

---

### Typography System

**Font Pairing (Dual-Font System):**
- **Display Font:** `"Calistoga", Georgia, serif` — A warm, characterful serif with personality. Used exclusively for h1/h2 headlines to create memorable anchor points.
- **UI & Body Font:** `"Inter", system-ui, sans-serif` — Highly legible, clean sans-serif for all body text, UI elements, and smaller headings.
- **Monospace:** `"JetBrains Mono", monospace` — For section labels, badges, and technical callouts.

**Type Scale & Usage:**

| Element | Size | Font | Weight | Tracking | Notes |
|:--------|:-----|:-----|:-------|:---------|:------|
| Hero Headline | `5xl` → `5.25rem` | Calistoga | Normal | `-0.02em` | Tight leading (1.05). Last word gets gradient text treatment. |
| Section Headlines | `3xl` → `3.25rem` | Calistoga | Normal | Normal | Leading 1.15. Key word can use gradient text. |
| Card Titles | `lg` → `2xl` | Inter | Semibold (600) | `-0.01em` | Tight tracking for density. |
| Body Text | `base` → `lg` | Inter | Normal (400) | Normal | Relaxed line-height (1.625-1.75). |
| Section Labels | `xs` (12px) | JetBrains Mono | Normal | `0.15em` | UPPERCASE. Used in pill badges with accent dot. |

**Gradient Text Effect (with Enhanced Underline):**
```css
.gradient-text {
  background: linear-gradient(to right, #0052FF, #4D7CFF);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

/* Gradient underline bar for hero headline */
.gradient-underline {
  position: absolute;
  bottom: -0.25rem; /* md: -0.5rem */
  left: 0;
  height: 0.75rem; /* md: 1rem */
  width: 100%;
  border-radius: 0.125rem;
  background: linear-gradient(to right, rgba(0, 82, 255, 0.15), rgba(77, 124, 255, 0.1));
}
```

---

### Spacing & Layout

**Core Principle:** Generous, intentional whitespace is a primary design tool—but it's balanced by density within components.

- **Section Spacing:** Large vertical padding (`py-28` to `py-44`) creates a calm, paced scrolling experience.
- **Container Width:** `max-w-6xl` (72rem) for primary content. Centered with `mx-auto`.
- **Component Density:** Within cards and components, spacing is tighter to create cohesive units that float in the generous section whitespace.
- **Grid Gaps:** `gap-5` to `gap-8` between grid items. Slightly tighter than standard to maintain visual cohesion.

**Asymmetry Patterns:**
- Hero: `grid-cols-[1.1fr_0.9fr]` — Left-heavy for text dominance
- Benefits: `grid-cols-[1.2fr_0.8fr]` — Content over visual
- Use negative margins and overlapping elements to create Z-depth

---

### Borders, Surfaces & Shadows

**Surfaces:**
- Cards use pure white (`#FFFFFF`) with `1px` border in `border` color
- Elevated cards add `shadow-lg` or `shadow-xl` for lift
- Featured elements use gradient borders (2px stroke effect via nested divs)

**Shadow System:**
| Token | Value | Usage |
|:------|:------|:------|
| `shadow-sm` | `0 1px 3px rgba(0,0,0,0.06)` | Subtle lift |
| `shadow-md` | `0 4px 6px rgba(0,0,0,0.07)` | Standard cards |
| `shadow-lg` | `0 10px 15px rgba(0,0,0,0.08)` | Elevated cards |
| `shadow-xl` | `0 20px 25px rgba(0,0,0,0.1)` | Hero elements |
| `shadow-accent` | `0 4px 14px rgba(0,82,255,0.25)` | Accent-tinted lift |
| `shadow-accent-lg` | `0 8px 24px rgba(0,82,255,0.35)` | Featured elements |

**Textures (Critical for Avoiding Flatness):**
- **Dot Pattern:** `radial-gradient(circle, white 1px, transparent 1px)` at `32px` intervals, `opacity: 0.03` — Used on dark inverted sections
- **Radial Glows:** Large blurred circles (`blur-[150px]`) of accent color at `3-6%` opacity — Positioned at section corners
- **Gradient Overlays:** Subtle `radial-gradient` from accent color, `8%` opacity — Used in hero graphic backgrounds

---

## Component Styling & Interactions

### Buttons

**Primary Button:**
- Background: Gradient from `accent` to `accent-secondary` (`bg-gradient-to-r from-[var(--accent)] to-[#4D7CFF]`)
- Text: White, medium weight
- Shadow: `shadow-sm` default, `shadow-accent` on hover (accent-tinted)
- Border-radius: `rounded-xl` (12px)
- Hover: Lifts up (`-translate-y-0.5`), `shadow-accent-lg`, brightness increase (`brightness-110`), arrow icon translates right
- Active: Slight scale down (`scale-[0.98]`) for tactile feedback

**Secondary/Outline Button:**
- Background: Transparent → `muted` on hover
- Border: `1px` in `border` color
- Text: `foreground`
- Hover: Border shifts to `accent/30`, shadow appears

**Ghost Button:**
- No background or border
- Text: `muted-foreground` → `foreground` on hover

**Animation:** All buttons have `transition-all duration-200`. Subtle upward translation on hover (`-translate-y-0.5`). Arrow icons translate right on hover (`group-hover:translate-x-1`).

---

### Cards

**Standard Card:**
- Background: `card` (white)
- Border: `1px` in `border` color
- Border-radius: `rounded-xl` (12px) or `rounded-2xl` (16px)
- Shadow: `shadow-md` default, `shadow-xl` on hover
- Padding: `p-6` to `p-10` depending on prominence

**Elevated Card:**
- Adds stronger shadow and optional accent tint
- Used for featured items, highlighted pricing tiers

**Hover Effects:**
- Gradient overlay fades in: `bg-gradient-to-br from-accent/[0.03] to-transparent`
- Shadow deepens
- Optional icon scale: `group-hover:scale-110`

**Featured Card (Gradient Border):**
```jsx
<div className="rounded-xl bg-gradient-to-br from-accent via-accent-secondary to-accent p-[2px]">
  <div className="h-full w-full rounded-[calc(12px-2px)] bg-card">
    {/* content */}
  </div>
</div>
```

---

### Inputs

- Height: `h-12` to `h-14`
- Border: `1px` in `border` color
- Border-radius: `rounded-lg` or `rounded-xl`
- Background: Transparent or very subtle `muted/10`
- Focus: `ring-2 ring-accent ring-offset-2`
- Placeholder: `text-muted-foreground/50`

---

### Section Labels (Badges)

A consistent badge pattern appears at the start of each section:
```jsx
<div className="inline-flex items-center gap-3 rounded-full border border-accent/30 bg-accent/5 px-5 py-2">
  <span className="h-2 w-2 rounded-full bg-accent" /> {/* Can be animated/pulsing */}
  <span className="font-mono text-xs uppercase tracking-[0.15em] text-accent">
    Section Name
  </span>
</div>
```

---

## The "Bold Factor" (Signature Elements)

These elements define this implementation and prevent generic output:

1. **Gradient Text Highlights:** Key words in headlines use the signature gradient as text color via `bg-clip-text`.

2. **Inverted Sections:** At least one section uses `bg-foreground text-background` with dot pattern texture for dramatic contrast.

3. **Animated Hero Graphic:** Abstract generative composition with:
   - Rotating outer ring (`animate` with 60s duration, linear)
   - Floating cards with staggered `y` animations (5s and 4s durations, ±10px movement)
   - Geometric shapes (circles, rounded rectangles, gradient fills)
   - Decorative dot grid (3x3)
   - Corner accent block in solid `accent` with shadow

4. **Gradient Icon Backgrounds:** Feature icons use full gradient backgrounds (`from-accent to-accent-secondary`) rather than translucent fills.

5. **Gradient Border Effects:** Highlighted elements (pricing tiers, featured cards) use the 2px gradient stroke technique.

6. **Large Decorative Elements:** Quote marks at `120px`, step numbers at `text-4xl`, trend arrows in badges.

7. **Pulsing Indicators:** Animated dots in badges using scale/opacity keyframes.

8. **Arrow Connectors:** Timeline steps connected by small accent-colored circular badges with arrow icons.

---

## Effects & Animation

**Motion Philosophy:** Smooth, confident, and purposeful. Animations enhance understanding and add delight without being distracting. All motion follows natural easing curves.

**Transition Defaults:**
- Standard: `transition-all duration-200 ease-out`
- Entrance: `duration-700` with stagger (`0.1s` delay between children)
- Hover lifts: `duration-300`
- Button active: `duration-200` with scale down

**Entrance Animations (Framer Motion):**
```js
const easeOut = [0.16, 1, 0.3, 1] as const;

const fadeInUp = {
  hidden: { opacity: 0, y: 28 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.7, ease: easeOut } }
};

const fadeIn = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { duration: 0.7, ease: easeOut } }
};

const stagger = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.1, delayChildren: 0.1 } }
};
```

**Continuous Animations:**
- Rotating ring: `60s` linear infinite rotation (hero graphic)
- Floating cards: `4-5s` ease-in-out infinite y-axis bobbing (±10px amplitude)
- Pulsing dot: `2s` infinite scale/opacity pulse (scale: [1, 1.3, 1], opacity: [1, 0.7, 1])
- Activity indicators: `3s` infinite scale/opacity pulse (subtle)

---

## Responsive Strategy

**Breakpoint Philosophy:** Mobile layouts simplify structure but maintain the bold aesthetic. Touch targets are 44px+ minimum.

- **Hero:** Single column. Hide abstract graphic on small screens. Stack CTAs vertically with full width (`w-full sm:w-auto`).
- **Stats:** 2 columns on mobile → 4 columns on desktop with vertical dividers hidden on mobile
- **Features:** 1 column → 2 columns (md) → 3 columns (lg) with first card spanning on larger screens
- **How It Works:** Vertical stack on mobile, horizontal timeline with connecting line on desktop (md+)
- **Pricing:** Stack vertically, highlighted tier maintains elevation and gradient border
- **Testimonials:** Stack vertically, center card offset removed on mobile
- **Final CTA:** Input and button stack vertically on mobile, horizontal on sm+, button goes full width on mobile

**Key Adaptations:**
- Reduce headline sizes: `text-[2.75rem]` mobile → `text-6xl` → `text-[5.25rem]` desktop
- Maintain generous section padding: `py-28` → `py-44` (reduce slightly, not dramatically)
- Hide decorative elements on mobile: rotating rings, complex graphics (use `hidden lg:block`)
- Keep gradient accents and color inversions—these define the style
- Button heights: `h-12` to `h-14` for primary CTAs (44px-56px touch targets)

---

## Accessibility & Best Practices

**Color Contrast:** All text meets WCAG AA. The `accent` blue (#0052FF) on white background passes at 4.5:1+. Inverted sections use near-white text (#FFFFFF or rgba(255,255,255,0.9)) on deep slate (#0F172A) for maximum contrast.

**Focus States:**
- Visible focus rings using `ring-2 ring-accent ring-offset-2` with `ring-offset-background`
- Focus rings match the gradient accent aesthetic
- Interactive elements have clear hover/focus differentiation (lift, shadow, color shift)
- Buttons have `active:scale-[0.98]` for tactile feedback

**Touch Targets:**
- Minimum 44px height on all interactive elements
- Buttons use `h-12` (48px) to `h-14` (56px) for primary CTAs
- Adequate spacing between tap targets (gap-4 minimum)

**Motion:**
- Respect `prefers-reduced-motion` for continuous animations
- Entrance animations are subtle enough to not cause issues (0.7s duration, 28px vertical movement)
- No flashing or rapid movements
- Continuous animations are slow and gentle (4-5s duration, ±10px movement)

---

## Implementation Notes

**Component Structure:**
All components (Button, Card, Input) are built locally using `cva` and `tailwind-merge`, following Shadcn API patterns but tailored to this design system.

**CSS Custom Properties:**
The StyleWrapper component injects all design tokens as CSS custom properties, allowing for consistent theming across all components.

**Font Loading:**
Fonts are loaded via Google Fonts:
- Inter: weights 400, 500, 600, 700
- Calistoga: default weight
- JetBrains Mono: weights 400, 500

**Animation Library:**
Framer Motion is used for all entrance animations and continuous motion. Viewport options are set to `{ once: true, amount: 0.15, margin: "-60px" }` for optimal performance and timing.
</design-system>
