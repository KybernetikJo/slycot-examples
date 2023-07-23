# Fortran90/95 F2PY Tests

## Compile f95

```bash
f95 main_scalar.f sclar.f -o _output/scalar.out
```

```bash
f95 main_onearr.f onearr.f -o _output/onearr.out
```

## f2py

```bash
f2py scalar.f -m scalar0 -h scalar0.pyf
```

```bash
f2py -c scalar0.pyf scalar.f
```

```bash
f2py onearr.f -m onearr0 -h onearr.pyf
```

```bash
f2py -c onearr0.pyf onearr.f
```