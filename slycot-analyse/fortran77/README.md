# FORTRAN77 and F2PY

## Example: scalar.f

### FORTRAN77

```fortran
C FILE: MAIN_SCALAR.F
      PROGRAM MAIN
         REAL*8 :: A
         REAL*8 :: B
         A = 1D0
         B = 2D0
         CALL FOO(A,B)
         PRINT*, "MAIN A=",A," B=",B
      END
```

```fortran
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
```

```bash
f77 main_scalar.f scalar.f -o scalar.out
./a.out
```

```bash
 BEFORE INCREMENT
      A=   1.0000000000000000       B=   2.0000000000000000     
 INCREMENT A AND B
 NEW  A=   2.0000000000000000       B=   1.0000000000000000     
 MAIN A=   2.0000000000000000       B=   1.0000000000000000 
```

### F2PY

```bash
f2py scalar.f -m scalar0 -h scalar.pyf
```

```fortran
!    -*- f90 -*-
! Note: the context of this file is case sensitive.

python module scalar0 ! in 
    interface  ! in :scalar0
        subroutine foo(a,b) ! in :scalar0:scalar.f
            real*8 :: a
            real*8 :: b
        end subroutine foo
    end interface 
end python module scalar0

! This file was auto-generated with f2py (version:1.25.1).
! See:
! https://web.archive.org/web/20140822061353/http://cens.ioc.ee/projects/f2py2e
```

```bash
f2py -c scalar0.pfy scalar.f
```

```python
import numpy as np
import scalar0

a = 1.0
b = 2.0

print("main", a,b)
scalar0.foo(a,b)
print("main", a,b)
```

```
python scalar0.py
```