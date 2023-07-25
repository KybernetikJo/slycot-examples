C FILE: ARRAY.F
      PROGRAM MAIN
         implicit none
         INTEGER :: N = 2
         INTEGER :: M = 2
         INTEGER :: O = 2
         REAL*8 :: A(2)
         REAL*8 :: B(2)
         REAL*8 :: C(2)
         A(1) = 1D0
         A(2) = 1D0
         B(1) = 2D0
         B(2) = 2D0
         C(1) = 3D0
         C(2) = 3D0
         PRINT*, "MAIN A=",A," B=",B," C=",C
         CALL FOO(N,M,O,A,B,C)
         PRINT*, "MAIN A=",A," B=",B," C=",C
      END
