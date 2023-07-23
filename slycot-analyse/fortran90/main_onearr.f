C FILE: ARRAY.F
      PROGRAM MAIN
         implicit none
         INTEGER :: N = 2
         INTEGER :: M = 2
         REAL*8 :: A(2)
         REAL*8 :: B(2)
         A(1) = 1D0
         A(2) = 2D0
         B(1) = 3D0
         B(2) = 4D0
         PRINT*, "MAIN A=",A," B=",B
         CALL FOO(N,M,A,B)
         PRINT*, "MAIN A=",A," B=",B
      END
