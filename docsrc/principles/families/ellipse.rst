Family: ellipse
===============

10 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``sympy_ellipse_bounds``
     - ``construction``
     - sympy
     - Return a tuple (xmin, ymin, xmax, ymax) representing the bounding
   * - ``sympy_ellipse_eccentricity``
     - ``measure``
     - sympy
     - The eccentricity of the ellipse.
   * - ``sympy_ellipse_encloses_point``
     - ``predicate``
     - sympy
     - Return True if p is enclosed by (is inside of) self.
   * - ``sympy_ellipse_equation``
     - ``construction``
     - sympy
     - Returns the equation of an ellipse aligned with the x and y axes;
   * - ``sympy_ellipse_is_tangent``
     - ``predicate``
     - sympy
     - Is `o` tangent to the ellipse?
   * - ``sympy_ellipse_normal_lines``
     - ``construction``
     - sympy
     - Normal lines between `p` and the ellipse.
   * - ``sympy_ellipse_random_point``
     - ``construction``
     - sympy
     - A random point on the ellipse.
   * - ``sympy_ellipse_reflect``
     - ``construction``
     - sympy
     - Override GeometryEntity.reflect since the radius
   * - ``sympy_ellipse_rotate``
     - ``construction``
     - sympy
     - Rotate ``angle`` radians counterclockwise about Point ``pt``.
   * - ``sympy_ellipse_scale``
     - ``construction``
     - sympy
     - Override GeometryEntity.scale since it is the major and minor
