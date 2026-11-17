Family: segments
================

2 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``leaneuclid_unexpand_endpoints``
     - ``definition``
     - leaneuclid
     - Unexpander \| `($_ $t $s) => `(($t ─ $s)) \| _ => throw ()
   * - ``leaneuclid_unexpand_length``
     - ``definition``
     - leaneuclid
     - Lean.PrettyPrinter.Unexpander \| `($_ $i:ident) => `(\|$i:ident\|) \| `($_ ($t:term ─ $s:term)) => `(\|($t:term─$s:term)
