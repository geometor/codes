# Canonical Lexicon — Naming Conventions

The `codes` lexicon gives every geometric concept **one canonical name** and
records what each system calls it. The seed is the function vocabulary of
`geometor.etc` (`etc/src/geometor/etc/ops.py`): wherever systems disagree,
ETC's style wins.

## Rules

1. **snake_case**, ASCII, no abbreviations unless universal (`nine_point_center`,
   not `npc`; `midpoint`, not `midp`).
2. **Constructions are named after what they return**, not the act of
   constructing: `midpoint(A, B)`, `perpendicular_foot(P, L)`,
   `circumcenter(T)`, `equilateral_apex(A, B)`.
   Verb forms (`bisect_segment`, `perpendicular_from`, `find_circle_center`)
   are recorded as aliases.
3. **Predicates are relations** in the indicative: `collinear`, `concyclic`,
   `parallel`, `perpendicular`, `congruent`, `between`, `same_side`; the
   `is_*` form is reserved for unary properties (`is_isosceles`, `is_right`).
4. **Theorems are descriptive noun phrases** of their content:
   `isosceles_base_angles`, `inscribed_angle`, `triangle_angle_sum`,
   `pythagorean`, `thales_intercept`. Classical eponyms are kept when they
   are the common name (`pappus_hexagon`, `simson_line`).
5. **Operators follow ETC / Gibert**: `isogonal_conjugate` (Gibert prefix `g`),
   `isotomic_conjugate` (`t`), `complement` (`c`), `anticomplement` (`a`),
   `circle_inverse` (`i`).
6. **Triangle-derived objects** end in their type: `medial_triangle`,
   `nine_point_circle`, `euler_line`.

## Kinds

| kind | meaning | example |
|---|---|---|
| `object` | a sort / primitive type | `point`, `line`, `circle` |
| `relation` | a predicate on objects | `collinear`, `between` |
| `measure` | a quantity | `quadrance`, `spread`, `length`, `area` |
| `construction` | returns a new object from given ones | `midpoint`, `perpendicular_foot` |
| `center` | a triangle center (ETC X(n)) | `incenter` (X(1)) |
| `triangle` | a derived triangle | `orthic_triangle` |
| `circle` | a derived circle | `nine_point_circle` |
| `operator` | a point-to-point transformation | `isogonal_conjugate` |
| `property` | a unary property | `is_isosceles` |

## Alias systems

`etc`, `elements`, `model`, `alphageometry`, `newclid`, `sympy`, `system_e`,
`geocoq`, `mathlib4`, `gibert`.

An alias must be **unique within its system** (one system name maps to exactly
one canonical concept). SymPy aliases are written `Class.member` and are
checked against the installed SymPy.

## Renames

The lexicon never forces a rename. `codes lexicon audit` *proposes* canonical
names for divergent identifiers in GEOMETOR repos. Any later rename is a
separate branch that keeps the old name as an alias.
