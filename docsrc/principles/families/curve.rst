Family: curve
=============

4 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``sympy_curve``
     - ``sort``
     - sympy
     - A curve in space.
   * - ``sympy_curve_rotate``
     - ``construction``
     - sympy
     - This function is used to rotate a curve along given point ``pt`` at given angle(in radian).
   * - ``sympy_curve_scale``
     - ``construction``
     - sympy
     - Override GeometryEntity.scale since Curve is not made up of Points.
   * - ``sympy_curve_translate``
     - ``construction``
     - sympy
     - Translate the Curve by (x, y).
