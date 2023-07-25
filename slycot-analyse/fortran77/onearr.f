C FILE: ARRAY.F
      SUBROUTINE FOO(M,N,O,A,B,C)
C
C     INCREMENT THE FIRST ROW AND DECREMENT THE FIRST COLUMN OF A
C
         INTEGER M, N, O
         INTEGER I, J, K
         REAL*8 A(N)
         REAL*8 B(M)
         REAL*8 C(O)

         PRINT*, "BEFORE INCREMENT"
         PRINT*, "     A=",A," B=",B," C=",C
         PRINT*, "INCREMENT A AND B"
         DO I=1,M
            A(I) = A(I) + 1D0
         ENDDO
         DO J=1,N
            B(J) = B(J) + 2D0
         ENDDO
         DO K=1,O
            C(K) = C(K) + 3D0
         ENDDO
         PRINT*, "     A=",A," B=",B," C=",C
      END
C END OF FILE ARRAY.F
