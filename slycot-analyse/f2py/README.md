# Slicot and Slycot

## Slicot

```bash
grep -i " function [a-z][a-z][0-9][0-9a-z][a-z][a-z]("  Slycot/slycot/src/SLICOT-Reference/src/*.f >> slicot_function.out
```

```bash
grep -i " subroutine [a-z][a-z][0-9][0-9a-z][a-z][a-z]("  Slycot/slycot/src/SLICOT-Reference/src/*.f >> slicot_subroutine.out
```

```bash
 find Slycot/slycot/src/SLICOT-Reference/src/ | grep -i [a-z][a-z][0-9][0-9a-z][a-z][a-z].f >> slicot_files.out
```

```bash
 find Slycot/slycot/src/SLICOT-Reference/src/ | grep -v -i [a-z][a-z][0-9][0-9a-z][a-z][a-z].f >> slicot_files2.out
```

## slycot

```bash
grep -i "^subroutine [a-z][a-z][0-9][0-9a-z][a-z][a-z][_,(]"  Slycot/slycot/src/*.pyf >> slycot_subroutine.out
```

```bash
grep -i "function [a-z][a-z][0-9][0-9a-z][a-z][a-z][_,(]"  Slycot/slycot/src/*.pyf >> slycot_function.out
```