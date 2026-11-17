Family: regularpolygon
======================

8 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``sympy_regularpolygon``
     - ``sort``
     - sympy
     - A regular polygon.
   * - ``sympy_regularpolygon_circumradius``
     - ``measure``
     - sympy
     - Alias for radius.
   * - ``sympy_regularpolygon_encloses_point``
     - ``predicate``
     - sympy
     - Return True if p is enclosed by (is inside of) self.
   * - ``sympy_regularpolygon_inradius``
     - ``measure``
     - sympy
     - Alias for apothem.
   * - ``sympy_regularpolygon_radius``
     - ``measure``
     - sympy
     - Radius of the RegularPolygon
   * - ``sympy_regularpolygon_reflect``
     - ``construction``
     - sympy
     - Override GeometryEntity.reflect since this is not made of only
   * - ``sympy_regularpolygon_rotate``
     - ``construction``
     - sympy
     - Override GeometryEntity.rotate to first rotate the RegularPolygon
   * - ``sympy_regularpolygon_scale``
     - ``construction``
     - sympy
     - Override GeometryEntity.scale since it is the radius that must be
