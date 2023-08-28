There are many option how to design F2PY `signature files`. The `intent attribute` in `signature files` as tons of options.

===================

However, currently we need a solution for the case, where the parameter are labeled as `input/output` in SLICOT,
are arrays in fortran and numpy arrays in python. Mostly for vectors and matrices e.g state space matrices A,B,C,D.

> Fix options:
> 
> * API-preserving and easiest: change to `intent(in,out)` and update Slycot docstrings where needed.
> * API-changing 1: change to `intent(in,out,copy)`, and returned the resulting matrices
> * API-changing 2: change to `intent(in, copy)`: users expecting mutation will be surprised.
>   
>   * removes capability for users wanting SLICOT results

* API-changing 2: change to `intent(in, copy)`: users expecting mutation will be surprised.

This option would potentially severely limit SLICOT procedures.
I think, if we have an `INPUT/OUTPUT` argument in SLICOT, we should use `intent(in,out)` or `intent(in,out,copy)`.

* API-preserving and easiest: change to `intent(in,out)` and update Slycot docstrings where needed.

Here, we would have to deal with Slycot function side effects somewhere.
We could use `shallow copies` in the outer wrapper python files.
Or we could deal with the side effects in `python-control`.
This could lead to many bugs.

Having said that, there are `inplace` function in python

```python
[].sort()
```

I think in numpy there are not that common. For instance

```python
a_out = np.sort(a)
```

* API-changing 1: change to `intent(in,out,copy)`, and returned the resulting matrices

I still think this is the best option for us. This makes the slycot._wrapper function already more `PYTHONIC`.

===================

We could use even more `intent attribute` in the `signature files` to make the `slycot._wrapper` functions easier and save to use, and more `PYTHONIC`.
This would make massive changes in `pyhton-control` necessary.

The output

```fortran
double precision intent(out) :: ab13bd
```

in the `.pyf` file is there because `ab13bd` is `function` and not a `subrountine`.

In the following example the `optional attribute` with default values is used heavily. The dimension `n,m,p` are determind by `shape`.

```fortran
function ab13bd(dico,jobn,n,m,p,a,lda,b,ldb,c,ldc,d,ldd,nq,tol,dwork,ldwork,iwarn,info) ! in AB13BD.f
    character optional :: dico = 'C'
    character optional :: jobn = 'H'
    integer optional :: n = shape(a,0)
    integer optional :: m = shape(b,1)
    integer optional :: p = shape(c,0)
    double precision dimension(n,n), intent(in,out,copy) :: a
    integer optional, depend(a) :: lda = shape(a,0)
    double precision dimension(n,m), intent(in,out,copy) :: b
    integer optional, depend(b) :: ldb = shape(b,0)
    double precision dimension(p,n), intent(in,out,copy) :: c
    integer optional, depend(c) :: ldc = shape(c,0)
    double precision dimension(p,m), intent(in,out,copy) :: d
    integer optional, depend(d) :: ldd = shape(d,0)
    integer intent(out) :: nq
    double precision optional :: tol = 0.0
    double precision intent(hide,cache),dimension(ldwork),depend(ldwork) :: dwork
    integer optional :: ldwork = max(1,max(m*(n+m)+max(n*(n+5),max(m*(m+2),4*p)),n*(max(n,p)+4)+min(n,p)))
    integer intent(out) :: iwarn
    integer intent(out) :: info
    double precision intent(out) :: ab13bd
end function ab13bd
```

This would allow a minimal function call

```
slycot._wrapper.ab13bd(A,B,C,D)
```

but also some optional attributes

```
out = _wrapper.ab13bd(A, B, C, D, dico=dico, jobn=jobn, n=n, m=m, p=p, tol=tol)
```

are possible.

