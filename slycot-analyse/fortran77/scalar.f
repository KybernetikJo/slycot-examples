C FILE: SCALAR.F
      SUBROUTINE FOO(A,B)
         REAL*8 A
         REAL*8 B

         PRINT*, "BEFORE INCREMENT"
         PRINT*, "     A=",A," B=",B
         PRINT*, "INCREMENT A AND B"
         A = A + 1D0
         B = B - 1D0
         PRINT*, "NEW  A=",A," B=",B
      END
C END OF FILE SCALAR.F
