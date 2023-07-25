# Slycot Analyse

This subfolder contains some information and tools for the Slycot Module.

## F2PY

F2PY-API is designed with Fortran90/95 in mind.

Generate the `signature file`:

```bash
f2py <file.f> -m <module> -h <signature_file.pyf>
```

```bash
f2py -c <signature_file.pyf> <file.f>
```

## Fortran77

Fortran77
- call-by-reference.
- intent(in,inout,out) `IS NOT` part of Fortran77

## Fortran90/95

Fortran90/95
- call-by-reference.
- intent(in,inout,out) `IS` part of Fortran77


