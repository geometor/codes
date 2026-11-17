Family: triangle_center
=======================

9 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``centroid``
     - ``construction``
     - alphageometry, sympy
     - ncoll(A, B, C) => b(C), y(:, C, A), z(:, A, B), i(:, A, X, B, Y), coll(X, B, C), cong(X, B, X, C), y(:, coll, Y, C, A), 
   * - :ref:`centroid_concurrence <centroid_concurrence>`
     - ``theorem``
     - newclid
     - midp(M, A, B), coll(M, X, C), midp(N, B, C), coll(N, X, A), midp(P, C, A) => coll(X, P, B)
   * - ``circumcenter``
     - ``construction``
     - alphageometry, sympy
     - ncoll(A, B, C) => cong(X, A, X, B), cong(X, B, X, C)
   * - :ref:`circumcenter_concurrence <circumcenter_concurrence>`
     - ``theorem``
     - newclid
     - midp(M, A, B), perp(X, M, A, B), midp(N, B, C), perp(X, N, B, C), midp(P, C, A) => perp(X, P, C, A)
   * - ``excenters``
     - ``construction``
     - sympy
     - excenters
   * - ``incenter``
     - ``construction``
     - alphageometry, sympy
     - ncoll(A, B, C) => eq_angle(A, B, A, X, A, X, A, C), eq_angle(C, A, C, X, C, X, C, B), eq_angle(B, C, B, X, B, X, B, A)
   * - :ref:`incenter_concurrence <incenter_concurrence>`
     - ``theorem``
     - newclid
     - eq_angle(A, B, A, X, A, X, A, C), eq_angle(B, A, B, X, B, X, B, C), ncoll(A, B, C) => eq_angle(C, B, C, X, C, X, C, A)
   * - ``orthocenter``
     - ``construction``
     - alphageometry, sympy
     - ncoll(A, B, C) => perp(X, A, B, C), perp(X, B, C, A), perp(X, C, A, B)
   * - :ref:`orthocenter_concurrence <orthocenter_concurrence>`
     - ``theorem``
     - newclid
     - perp(A, B, C, D), perp(A, C, B, D), ncoll(A, B, C) => perp(A, D, B, C)
