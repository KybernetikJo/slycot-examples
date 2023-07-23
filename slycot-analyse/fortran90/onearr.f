C FILE: ARRAY.F
      SUBROUTINE FOO(N,M,A,B)
C
C     INCREMENT THE FIRST ROW AND DECREMENT THE FIRST COLUMN OF A
C
         INTEGER N, M
         INTEGER I, J
         REAL*8 A(N)
         REAL*8 b(M)

         PRINT*, "BEFORE INCREMENT"
         PRINT*, "     A=",A," B=",B
         PRINT*, "INCREMENT A AND B"
         DO I=1,M
            A(I) = A(I) + 1D0
         ENDDO
         DO J=1,N
            B(J) = B(J) - 1D0
         ENDDO
         PRINT*, "     A=",A," B=",B
      END
C END OF FILE ARRAY.F
