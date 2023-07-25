C FILE: SCALAR.F
      SUBROUTINE FOO(A,B,C)
         REAL*8 A
         REAL*8 B
         REAL*8 C

         PRINT*, "BEFORE INCREMENT"
         PRINT*, "     A=",A," B=",B," C=",C
         PRINT*, "INCREMENT A AND B"
         A = A + 1D0
         B = B + 2D0
         C = C + 3D0
         PRINT*, "NEW  A=",A," B=",B," C=",C
      END
C END OF FILE SCALAR.F
